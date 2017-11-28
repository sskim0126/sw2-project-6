class Guess:

    def __init__(self, word):
        self.secretWord = word  #비밀로 선택된 단어를 인자로 받아 그것을 기록
        self.guessedChars = []  #추측에 이용된 글자들을 담을 빈 리스트 생성
        self.numTries = 0  #실패한 추측의 횟수의 변수를 0으로 초기화
        self.currentStatus = '_' * len(self.secretWord)  #secretWord의 현재 상태


    def display(self):
        print("Current: ", self.currentStatus)  #currentStatus 출력
        print("Tries: ", self.numTries)  #numTries 출력


    def guess(self, character):
        if character in self.secretWord:  #secretWord에 입력받은 character가 있으면
            for i in range(len(self.secretWord)):  #secretWord의 길이만큼 반복
                if self.secretWord[i] == character:  #secretWord의 i번째 값이 character의 값과 같으면
                    self.currentStatus = self.currentStatus[0:i] + character + self.currentStatus[i+1:]
                    #currentStatus의 i번째의 값에 character를 넣어줌
                    #self.currentStatus[i] = character -> typeError 문제점?

            if self.secretWord == self.currentStatus:  #위에서 갱신한 데이터가 모든 위치의 글자를 알아낸경우
                print(self.secretWord)
                return True  #True를 리턴
            else:  #그렇지 않으면
                return False  #False를 리턴
        else:  #secretWord에 입력받은 character가 없으면
            self.numTries += 1  #numTries에 1을 더해줌
            self.guessedChars += character  #guessedChars에 character를 더해줌
