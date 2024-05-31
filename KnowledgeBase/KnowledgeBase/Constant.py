"""Константа, используемая в выражении."""
class Constant:
    def __init__(self, element):
        super().__init__()
        self.element = element

    def __repr__(self):
        return 'Constant({!r})'.format(self.element)

    def __str__(self):
        return str(self.element)

    def __eq__(self, other):
        return (
            self is other 
            or (isinstance(other, Term) and self.element == other.term.element)
            or ((isinstance(other, Variable) or isinstance(other, Constant)) and self.element == other.element)
        )

    def __ne__(self, other):
        return not self == other
