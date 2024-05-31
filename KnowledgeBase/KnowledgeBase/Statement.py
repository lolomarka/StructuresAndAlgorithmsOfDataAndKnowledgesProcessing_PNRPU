from .Term import Term

"""Утверждение"""
class Statement:
    def __init__(self, statement_list=None):
        if statement_list is None:
            statement_list = []
        self.terms = []
        self.predicate = ''
        if statement_list:
            self.predicate = statement_list[0]
            self.terms = [t if isinstance(t, Term) else Term(t) for t in statement_list[1:]]

    def __repr__(self):
        return 'Statement({!r}, {!r})'.format(self.predicate, self.terms)

    def __str__(self):
        return f'({self.predicate} {" ".join(str(t) for t in self.terms)})'
    
    def __eq__(self, other):
        if not isinstance(other, Statement):
            return False
        if self.predicate != other.predicate:
            return False
        return all(self_term == other_term for self_term, other_term in zip(self.terms, other.terms))
    
    def __ne__(self, other):
        return not self.__eq__(other)
