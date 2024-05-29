from Statement import Statement

class Rule(object):
    def __init__(self, rule, supported_by=[]):
        super(Rule, self).__init__()
        self.name = rule
        self.left_hand_statements = [statement if isinstance(statement, Statement) else Statement(statement) for statement in rule[0]]
        self.right_hand_statements = rule[1] if isinstance(rule[1], Statement) else Statement(rule[1])
        self.asserted = not supported_by
        self.supported_by = supported_by
        self.supports_facts = []
        self.supports_rules = []

    def __repr__(self):
        return 'Rule({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.name, self.left_hand_statements, self.right_hand_statements,
            self.asserted, self.supported_by,
            self.supports_facts, self.supports_rules)
    
    def __str__(self):
        string = f'{self.name}:\n'
        string += f'\t Left hand:\n'
        for statement in self.left_hand_statements:
            string += f'\t\t{str(statement)}\n'
        string += f'\t Right hand:\n\t\t{str(self.right_hand_statements)}\n'
        string += f'\t Asserted: {self.asserted}\n'
        
        if any(self.supported_by):
            name_strings = [str(x.name) for y in self.supported_by for x in y]
            supported_by_str = str.join(', ', name_strings)
            string += f'\t Supported by: [{supported_by_str}]\n'
        if any(self.supports_facts):
            name_strings = [str(x.name) for x in self.supports_facts]
            supports_fact_str = str.join(', ', name_strings)
            string += f'\t Supports facts: [{supports_fact_str}]\n'
        if any(self.supports_rules):
            name_strings = [str(x.Name) for x in self.supports_rules]
            supports_rules_str = str.join(', ', name_strings)
            string += f'\t Supports rules: [{supports_rules_str}]\n'
        return string
    
    def __eq__(self, other):
        return isinstance(other, Rule) and self.left_hand_statements == other.left_hand_statements and self.right_hand_statements == other.right_hand_statements
    
    def __ne__(self, other):
        return not self == other
