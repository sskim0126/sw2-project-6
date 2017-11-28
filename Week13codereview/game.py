from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        englishword = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                       'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue #입력값이 1이 아니면 다시 반복문.
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue #이미 사용된 글자가 들어오면 다시 반복문
        if guessedChar not in englishword:
            print('You only input english!')
            continue #영어 이외의 것이 들어오면 다시 반복문.
        finished = guess.guess(guessedChar)
        if finished == True:
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')

if __name__ == '__main__':
    gameMain()