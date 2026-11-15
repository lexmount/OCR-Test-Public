"""Offline, standard-library checks for the review progress fixture."""
import unittest

from src.review_rollout_probe import completed_ratio


class ReviewProgressTests(unittest.TestCase):
    def test_empty_batch_is_complete(self):
        self.assertEqual(completed_ratio(0, 0), 1.0)

    def test_no_completed_reviews(self):
        self.assertEqual(completed_ratio(0, 4), 0.0)

    def test_all_reviews_complete(self):
        self.assertEqual(completed_ratio(4, 4), 1.0)

    def test_partial_progress_keeps_fraction(self):
        self.assertEqual(completed_ratio(1, 2), 0.5)
        self.assertAlmostEqual(completed_ratio(1, 3), 1 / 3)

    def test_invalid_counts_are_rejected(self):
        for completed, total in [(-1, 2), (3, 2), (0, -1), (1, 0)]:
            with self.subTest(completed=completed, total=total):
                with self.assertRaises(ValueError):
                    completed_ratio(completed, total)


if __name__ == "__main__":
    unittest.main()
