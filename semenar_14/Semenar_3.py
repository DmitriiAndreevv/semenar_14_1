import unittest
from Semenar_1 import clean_text


class TestCleanText(unittest.TestCase):
    def test_1(self):
        self.assertEqual(clean_text('python'), 'python', msg='Something is not OK')

    def test_2(self):
        self.assertEqual(clean_text('Python'), 'python', msg='Something is not OK')

    def test_3(self):
        self.assertEqual(clean_text('python, but not java'), 'python but not java', msg='Something is not OK')

    def test_4(self):
        self.assertEqual(clean_text('python - это не питон'), 'python    ', msg='Something is not OK')

    def test_5(self):
        self.assertEqual(clean_text('"Python" - это не "Питон"'), 'python    ', msg='Something is not OK')


if __name__ == '__main__':
    unittest.main(verbosity=2)
