import sys
import random


def main():
    secret_code, attempts = check_stdin()
    guess(secret_code, attempts)
    

def check_stdin():
    """Check -c secret code and -t number of attempts in stdin"""
    if len(sys.argv) < 2:
        secret_code = int(generate_secret_code())
        attempts = 10
    elif sys.argv[1] == "-c" and len(sys.argv) == 3:
        secret_code = int(sys.argv[2])
        attempts = 10
    elif sys.argv[1] == "-t" and len(sys.argv) == 3:
        attempts = int(sys.argv[2])
        secret_code = int(generate_secret_code())
    else:
        secret_code = int(sys.argv[2])
        attempts = int(sys.argv[4])
    return secret_code, attempts


def guess(secret_code, attempts):
    print("Will you find the secret code?")
    round = 0
    while(attempts > 0):
        print(f"---\nRound {round}\n>", end="")
        try:
            guess_code = int(input())
            guess_code_len = check_guess_code(guess_code)
            if guess_code_len == 4:
                well_placed, misplaced = check_placement(secret_code, guess_code)
                if secret_code == guess_code:
                    print("Congratz! You did it!")
                    break
                print_pieces(well_placed, misplaced)
        except ValueError:
            print("Wrong Input!")

        if round == attempts and secret_code != guess_code:
            print("You lost! It's ok, mistakes happen. Try again.")
            break
        round += 1


def generate_secret_code():
    code_list = []
    i = 0
    while (i < 4):
        secret_code = random.randrange(0, 8)
        code_list.append(str(secret_code))
        i += 1
    secret_code = ''.join(code_list)
    return secret_code


def check_guess_code(guess_code):
    guess_code_len = len(str(guess_code))
    if guess_code_len < 4:
        print("Please enter a four digit number.")
    elif guess_code_len > 4:
        print("Please enter a four digit number.")
    return guess_code_len


def check_placement(secret_code, guess_code):
    secret_code = str(secret_code)
    guess_code = str(guess_code)
    well_placed = 0
    misplaced = 0
    for i in range(len(secret_code)):
        if secret_code[i] == guess_code[i]:
            well_placed += 1
        else:
            for j in range(len(guess_code)):
                if secret_code[i] == guess_code[j]:
                    misplaced += 1
    return well_placed, misplaced


def print_pieces(well_placed, misplaced):
    print(f"Well placed pieces: {well_placed}")
    print(f"Misplaced pieces: {misplaced}")


if __name__ == "__main__":
    main()
