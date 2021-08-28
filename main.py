import random
print('Welcome to Number guessing game')


def guess(x):
    ran_number = random.randint(1, x)
    tries = 1
    guess = 0
    while guess != ran_number:
        tries += 1
        raw = input(f'guess a number between 1 and {x}: ')

        if raw.isdigit():
            guess = int(raw)
            if guess < ran_number:
                print('Try again you were too low')
            else:
                print('You were too high')
        else:
            print('Enter a valid Number')

    print(f'Congratulation you guessed it correct in {tries}th time')


while True:
    userNumber = input("Enter the highest number that you want to guess: ")
    if userNumber.isdigit():
        guess(int(userNumber))
    else:
        print('Enter a valid number')
        continue
