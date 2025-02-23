from bfs.count_islands import num_islands

import unittest

class TestCountIslands(unittest.TestCase):

    def test_count_islands(self):
        grid_1 =   [[1, 1, 1, 1, 0], 
                    [1, 1, 0, 1, 0], 
                    [1, 1, 0, 0, 0], 
                    [0, 0, 0, 0, 0]]
        self.assertEqual(1, num_islands(grid_1))
        grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
        self.assertEqual(3, num_islands(grid_2))
        grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
        self.assertEqual(3, num_islands(grid_3))
        grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0]]
        self.assertEqual(5, num_islands(grid_4))


if __name__ == "__main__":
    unittest.main()
