class Guess:

    def __init__(self, word):
        self.letters = [word[i] for i in range(len(word))]
        self.currentStatus = ['_' for i in range(len(self.letters))]
        self.guessedChars = []
        self.numTries = 0
        self.secretWord = word

    def display(self):
        print('Current: ', end="")
        for letter in self.currentStatus:
            print(letter[0], end=" ")
        print()
        print('Tries: ', self.numTries)


    def guess(self, character):
        self.guessedChars.append(character)

        if not character in self.letters:
            self.numTries += 1
        else:
            for i in range(len(self.letters)):
                if character == self.letters[i]:
                    self.currentStatus[i] = character

        if '_' in self.currentStatus:
            return False
        else:
            return True
