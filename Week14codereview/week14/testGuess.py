import unittest

from guess import Guess
from hangman import Hangman
from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('access')   # word that has same letters
        self.h1 = Hangman()
        self.w1 = Word('words.txt')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('k')  # letter not in 'default'
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('a')  # already guessed letter (not processed in main)
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

        self.assertEqual(self.g2.displayCurrent(), '_ _ _ e _ _ ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ e _ _ ')
        self.g2.guess('s')
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ e s s ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('k')  # letter not in 'default'
        self.assertEqual(self.g1.displayGuessed(), ' a e k n t u ')
        self.g1.guess('a')  # already guessed letter (not processed in main)
        self.assertEqual(self.g1.displayGuessed(), ' a e k n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e k n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f k n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f k l n t u ')

        self.assertEqual(self.g2.displayGuessed(), ' e n ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayGuessed(), ' a e n ')
        self.g2.guess('s')
        self.assertEqual(self.g2.displayGuessed(), ' a e n s ')

    def testGuess(self):
        self.assertEqual(self.g1.guessedChars, {'e', 'n', ''})
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.guessedChars, {'a', 'e', 'n', ''})
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertTrue(self.g1.guess('f'))
        self.assertEqual(self.g1.guessedChars, {'a', 'e', 'f', 'n', ''})
        self.assertEqual(self.g1.currentStatus, '_efa___')
        self.assertFalse(self.g1.guess('k'))    # letter not in 'default'
        self.assertEqual(self.g1.guessedChars, {'a', 'e', 'f', 'k', 'n', ''})
        self.assertEqual(self.g1.currentStatus, '_efa___')

        self.assertEqual(self.g2.guessedChars, {'e', 'n', ''})
        self.assertEqual(self.g2.currentStatus, '___e__')
        self.assertTrue(self.g2.guess('a'))
        self.assertEqual(self.g2.guessedChars, {'a', 'e', 'n', ''})
        self.assertEqual(self.g2.currentStatus, 'a__e__')
        self.assertTrue(self.g2.guess('s'))
        self.assertEqual(self.g2.guessedChars, {'a', 'e', 'n', 's', ''})
        self.assertEqual(self.g2.currentStatus, 'a__ess')

    def testFinished(self):
        testList = ['d', 'e', 'f', 'a', 'u', 'l', 't']
        for letter in testList:
            self.g1.guess(letter)
        self.assertTrue(self.g1.finished())


    def testHangman(self):
        self.assertEqual(self.h1.remainingLives, 6)
        self.assertEqual(self.h1.currentShape(),
'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)
        self.assertEqual(self.h1.currentShape(),
'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')

    def testWord(self):
        self.assertEqual(self.w1.count, 19184)
        self.assertIn(self.w1.randFromDB(), self.w1.words)

if __name__ == '__main__':
    unittest.main()
