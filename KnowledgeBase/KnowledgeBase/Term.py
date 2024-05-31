from .Constant import Constant
from .Variable import Variable
from .utils import is_var

"""Термин (константа или переменная)."""
class Term:
    def __init__(self, term):
        """
        Конструктор термина - приводит к требуемой форме.
        """
        is_var_or_const = isinstance(term, (Variable, Constant))
        self.term = term if is_var_or_const else (Variable(term) if is_var(term) else Constant(term))

    def __repr__(self):
        return 'Term({!r})'.format(self.term)
    
    def __str__(self):
        return str(self.term)
    
    def __eq__(self, other):
        return (
            self is other
            or isinstance(other, Term)
            and self.term.element == other.term.element
            or (
                isinstance(other, (Variable, Constant))
                and self.term.element == other.element
            )
        )

    def __ne__(self, other):
        return not self.__eq__(other)
