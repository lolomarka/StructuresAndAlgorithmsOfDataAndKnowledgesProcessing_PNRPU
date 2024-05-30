""" Константа, используемая в выражении. """
class Constant(object):
    def __init__(self, element):
        super(Constant, self).__init__()
        self.element = element

    def __repr__(self):
        return 'Constant({!r})'.format(self.element)
    
    def __str__(self):
        return str(self.element)
    
    def __eq__(self, other):
        return (self is other 
            or (isinstance(other, Term) and self.term.element == other.term.element)
            or (((isinstance(other, Variable) or isinstance(other, Constant)) and self.term.element == other.element)))
    
    def __ne__(self, other):
        return not self == other