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
        print(answer)
        
    def test2(self):
        ask2 = parse_input('fact: (это пирамида2 ?X)')
        print('Вопрос: ', ask2)
        answer = self.knowledge_base.ask_knowledge_base(ask2)
        print(answer)

if __name__ == '__main__':
    unittest.main()


