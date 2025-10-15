import random
import gui_functions

def load_countries():
    global countries
    countries = []
    file_path = "data/countries.txt"
    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line != "":
                countries.append(clean_line.lower())
    return countries

def start_game(countries, max_attempts = 7):
    global attempts
    chosen_country = random.choice(countries)
    display = []
    for letter in chosen_country:
        if letter.isalpha():
            display.append("_")
        else:
            display.append(letter)
    guessed_letters = []
    attempts = 0
    return {
        "chosen_country": chosen_country,
        "display": display,
        "guessed_letters": guessed_letters,
        "attempts": attempts,
        "max_attempts": max_attempts
    }

def check_guess(game_state, guess):
    guess = guess.lower()

    if len(guess) != 1 or not guess.isalpha():
        return "invalid"

    if guess in game_state["guessed_letters"]:
        return "already"

    game_state["guessed_letters"].append(guess)

    correct_guess = False
    i = 0
    for letter in game_state["chosen_country"]:
        if letter == guess:
            game_state["display"][i] = guess
            correct_guess = True
        i += 1

    if not correct_guess:
        game_state["attempts"] += 1

    gui_functions.update_display(game_state)
    gui_functions.update_lives(game_state)
    gui_functions.check_game_end(game_state)
    return "correct" if correct_guess else "wrong"


def game_over(game_state):
    if "_" not in game_state["display"]:
        return "won"
    elif game_state["attempts"] >= game_state["max_attempts"]:
        return "lost"
    return None