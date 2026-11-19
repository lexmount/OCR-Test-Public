import unittest

from src.ocr54_ready import sample_coordinates


class CoordinateTests(unittest.TestCase):
    def test_sample_coordinates(self):
        self.assertEqual(sample_coordinates(), (2, 7))
