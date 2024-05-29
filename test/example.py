import unittest
from KnowledgeBase import read_tokenize
from KnowledgeBase import KnowledgeBase
from KnowledgeBase import Fact
from KnowledgeBase import Rule
from KnowledgeBase import read

class KnowledgeBaseTest(unittest.TestCase):

    def setUp(self):
        file = 'test_kb.txt'
        self.data = read_tokenize(file)
        self.knowledge_base = KnowledgeBase([], [])
        for item in self.data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.knowledge_base.assert_to_knowledge_base(item)

    def test1(self):
        ask1 = read.parse_input('fact: (цвет пирамида2 ?X)')
        print('Вопрос если: ', ask1)
        answer = self.knowledge_base.ask_knowledge_base(ask1)
        print(answer)

if __name__ == '__main__':
    unittest.main()


