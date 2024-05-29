from .Fact import Fact
from .Rule import Rule
from .utils import print_verbose

verbose = 0

def parse_input(el : str):
    """Парсит строковый элемент,
    присваивает метки и разделяет правила на left_hand_rules и right_hand_rules
    """
    if len(el) == 0:
        return None
    elif el[0] == '#':
        # Комментарий
        return el[1:]
    elif el[0:5] == 'fact:':
        # Факт
        el = el[5:].replace(')', '').replace('(', '').rstrip().strip().split()
        return Fact(el)
    elif el[0:5] == 'rule:':
        # Правило
        el = el[5:].split('->')
        rhs = el[1].replace(')', '').replace('(','').rstrip().strip().split()
        lhs = el[0].rstrip(') ').strip('( ').replace('(','').split(')')
        lhs = map(lambda x: x.rstrip().strip().split(), lhs)

        return Rule([lhs, rhs])
    else:
        print_verbose('PARSING ERROR: input header {!r} not recognized', 0, verbose, [el[0:5]])

def read_tokenize(file_path : str):
    """Читает файл и разбивает его на список фактов и правил.
    """
    file = open(file_path, 'r')
    elements = []
    current = ''
    for line in file:
        if line[0:5] in ('fact:', 'rule:'):
            elements.append(current)
            current = line.rstrip()
        else:
            current = current + ' ' + line.rstrip().strip()
    elements.append(current)
    output = []
    for el in elements:
        parsed = parse_input(el)
        if isinstance(parsed, Fact) or isinstance(parsed, Rule):
            output.append(parsed)
    
    file.close()
    return output


def get_new_fact_or_rule():
    prompt = 'Пожалуйста, введите факт или правило, которое вы хотите добавить в базу знаний:\n'
    el = input(prompt)
    return parse_input(el)

def get_new_statements():
    prompt = 'Пожалуйста введите утверждение в форме "pred x1 x2 ...":\n'
    el = input(prompt)
    return el.split()

