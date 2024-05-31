"""Привязка переменной к константе."""
class Binding:
    def __init__(self, variable, constant):
        super().__init__()
        self.variable = variable
        self.constant = constant

    def __repr__(self):
        return 'Binding({!r}, {!r})'.format(self.variable, self.constant)

    def __str__(self):
        return f'{self.variable.element.upper()} : {self.constant.element}'
