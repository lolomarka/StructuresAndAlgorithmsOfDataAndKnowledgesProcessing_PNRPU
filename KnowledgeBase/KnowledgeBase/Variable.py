"""Переменная, используемая в выражениях."""
class Variable:
    def __init__(self, element):
        self.element = element

    def __repr__(self):
        return f'Variable({self.element!r})'

    def __str__(self):
        return str(self.element)

    def __eq__(self, other):
        return (
            self is other
            or (isinstance(other, Term) and self.term.element == other.term.element)
            or (
                (isinstance(other, Variable) or isinstance(other, Constant))
                and self.term.element == other.element
            )
        )

    def __ne__(self, other):
        return not self == other
