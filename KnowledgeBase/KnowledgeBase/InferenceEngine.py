from .Fact import Fact
from .Rule import Rule

"""Основной движок (на самом деле просто 1 метод.)
Когда мы добавляем новый факт в КБ, мы проверяем, вызывает ли он какое-либо правило (правила).
Когда мы добавляем новое правило, мы проверяем, срабатывает ли оно от существующих фактов.
Однако правило может содержать несколько утверждений в левой части (LHS), 
и мы не хотим выполнять итерации по каждому из этих утверждений каждый раз, когда добавляем новый факт в KB.
Вместо этого всякий раз, когда мы добавляем новое правило, мы будем проверять только первый элемент LHS этого правила на соответствие фактам в нашем KB.
(Если мы добавляем новый факт, мы сделаем обратное - мы рассмотрим каждое правило в нашем KB и проверим первый элемент его LHS на соответствие этому новому факту).
Если есть совпадение с первым элементом, мы добавим новое правило в паре с привязками для этого совпадения.
"""
class InferenceEngine:
    @staticmethod
    def fc_infer(fact: Fact, rule: Rule, knowledge_base):
        bindings = match(rule.left_hand_statements[0], fact.statement)
        if bindings is False:
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
                local_left_hand_statements.append(
                    instantiate(rule.left_hand_statements[i], bindings)
                )
                local_rules.append(local_left_hand_statements)
                local_rules.append(instantiate(rule.right_hand_statements, bindings))
                new_rule = Rule(local_rules, [[rule, fact]])
                rule.supports_rules.append(new_rule)
                fact.supports_rules.append(new_rule)
                knowledge_base.add_to_knowledge_base(new_rule)