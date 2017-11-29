from hangman import Hangman
from word import Word


class Guess:
    def __init__(self, word):  # 사용한 글자, 실패한 횟수, 현재 상태 데이터 초기화
        self.guessedChars = []  # 사용한 글자의 데이터타입.
        self.numTries = 0  # 실패한 횟수.
        self.secretWord = word  # 비밀로 선택된 단어 기록
        self.currentStatus = '_' * len(self.secretWord)  # 맞춘 단어 기록

    def display(self):  # 지금까지 알아낸 글자,그위치를 가리키는 데이터(hangman그림),실패한 추측의회수를 화면에 출력
        print("Current: ", self.currentStatus)
        print("Tries: ", self.numTries)  # 실패한 추측의 횟수.
        print("already used: ", self.guessedChars)

    def guess(self, character):  # numTries는 +되야할 기능 추가!
        for i, x in enumerate(self.secretWord):  # 자료형을 입력으로받아 인덱스,값을 포함해 리턴.
            if character == x:  # x는 secreWord의 글자.
               self.currentStatus = self.currentStatus[:i] + x + self.currentStatus[i+1:]
        self.guessedChars += character
        if character not in self.secretWord:
            self.numTries += 1  # 실패한 회수 증가.
            #self.guessedChars += character  # 사용한 글자의 집합에 원소로 추가.
        if self.currentStatus == self.secretWord:
            print(self.secretWord)
            return True
        else:
            return False

      


