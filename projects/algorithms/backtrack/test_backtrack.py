#import os
#import importlib

# get all the python files in current folder except __init__.py and test_backtrack.py
#module_files = [f[:-3] for f in os.listdir(os.path.dirname(__file__))
#                if f.endswith(".py") and f not in ("__init__.py", "test_backtrack.py")]

# import all modules dynamically
#for module in module_files:
#    importlib.import_module(module)
#from backtrack import add_operators # import the modules in backtrack directly 这里不适用，编译会报错说模块对象不可调用，因为这里的add_operators不是module，而是一个函数
from backtrack.add_operators import add_operators  # other alternative: import the specific func/class
from backtrack.anagram import anagram

import unittest

class TestAddOperator(unittest.TestCase):
    def test_add_operators(self):
        #"123", 6 -> ["1+2+3", "1*2*3"]
        s = "123"
        target = 6
        self.assertEqual(add_operators(s, target), ["1+2+3", "1*2*3"])
        # "232", 8 -> ["2*3+2", "2+3*2"]
        s = "232"
        target = 8
        self.assertEqual(add_operators(s, target), ["2+3*2", "2*3+2"])

        s = "123045"
        target = 3
        answer = ['1+2+3*0*4*5',
                  '1+2+3*0*45',
                  '1+2-3*0*4*5',
                  '1+2-3*0*45',
                  '1-2+3+0-4+5',
                  '1-2+3-0-4+5',
                  '1*2+3*0-4+5',
                  '1*2-3*0-4+5',
                  '1*23+0-4*5',
                  '1*23-0-4*5',
                  '12+3*0-4-5',
                  '12-3*0-4-5']
        self.assertEqual(add_operators(s, target), answer)

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram('apple', 'pleap'))
        self.assertFalse(anagram("apple", "cherry"))

if __name__ == '__main__':
    unittest.main()

#__init__.py里用的是相对路径，所以这里只能在backtrack的上一级目录里把这些.py文件当python包运行：python3 -m backtrack.test_backtrack
