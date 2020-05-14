import random

def get_choice():
    guess = input("Guess a letter: ")
    guess = str.upper(guess)

    if len(guess) == 1:
        return guess
    else:
        print("Please select a usable choice!")
        get_choice()

def main():

    guesses = []
    incorrect = []

    f = open("capitals.txt", "r")
    if f.mode == "r":
        contents = f.readlines()
        #print(list(contents))

    original = random.choice(contents)
    original = original.strip('\n')
    #print(original)

    check = list(original)
    original = list(original)
    for x in range(len(original)):
        if original[x] == ' ':
            original[x] = ' '
        elif original[x] == ',':
            original[x] = ','
        else:
            original[x] = '_'

    censored = original
    print("".join(censored))

    Try = 6

    while Try >= 1:
        if list(check) == list(original):
            print("You Win!!")
            break

        guess = get_choice()

        if guess in guesses:
            print("You have already put this letter!")
            print(guesses)

        else:
            if guess in check:
                guesses.append(guess)
                for y in range(len(original)):
                    if guess == check[y]:
                        original[y] = guess
                        censored = "".join(censored)
                print("".join(original))
            else:
                if guess in incorrect:
                    print("You have already guessed that!")
                    print("Previous incorrect answers: ", incorrect)
                    print("All guesses: ", guesses)
                else:
                    print("%s is not in the string!" % (guess))
                    Try -= 1
                    print("Tries left: %d" % Try)
                    incorrect.append(guess)
    print("Game Over!")
    print("The correct answer was: " + "".join(check))

main()