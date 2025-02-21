from dfs.count_islands import num_islands

import unittest

class TestCountIslands(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(1, num_islands([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0],
                                         [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
        self.assertEqual(3, num_islands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                                         [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]))

if __name__ == "__main__":
    unittest.main()