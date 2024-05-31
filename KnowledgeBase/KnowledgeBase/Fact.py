from .Statement import Statement

"""Факт в базе знаний.
   Содержит утверждение, например человек - животное и поля, для отслеживания,
   какие факты/правила в БЗ этот факт подтверждают, или их подтверждает этот факт.
"""
class Fact:
    def __init__(self, statement, supported_by=None):
        if supported_by is None:
            supported_by = []
        self.name = 'fact'
        self.statement = statement if isinstance(statement, Statement) else Statement(statement)
        self.asserted = not supported_by
        self.supported_by = supported_by
        self.supports_facts = []
        self.supports_rules = []

    def __repr__(self):
        return 'Fact({!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.name,
            self.statement,
            self.asserted,
            self.supported_by,
            self.supports_facts,
            self.supports_rules
        )

    def __str__(self):
        string = self.name + ":\n"
        string += f'\t{str(self.statement)}\n'
        string += f'\t Asserted: {str(self.asserted)}\n'
        if any(self.supported_by):
            name_strings = [str(x.name) for y in self.supported_by for x in y]
            supported_by_str = ', '.join(name_strings)
            string += f'\t Supported by: [{supported_by_str}]\n'
        if any(self.supports_facts):
            name_strings = [str(x.name) for x in self.supports_facts]
            supports_fact_str = ', '.join(name_strings)
            string += f'\t Supports facts: [{supports_fact_str}]\n'
        if any(self.supports_rules):
            name_strings = [str(x.name) for x in self.supports_rules]
            supports_rules_str = ', '.join(name_strings)
            string += f'\t Supports rules: [{supports_rules_str}]\n'
        return string

    def __eq__(self, other):
        return isinstance(other, Fact) and self.statement == other.statement

    def __ne__(self, other):
        return not self == other
