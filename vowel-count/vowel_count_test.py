import unittest
from vowel_count import vowel_count

class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEquals(2, vowel_count("sajad"))
        self.assertEquals(1, vowel_count("python"))
        self.assertEquals(0, vowel_count("zzz"))


if __name__ == '__main__':
    unittest.main()