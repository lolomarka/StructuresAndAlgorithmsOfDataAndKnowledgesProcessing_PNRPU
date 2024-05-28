from Constant import Constant
from Variable import Variable
from utils import is_var

class Term(object):
    """Термин (константа или переменная)
    """
    def __init__(self, term):
        """
        Конструктор термина - приводит к требуемой форме
        """
        super(Term, self).__init__()
        is_var_or_const = isinstance(term, Variable) or isinstance(term, Constant)
        self.term = term if is_var_or_const else (Variable(term) if is_var(term) else Constant(term))

    def __repr__(self):
        return 'Term({!r})'.format(self.term)
    
    def __str__(self):
        return str(self.term)
    
    def __eq__(self, other):
        return (self is other
                or isinstance(other, Term) and self.term.element == other.term.element
                or ((isinstance(other, Variable) or isinstance(other, Constant))
                    and self.term.element == other.element))
    
    def __ne__(self, other):
        return not self == other