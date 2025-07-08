import tkinter as tk
import random

mystery_num = random.randint(1, 100)
tries = 0

def handle_guess():
    global tries
    user_input = guess_box.get()

    if not user_input.isdigit():
        feedback_label.config(text="Please enter a valid number!")
        return

    guess = int(user_input)
    tries += 1

    if guess < mystery_num:
        feedback_label.config(text="Too low! Try again.")
    elif guess > mystery_num:
        feedback_label.config(text="Too high! Try again.")
    else:
        feedback_label.config(text=f"Correct! Took you {tries} tries.")

root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x200")

instruction = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
instruction.pack(pady=10)

guess_box = tk.Entry(root, font=("Arial", 12))
guess_box.pack()

submit_button = tk.Button(root, text="Submit Guess", command=handle_guess)
submit_button.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack()

root.mainloop()
