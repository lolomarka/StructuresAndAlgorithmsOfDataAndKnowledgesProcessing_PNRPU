from .Rule import Rule
from .Fact import Fact
from .utils import *

#FOR DEBUG
verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        
        from .InferenceEngine import InferenceEngine
        self.infer_engine = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = 'Knowledge Base: \n'
        string += f'{str.join('\n', (str(fact) for fact in self.facts))}\n'
        string += f'{str.join('\n', (str(rule) for rule in self.rules))}'
        return string
    
    def _get_fact(self, fact):
        """INTERNAL"""

        for kb_fact in self.facts:
            if fact == kb_fact:
                return kb_fact
            
    def _get_rule(self, rule):
        """INTERNAL"""
        for kb_rule in self.rules:
            if rule == kb_rule:
                return kb_rule
            
    def add_to_knowledge_base(self, fact_or_rule):
        print_verbose('Adding {!r}', 1, verbose, [fact_or_rule])
        if isinstance(fact_or_rule, Fact):
            if fact_or_rule not in self.facts:
                self.facts.append(fact_or_rule)
                for rule in self.rules:
                    self.infer_engine.fc_infer(fact_or_rule, rule, self)
            else:
                if fact_or_rule.supported_by:
                    index = self.facts.index(fact_or_rule)
                    for f in fact_or_rule.supported_by:
                        self.facts[index].supported_by.append(f)
                else:
                    index = self.facts.index(fact_or_rule)
                    self.facts[index].asserted = True
        elif isinstance(fact_or_rule, Rule):
            if fact_or_rule not in self.rules:
                self.rules.append(fact_or_rule)
                for fact in self.facts:
                    self.infer_engine.fc_infer(fact, fact_or_rule, self)
            else:
                if fact_or_rule.supported_by:
                    index = self.rules.index(fact_or_rule)
                    for f in fact_or_rule.supported_by:
                        self.rules[index].supported_by.append(f)
                else:
                    index = self.rules.index(fact_or_rule)
                    self.rules[index].asserted = True
        

    def assert_to_knowledge_base(self, fact_or_rule):
        print_verbose('Asserting {!r}', 0, verbose, [fact_or_rule])
        self.add_to_knowledge_base(fact_or_rule)

    def ask_knowledge_base(self, fact):
        print_verbose('Asking {!r}', 0, verbose, [fact])
        if factq(fact):
            f = Fact(fact.statement)
            
            from .BindingsList import BindingsList  
            binding_list = BindingsList()

            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    binding_list.add_bindings(binding, [fact])
            return binding_list if binding_list.bindings_list else []
        
        else:
            print('Invalid ask: ', fact.statement)
            return []
        
    def retract_from_knowledge_base(self, fact_or_rule):
        print_verbose('Retracting {!r}', 0, verbose, [fact_or_rule])

        if len(fact_or_rule.supported_by) != 0:
            return None
        
        if isinstance(fact_or_rule, Rule):
            if fact_or_rule in self.rules and len(fact_or_rule.supported_by) == 0:
                self.rules.remove(fact_or_rule)

        if isinstance(fact_or_rule, Fact):
            flag = False
            for x in self.facts:
                if fact_or_rule.statement == x.statement:
                    fact_or_rule = x
                    flag = True
                    break

                if not flag:
                    return None
                
                if len(fact_or_rule.supported_by) == 0:
                    self.facts.remove(fact_or_rule)

        # Ищем все поддерживаемые факты
        for temp in fact_or_rule.supports_facts:
            temp_len = 0
            standard = len(temp.supported_by)
            for x in temp.supported_by:
                if fact_or_rule in x:
                    temp.supported_by.remove(x)
                    temp_len += 1

                if standard == temp_len:
                    self.retract_from_knowledge_base(temp)

        # Ищем все поддерживаемые правила
        for temp in fact_or_rule.supports_rules:
            temp_len = 0
            standard = len(temp.supported_by)
            for y in temp.supported_by:
                if fact_or_rule in y:
                    temp.supported_by.remove(y)
                    temp_len += 1
            
            if standard == temp_len:
                self.retract_from_knowledge_base(temp)
        

