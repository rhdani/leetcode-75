import unittest
from slidingWindowMedian import median_sliding_window

class TestMedianSlidingWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            median_sliding_window([1,3,-1,-3,5,3,6,7], 3),
            [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        )
        self.assertEqual(
            median_sliding_window([3, 1, 2, -1, 0, 5, 8], 4),
            [1.5, 0.5, 1.0, 2.5]
        )
        self.assertEqual(median_sliding_window([1,2], 1), [1.0, 2.0])
        self.assertEqual(median_sliding_window([4,7,2,21], 2), [5.5, 4.5, 11.5])
        self.assertEqual(median_sliding_window([1,1,1,1,1], 2), [1.0, 1.0, 1.0, 1.0])

    def test_edge_cases(self):
        # k equals length
        self.assertEqual(median_sliding_window([5,2,3], 3), [3.0])
        # empty input
        self.assertEqual(median_sliding_window([], 3), [])
        # k = 0 (undefined) -> expect []
        self.assertEqual(median_sliding_window([1,2,3], 0), [])

    def test_k_one(self):
        # when k=1, medians should be the original elements as floats
        arr = [5, -2, 3, 8, 0]
        expected = [float(x) for x in arr]
        self.assertEqual(median_sliding_window(arr, 1), expected)

if __name__ == '__main__':
    unittest.main()
