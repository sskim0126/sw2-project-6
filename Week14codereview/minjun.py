import unittest
from game import *
from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess(self.secretWord)

    def tearDown(self):
        pass

    def wordcorrect(self): #단어의 전체를 다 맞춘 경우 처리
        if self.currentStatus == self.secretWord:
            self.assertEqual(self.g1.finished(), True)
        else:
            self.assertEqual(self.g1.finished(), False)
    def testDisplayCurrent(self): #부분적으로 맞추어진 단어의 상태가 올바르게 유지되는가?

        i = 0
        while i < 7:
            self.assertEqual(self.g1.displayCurrent(),self.g1.currentStatus)
        # self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        # self.g1.guess('a')
        # self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        # self.g1.guess('t')
        # self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        # self.g1.guess('u')
        # self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self): #이용된 글자들의 집합을 나타내는 데이터 유지 경우 처리
        i = 0
        string = ' e n '
        while i < 7:
            self.assertEqual(self.g1.displayGuessed(), string)
            self.g1.guess('guessedChar')
            string += ' ' + 'guessedChar' + ' '
#         self.assertEqual(self.g1.displayGuessed(), ' e n ')
#         self.g1.guess('a')
#         self.assertEqual(self.g1.displayGuessed(), ' a e n ')
#         self.g1.guess('t')
#         self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
#         self.g1.guess('u')
#         self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
#

if __name__ == '__main__':
    unittest.main()