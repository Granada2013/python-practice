from typing import List, Dict, Union
import re
from datetime import datetime


class Visitor:
    FIELDS: dict = {'NAME': 'name',
                    'NATION': 'nationality',
                    'ID#': 'ID number',
                    'HEIGTH': 'height',
                    'WEIGHT': 'weight',
                    'DOB': 'date of birth'}

    def __init__(self, entrant: Dict[str, str]):
        self.data: dict = {}
        self.nation: str = 'N/A'

        self.__parse_entrant_data(entrant)
        self.__generate_nation()

    def __parse_entrant_data(self, entrant: Dict[str, str]) -> None:
        def parse_string(string: str) -> Dict[str, str]:
            parsed_string = {}
            splitted_str = re.split(":|\n", string)
            for i in range(0, len(splitted_str) - 1, 2):
                parsed_string[splitted_str[i]] = splitted_str[i + 1].strip()
            return parsed_string

        for key, value in entrant.items():
            self.data[key] = parse_string(value)

    def __generate_nation(self) -> None:
        if 'ID_card' in self.data:
            self.nation = 'Arstotzka'
        else:
            for key, value in self.data.items():
                if 'NATION' in value:
                    self.nation = value['NATION']
                    break

    def __is_worker(self):
        return 'access_permit' in self.data and self.data['access_permit']['PURPOSE'] == 'WORK'

    def __has_work_pass(self):
        return 'work_pass' in self.data

    def is_criminal(self, criminal: str) -> bool:
        for key in self.data:
            name = self.data[key]['NAME'].split(',')
            name[0], name[1] = name[1], name[0]
            if ' '.join(name).strip() == criminal:
                return True
        return False

    def has_mismatch(self) -> Union[str, bool]:
        def dicts_mismatch(d1: dict, d2: dict) -> Union[str, bool]:
            set_keys = [set(d.keys()) for d in (d1, d2)]
            common_keys = set_keys[0] & set_keys[1]
            for key in common_keys:
                if d1[key] != d2[key] and key != 'EXP':
                    return Visitor.FIELDS[key]
            return False

        if len(self.data) > 1:
            keys = list(self.data)
            for i in range(len(keys) - 1):
                d1 = self.data[keys[i]]
                for j in range(i + 1, len(keys)):
                    d2 = self.data[keys[j]]
                    return dicts_mismatch(d1, d2)
        return False

    def has_expired_documents(self) -> Union[str, bool]:
        for key, value in self.data.items():
            for key1, value1 in value.items():
                if key1 == 'EXP':
                    exp_data = datetime.strptime(value1, '%Y.%m.%d')
                    if exp_data <= datetime(1982, 11, 22):
                        return re.sub(r'_', ' ', key)
        return False

    def missed_vaccunations(self, vacuns_required: List[str]) -> Union[str, bool]:
        if vacuns_required:
            if 'certificate_of_vaccination' not in self.data:
                return 'missing required certificate of vaccination'
            for vac in vacuns_required:
                if vac not in self.data['certificate_of_vaccination']['VACCINES'].split(', '):
                    return 'missing required vaccination'
        return False

    def has_invalid_dipl_auth(self) -> bool:
        return 'Arstotzka' not in self.data['diplomatic_authorization']['ACCESS'].split(', ')

    def missed_required_docs(self, docs_required: List[str], work_pass_req: bool = False) -> Union[str, bool]:
        for doc in docs_required:
            if doc not in self.data:
                if doc == 'access_permit' and (
                        'grant_of_asylum' in self.data or 'diplomatic_authorization' in self.data):
                    continue
                else:
                    return re.sub('_', ' ', doc)
        if work_pass_req:
            if self.__is_worker() and not self.__has_work_pass():
                return 'work pass'
        return False
