from .Bindings import Bindings

def is_var(var):
    """Проверяет, является ли элемент переменной (или экземпляром Variable),
    или термином (экземпляр Term)
    или строка, начинающаяся с '?', например '?d'.
    """
    from .Term import Term
    from .Variable import Variable
    
    if type(var) == str:
        return var[0] == '?'
    if isinstance(var, Term):
        return isinstance(var.term, Variable)
    return isinstance(var, Variable)


def match_recursive(terms1, terms2, bindings):
    """
    Вспомогательный рекурсивный метод для сопоставления (метод match)
    """

    if len(terms1) == 0:
        return bindings
    if is_var(terms1[0]):
        if not bindings.test_and_bind(variable_term=terms1[0], value_term=terms2[0]):
            return False
    elif is_var(terms2[0]):
        if not bindings.test_and_bind(terms2[0], terms1[0]):
            return False
    elif terms1[0] != terms2[0]:
        return False
    return match_recursive(terms1[1:], terms2[1:], bindings)

def match(state1, state2, bindings=None):
    """Сопоставляет два высказывания и возвращает связанные с ним binding-и."""
    if len(state1.terms) != len(state2.terms) or state1.predicate != state2.predicate:
        return False
    if not bindings:
        bindings = Bindings()
    return match_recursive(state1.terms, state2.terms, bindings)


def instantiate(statement, bindings):
    """Генерирует утверждение из переданных утверждений и binding-ов."""
    from .Statement import Statement

    from .Term import Term

    def handle_term(term):
        if is_var(term):
            binded_value = bindings.bound_to(term.term)
            return Term(binded_value) if binded_value else term
        return term

    new_terms = [handle_term(term) for term in statement.terms]
    return Statement([statement.predicate] + new_terms)


def factq(element):
    """Проверяет, что переданный элемент - факт"""
    from .Fact import Fact
    return isinstance(element, Fact)

def print_verbose(message, level, verbose, data=[]):
    """Выводит отформатированное сообщение, если переданный verbose больше уровня"""
    if verbose > level:
        print(message.format(*data) if data else message)