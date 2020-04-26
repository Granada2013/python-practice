from typing import Dict
import re
from papers_please.visitor_cls import Visitor


class Inspector:
    _NATIONS = ["Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation", "N/A"]
    _FOREIGNERS = ["Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation", "N/A"]

    def __init__(self):
        self.parsed_bulletin: dict = {nation: dict(zip(('Allowed_to_enter', 'Docs_required', 'Vaccinas_required'),
                                                       (False, set(), set()))) for nation in Inspector._NATIONS}
        self.criminal_wanted: str = ''
        self.work_pass_required = False

    def __parse_line_to_field(self, field_name: str, fillwith: str, text: str) -> None:
        if text.startswith('Entrants'):
            nations = Inspector._NATIONS
        elif text.startswith('Foreigners'):
            nations = Inspector._FOREIGNERS
        elif text.startswith('Citizens of'):
            nations = re.search(r'(?<=of\s).+(?= no longer)|(?<=of\s).+(?= require)', text)[0].split(', ')
        for nation in nations:
            if 'no longer' in text:
                self.parsed_bulletin[nation][field_name].discard(fillwith)
            else:
                self.parsed_bulletin[nation][field_name].add(fillwith)

    def receive_bulletin(self, bulletin: str) -> None:
        self.criminal_wanted = ''

        for line in bulletin.splitlines():
            if line.startswith('Allow citizens') or line.startswith('Deny citizens'):
                nations = line.split('of ')[1].split(', ')
                for nation in nations:
                    if line.startswith('Allow'):
                        self.parsed_bulletin[nation]['Allowed_to_enter'] = True
                    else:
                        self.parsed_bulletin[nation]['Allowed_to_enter'] = False

            elif 'vaccination' in line:
                vac = re.search(r'(?<=require ).+(?= vaccination)', line)[0]
                self.__parse_line_to_field(field_name='Vaccinas_required', fillwith=vac, text=line)

            elif 'Worker' in line:
                self.work_pass_required = False if 'no longer' in line else True

            elif 'require' in line:
                doc = re.sub(r' ', '_', re.search(r'(?<=require ).+', line)[0])
                self.__parse_line_to_field(field_name='Docs_required', fillwith=doc, text=line)

            elif line.startswith('Wanted by the State'):
                self.criminal_wanted = line.split(': ')[1]

    def inspect(self, entrant: Dict[str, str]) -> str:
        visitor = Visitor(entrant)

        if visitor.is_criminal(self.criminal_wanted) or visitor.has_mismatch():
            return "Detainment: {}".format(
                'Entrant is a wanted criminal.' if visitor.is_criminal(criminal=self.criminal_wanted)
                else f'{visitor.has_mismatch()} mismatch.')

        if visitor.missed_required_docs(docs_required=self.parsed_bulletin[visitor.nation]['Docs_required'],
                                        work_pass_req=self.work_pass_required):
            docs = visitor.missed_required_docs(docs_required=self.parsed_bulletin[visitor.nation]['Docs_required'],
                                                work_pass_req=self.work_pass_required)
            return f"Entry denied: missing required {docs}."

        if 'diplomatic_authorization' in visitor.data and visitor.has_invalid_dipl_auth():
            return 'Entry denied: invalid diplomatic authorization.'

        if not self.parsed_bulletin[visitor.nation]['Allowed_to_enter']:
            return f"Entry denied: citizen of banned nation."

        if visitor.has_expired_documents():
            return f"Entry denied: {visitor.has_expired_documents()} expired."

        if visitor.missed_vaccunations(vacuns_required=self.parsed_bulletin[visitor.nation]['Vaccinas_required']):
            vac = visitor.missed_vaccunations(vacuns_required=self.parsed_bulletin[visitor.nation]['Vaccinas_required'])
            return f"Entry denied: {vac}."

        return "{}".format('Glory to Arstotzka.' if visitor.nation == 'Arstotzka' else 'Cause no trouble.')


