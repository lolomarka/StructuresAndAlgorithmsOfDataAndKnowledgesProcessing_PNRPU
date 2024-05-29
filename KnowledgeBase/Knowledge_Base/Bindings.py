from Binding import Binding
from Variable import Variable
from Constant import Constant
from utils import is_var

class Bindings(object):
    def __init__(self):
        self.bindings = []
        self.bindings_dict = {}

    def __repr__(self):
        return 'Bindings({!r}, {!r})'.format(self.bindings_dict, self.bindings)
    
    def __str__(self):
        if not any(self.bindings):
            return 'No bindings'
        return str.join(', ', (str(binding) for binding in self.bindings))
    
    def __getitem__(self, key):
        return (self.bindings_dict[key]
                if (self.bindings_dict and key in self.bindings_dict)
                else None)
    
    def add_binding(self, variable : Variable, value : Constant):
        self.bindings_dict[variable.element] = value.element
        self.bindings.append(Binding(variable, value))

    def bound_to(self, variable : Variable):
        if variable.element in self.bindings_dict.keys():
            value = self.bindings_dict[variable.element]
            if value:
                return Variable(value) if is_var(value) else Constant(value)
            
        return False
    
    def test_and_bind(self, variable_term, value_term):
        bound = self.bound_to(variable_term.term)
        if bound:
            return value_term.term == bound
        
        self.add_binding(variable_term.term, value_term.term)
        return True