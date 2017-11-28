class Guess:

    def __init__(self, secretword):
        self.secretWord = secretword
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = "_" * len(self.secretWord)

    def display(self):
        print("Current:" + self.currentStatus)
        print("Tries:%d"%self.numTries)
        print(self.guessedChars)

    def guess(self, character):
        self.numTries += 1
        self.guessedChars.append(character)
        if character in self.secretWord:
            for i in range(len(self.secretWord)):
                if character == self.secretWord[i]:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
                    self.numTries -= 1
                    self.guessedChars.remove(character)
                if self.secretWord == self.currentStatus:
                    print(self.secretWord)
                    return True



