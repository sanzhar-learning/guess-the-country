import tkinter as tk
from tkinter import messagebox
import quiz_game  

def start_new_game():
    global game_state
    game_state = quiz_game.start_game(countries)
    update_display(game_state)
    update_lives(game_state)
    guess_entry.config(state="normal")
    guess_button.config(state="normal")

def update_display(game_state):
    display_label.config(text=" ".join(game_state["display"]))

def update_lives(game_state):
    lives_label.config(text="❤️" * (game_state["max_attempts"] - game_state["attempts"]))


def guess_letter():
    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)
    result = quiz_game.check_guess(game_state, guess)
    if result == "invalid":
        messagebox.showwarning("Invalid", "Please enter a single letter.")
        return
    elif result == "already":
        messagebox.showinfo("Already guessed", f"You already guessed '{guess}'.")
    elif result == "correct":
        pass
    elif result == "wrong":
        pass
    
    update_display(game_state)
    update_lives(game_state)
    check_game_end(game_state)

def update_guessed_letters(game_state):
    guessed_text = ", ".join(game_state["guessed_letters"])
    guessed_label.config(text=f"Guessed letters: {guessed_text}")

def guess_letter():
    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)
    result = quiz_game.check_guess(game_state, guess)
    update_display(game_state)        
    update_lives(game_state)        
    update_guessed_letters(game_state)
    check_game_end(game_state)


def check_game_end(game_state):
    state = quiz_game.game_over(game_state)
    
    if state == "won":
        messagebox.showinfo(
            "You Won!",
            f"🎉 SUUUIIIIIIIII! The country was {game_state['chosen_country'].title()}! You don't have skill issue!"
        )
        end_game()
    elif state == "lost":
        messagebox.showinfo(
            "Game Over",
            f"💀💀💀 Dumbass! Attempts are over! The country was {game_state['chosen_country'].title()}. Never come back again!"
        )
        end_game()

def end_game():
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

root = tk.Tk()
root.title("Guess the Country")
root.geometry("600x400")
root.config(bg="#151616")

guessed_label = tk.Label(root, text="Guessed letters: ", font=("Arial", 12), bg="#3E4747")
guessed_label.pack(pady=5)

display_label = tk.Label(root, text="", font=("Arial", 24), bg="#4f5555")
display_label.pack(pady=20)

lives_label = tk.Label(root, text="", font=("Arial", 16), bg="#0f1414")
lives_label.pack()


guess_entry = tk.Entry(root, font=("Arial", 16), width=5)
guess_entry.pack(pady=10)
guess_button = tk.Button(root, text="Guess Letter", font=("Arial", 14), command=guess_letter)
guess_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=start_new_game)
restart_button.pack(pady=10)

countries = quiz_game.load_countries()
game_state = None
root.mainloop()