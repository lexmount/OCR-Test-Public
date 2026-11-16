import unittest

from src.task_batches import task_batches


class TaskBatchTests(unittest.TestCase):
    def test_order_and_remainder(self):
        tasks = ["a", "b", "c", "d", "e"]
        self.assertEqual(task_batches(tasks, 2), [["a", "b"], ["c", "d"], ["e"]])
        self.assertEqual(tasks, ["a", "b", "c", "d", "e"])

    def test_empty_input(self):
        self.assertEqual(task_batches([], 3), [])

    def test_large_batch(self):
        self.assertEqual(task_batches(["a", "b"], 20), [["a", "b"]])

    def test_result_lists_are_independent(self):
        tasks = ["a", "b"]
        result = task_batches(tasks, 1)
        result[0].append("c")
        self.assertEqual(tasks, ["a", "b"])
        self.assertEqual(result[1], ["b"])

    def test_nonpositive_size(self):
        for value in (0, -1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                task_batches(["a"], value)

    def test_noninteger_size(self):
        for value in (True, 1.5, "2", None):
            with self.subTest(value=value), self.assertRaises(TypeError):
                task_batches(["a"], value)


if __name__ == "__main__":
    unittest.main()
