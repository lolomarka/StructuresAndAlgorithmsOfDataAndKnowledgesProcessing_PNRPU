from .Fact import Fact
from .Rule import Rule
from .utils import *

class InferenceEngine(object):
    def fc_infer(self, fact : Fact, rule : Rule, knowledge_base):
        bindings = match(rule.left_hand_statements[0], fact.statement)

        if bindings == False:
            return None
        
        if len(rule.left_hand_statements) == 1:
            new_fact = Fact(instantiate(rule.right_hand_statements, bindings), [[rule, fact]])
            rule.supports_facts.append(new_fact)
            fact.supports_facts.append(new_fact)
            knowledge_base.add_to_knowledge_base(new_fact)
        else:
            local_left_hand_statements = []
            local_rules = []
            for i in range(1, len(rule.left_hand_statements)):
                local_left_hand_statements.append(instantiate(rule.left_hand_statements[i], bindings))
                local_rules.append(local_left_hand_statements)
                local_rules.append(instantiate(rule.right_hand_statements, bindings))
                new_rule = Rule(local_rules, [[rule, fact]])
                rule.supports_rules.append(new_rule)
                fact.supports_rules.append(new_rule)
                knowledge_base.add_to_knowledge_base(new_rule)
