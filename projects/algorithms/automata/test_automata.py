import unittest

from dfa import DFA

class TestDFA(unittest.TestCase):
    def test_DFA(self):
        transitions = {
            'a': {'1': 'a', '0': 'b'},
            'b': {'1': 'b', '0': 'a'}
        }

        final = ['a']
        start = 'a'

        self.assertEqual(False, DFA(transitions, start, final, "000111100"))
        self.assertEqual(True, DFA(transitions, start, final, "111000011"))

        transitions1 = {
            '0': {'0': '1', '1': '0'},
            '1': {'0': '2', '1': '0'},
            '2': {'0': '2', '1': '3'},
            '3': {'0': '3', '1': '3'}
        }
        final1 = ['0', '1', '2']
        start1 = '0'

        self.assertEqual(False, DFA(transitions1, start1, final1, "0001111"))
        self.assertEqual(True, DFA(transitions1, start1, final1, "01010101"))

        transitions2 = {
            '0': {'a': '0', 'b': '1'},
            '1': {'a': '0', 'b': '2'},
            '2': {'a': '3', 'b': '2'},
            '3': {'a': '3', 'b': '3'}
        }
        final2 = ['3']
        start2 = '0'

        self.assertEqual(False, DFA(transitions2, start2, final2, "aaabbb"))
        self.assertEqual(True, DFA(transitions2, start2, final2, "baabba"))

    def setUp(self):
        """初始化测试数据"""
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q0'}
        }
        self.start = 'q0'
        self.final = ['q1']

    def test_accept_valid_string(self):
        self.assertTrue(DFA(self.transitions, self.start, self.final, "a"))
        self.assertTrue(DFA(self.transitions, self.start, self.final, "aaa"))

    def test_reject_invalid_string(self):
        self.assertFalse(DFA(self.transitions, self.start, self.final, "b"))
        self.assertFalse(DFA(self.transitions, self.start, self.final, "bb"))

    def test_empty_string(self):
        """测试空字符串是否被正确处理"""
        self.assertFalse(DFA(self.transitions, self.start, self.final, ""))

    
if __name__ == '__main__':
    unittest.main()


'''
from dfa import DFA #绝对路径导入， 在automata目录下当独立脚本运行: python3 test_automata.py
from .dfa import DFA #相对路径导入，在automata的上一级目录里把automata当python包(因为已有__init__.py文件)运行: python3 -m automata.test_automata
'''
