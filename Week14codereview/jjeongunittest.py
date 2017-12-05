import unittest
import guess

class guessTest(unittest.TestCase):
    def setUp(self):
        self.g1 = guess("beauty")

    def tearDown(self):
        pass

    def test_displayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_e____')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ea___')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ea_t_')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_eaut_')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayCurrent(), 'beaut_')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayCurrent(), 'beauty')

    def test_displayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(),'e')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'e a')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), 'e a t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), 'e a t u')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayGuessed(), 'e a t u b')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayGuessed(), 'e a t u b y')

    def test_guess(self, beauty):
        self.g1 = guess("beauty")
        self.assertEqual(self.g1, 'beauty')

if __name__ == '__main__':
    unittest.main()
