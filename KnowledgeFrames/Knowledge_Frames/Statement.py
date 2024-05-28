from Term import Term

class Statement(object):
    """Утверждение
    """
    def __init__(self, statement_list=[]):
        super(Statement, self).__init__()
        self.terms = []
        self.predicate = ''
        if statement_list:
            self.predicate = statement_list[0]
            self.terms = [t if isinstance(t, Term) else Term(t) for t in statement_list[1:]]

    def __repr__(self):
        return 'Statement({!r}, {!r})'.format(self.predicate, self.terms)

    def __str__(self):
        return f'({self.predicate} {str.join(' ', (str(t) for t in self.terms))})'
    
    def __eq__(self, other):
        if self.predicate != other.predicate:
            return False
        
        for self_term, other_term in zip(self.terms, other.terms):
            if self_term != other_term:
                return False
        
        return True
    
    def __ne__(self, other):
        return not self == other