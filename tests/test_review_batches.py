import unittest

from src.review_batches import batch_ranges


class BatchRangeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(batch_ranges(0), [])

    def test_default_boundary(self):
        self.assertEqual(batch_ranges(21), [(0, 20), (20, 21)])

    def test_exact_boundary(self):
        self.assertEqual(batch_ranges(6, 3), [(0, 3), (3, 6)])

    def test_coverage(self):
        for total in range(30):
            for size in range(1, 12):
                items = [i for start, end in batch_ranges(total, size)
                         for i in range(start, end)]
                self.assertEqual(items, list(range(total)))

    def test_invalid_arguments(self):
        for total in (-1, True, 1.5, "2"):
            with self.assertRaises(ValueError):
                batch_ranges(total)
        for size in (0, -1, False, 1.5, "2"):
            with self.assertRaises(ValueError):
                batch_ranges(3, size)


if __name__ == "__main__":
    unittest.main()
