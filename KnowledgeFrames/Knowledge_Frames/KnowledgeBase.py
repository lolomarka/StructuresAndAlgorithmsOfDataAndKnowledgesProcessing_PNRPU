from InferenceEngine import InferenceEngine
from Fact import Fact
from Rule import Rule
from BindingsList import BindingsList
from utils import *

#FOR DEBUG
verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
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

    def ask_knowledge_base(self, fact : Fact):
        print_verbose('Asking {!r}', 0, verbose, [fact])
        if factq(fact):
            f = Fact(fact.statement)
            binding_list = BindingsList()

            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    binding_list.add_bindings(binding, [fact])
            return binding_list if binding_list.bindings_list else []
        
        else:
            print('Invalid ask: ', fact.statement)
            return []
        
        
        

