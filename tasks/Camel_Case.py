"""
Владимир написал свой открытый проект, именуя переменные в стиле «ВерблюжийРегистр».
И только после того, как написал о нём статью, он узнал, что в питоне для имён переменных
принято использовать подчёркивания для разделения слов (under_score).
Нужно срочно всё исправить, пока его не «закидали тапками».

Задача могла бы оказаться достаточно сложной, но, к счастью, Владимир совсем не использовал
строковых констант и классов. Поэтому любая последовательность букв и цифр, внутри которой есть заглавные, —
это имя переменной, которое нужно поправить.
"""

import re

def uncamel(text):
    def change(m):
        return "_" + str(m[0].lower())
    return re.sub(r'(?<=[a-z0-9])[A-Z](?=[a-z0-9])', change, text)


test = """
MyVar17 = OtherVar + YetAnother2Var 
TheAnswerToLifeTheUniverseAndEverything = 42
"""
print(uncamel(test))