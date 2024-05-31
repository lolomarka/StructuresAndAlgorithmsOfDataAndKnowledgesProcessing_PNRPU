from .Fact import Fact
from .Rule import Rule
from .utils import print_verbose

verbose = 0

"""Набор вспомогательных методов для чтения из файла/терминала."""

def parse_input(el: str):
    """Парсит строковый элемент,
    присваивает метки и разделяет правила на left_hand_rules и right_hand_rules.
    """
    if len(el) == 0:
        return None
    if el[0] == '#':
        # Комментарий
        return el[1:]
    if el[0:5] == 'fact:':
        # Факт
        el = el[5:].replace(')', '').replace('(', '').rstrip().strip().split()
        return Fact(el)
    if el[0:5] == 'rule:':
        # Правило
        el = el[5:].split('->')
        rhs = el[1].replace(')', '').replace('(', '').rstrip().strip().split()
        lhs = el[0].rstrip(') ').strip('( ').replace('(', '').split(')')
        lhs = [x.rstrip().strip().split() for x in lhs]

        return Rule([lhs, rhs])
    print_verbose('PARSING ERROR: input header {!r} not recognized', 0, verbose, [el[0:5]])
    return None

def read_tokenize(file_path: str):
    """Читает файл и разбивает его на список фактов и правил."""
    with open(file_path, 'r') as file:
        elements = []
        current = ''
        for line in file:
            if line[0:5] in {'fact:', 'rule:'}:
                if current:
                    elements.append(current)
                current = line.rstrip()
            else:
                current += ' ' + line.rstrip().strip()
        if current:
            elements.append(current)
        output = []
        for el in elements:
            parsed = parse_input(el)
            if isinstance(parsed, (Fact, Rule)):
                output.append(parsed)

    return output

def get_new_fact_or_rule():
    prompt = "Пожалуйста, введите факт или правило, которое вы хотите добавить в базу знаний:\n"
    el = input(prompt)
    return parse_input(el)

def get_new_statements():
    prompt = 'Пожалуйста введите утверждение в форме "pred x1 x2 ...":\n'
    el = input(prompt)
    return el.split()
