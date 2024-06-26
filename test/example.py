import unittest
from KnowledgeBase import KnowledgeBase
from KnowledgeBase.Fact import Fact
from KnowledgeBase.Rule import Rule
from KnowledgeBase.read import read_tokenize
from KnowledgeBase.read import parse_input

class KnowledgeBaseTest(unittest.TestCase):
    def setUp(self):
        file = '/home/lolomarka/Документы/a/StructuresAndAlgorithmsOfDataAndKnowledgesProcessing_PNRPU/test/test_kb.txt'
        self.data = read_tokenize(file)
        self.knowledge_base = KnowledgeBase([], [])
        for item in self.data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.knowledge_base.assert_to_knowledge_base(item)

    def test1(self):
        ask1 = parse_input('fact: (цвет пирамида2 ?X)')
        print('Вопрос: ', ask1)
        answer = self.knowledge_base.ask_knowledge_base(ask1)
        self.assertEqual(str(answer[0]), '?X : оранжевый')
        pprint_justification(answer)
        
    def test2(self):
        ask2 = parse_input('fact: (это пирамида2 ?X)')
        print('Вопрос: ', ask2)
        answer = self.knowledge_base.ask_knowledge_base(ask2)
        self.assertEqual(str(answer[0]), '?X : пирамида')
        pprint_justification(answer)
        
    def test3(self):
        ask3 = parse_input('fact: (является пирамида3 куб)')
        print ('Вопрос: ', ask3)
        answer = self.knowledge_base.ask_knowledge_base(ask3)
        self.assertEqual(answer, [])
        pprint_justification(answer)
            
def pprint_justification(answer):
    if not answer: print('Ответ - нет, нет обоснований')
    else:
        print('\nОбоснования:')
        for i in range(0,len(answer.bindings_list)):
            print(answer.bindings_list[i][0])
            for fact_rule in answer.bindings_list[i][1]:
                pprint_support(fact_rule,0)
                print

def pprint_support(fact_rule, indent):
    if fact_rule:
        print(' '*indent, "следует что")
        if isinstance(fact_rule, Fact):
            print(fact_rule.statement)
        else:
            print(fact_rule.left_hand_statements, "->", fact_rule.right_hand_statements)

        if fact_rule.supported_by:
            for pair in fact_rule.supported_by:
                print(' '*(indent+1), "Одно из подтверждений")
                for next in pair:
                    pprint_support(next, indent+2)

if __name__ == '__main__':
    unittest.main()

# Вопрос:  fact:
#         (цвет пирамида2 ?X)
#          Asserted: True


# Обоснования:
# ?X : оранжевый
#  следует что
# (цвет пирамида2 оранжевый)
# .Вопрос:  fact:
#         (это пирамида2 ?X)
#          Asserted: True


# Обоснования:
# ?X : пирамида
#  следует что
# (это пирамида2 пирамида)
# ?X : блок
#  следует что
# (это пирамида2 блок)
#   Одно из подтверждений
#    следует что
# [Statement('является', [Term(Constant('пирамида')), Term(Variable('?z'))])] -> (это пирамида2 ?z)
#     Одно из подтверждений
#      следует что
# [Statement('это', [Term(Variable('?x')), Term(Variable('?y'))]), Statement('является', [Term(Variable('?y')), Term(Variable('?z'))])] -> (это ?x ?z)
#      следует что
# (это пирамида2 пирамида)
#    следует что
# (является пирамида блок)
# .Вопрос:  fact:
#         (является пирамида3 куб)
#          Asserted: True

# Ответ - нет, нет обоснований
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.007s

# OK