import random
import datetime

def guess_country():
    user_name = input("Enter your name: ").strip()
    print("Let's start the game.")
    print()

    countries = []
    file = open("countries.txt", "r")
    for line in file:
        clean_line = line.strip()
        if clean_line != "":
            countries.append(clean_line.lower())
    file.close()

    index = random.randint(0, len(countries) - 1)
    chosen_country = countries[index]

    guessed_letters = []  
    display = []

    for i in chosen_country:
     display.append("_")

    print(f"The country has {len(chosen_country)} letters.")
    print(" ".join(display))
    print()

    attempts = 0
    max_attempts = 10
    won = False

    while attempts < max_attempts:
        guess = input(f"Enter a letter ({attempts}/{max_attempts} attempts used): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_country:
            print(f"Good! The letter '{guess}' is in the country.")
            for i, letter in enumerate(chosen_country):
                if letter == guess:
                    display[i] = guess
        else:
            print(f"Wrong! The letter '{guess}' is not in the country, idiot!")
            attempts += 1

        print("Current word:", " ".join(display))
        print()

        if "_" not in display:
            print(f"🎉 SUUUIIIIIIIII! The country was {chosen_country.title()}! You don't have skill issue!")
            won = True
            break

 
    if not won:
        print(f"💀💀💀 Dumbass! Attempts are over! The country was {chosen_country.title()}. Never come back again!")

    with open("game_log.txt", "a") as log_file:
        log_file.write(f"Time: {datetime.datetime.now()}\n")
        log_file.write(f"User: {user_name}\n")
        log_file.write(f"Word: {chosen_country}\n")
        log_file.write(f"Attempts: {attempts}\n")
        if won:
            log_file.write(f"Result: {'Won'}\n")
        else:
            log_file.write(f"Result: {'Lost'}\n")
        log_file.write("-" * 50 + "\n")

guess_country()