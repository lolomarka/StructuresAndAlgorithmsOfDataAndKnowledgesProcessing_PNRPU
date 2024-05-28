from Term import Term
from Variable import Variable


def is_var(var):
    """ Проверяет, является ли элемент переменной (или экземпляром Variable), 
    или термином (экземпляр Term)
    или строка, начинающаяся с '?', например '?d'. 
    """
    if type(var) == str:
        return var[0] == '?'
    if isinstance(var, Term):
        return isinstance(var.term, Variable)
    
    return isinstance(var, Variable)

