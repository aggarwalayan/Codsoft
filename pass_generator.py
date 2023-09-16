import random
import string
import tkinter as tk

def generate_password(min_length, min_uppercase, min_digits, min_special):
    if min_length < min_uppercase + min_digits + min_special:
        return "Minimum length is too short to meet minimum requirements."

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    num_uppercase = 0
    num_digits = 0
    num_special = 0

    password = []

    for _ in range(min_uppercase):
        password.append(random.choice(uppercase_chars))
        num_uppercase += 1

    for _ in range(min_digits):
        password.append(random.choice(digit_chars))
        num_digits += 1

    for _ in range(min_special):
        password.append(random.choice(special_chars))
        num_special += 1

    # fill the remaining length with random chars
    remaining_length = min_length - (min_uppercase + min_digits + min_special)
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password) #shuffles to randomize relative positions

    return ''.join(password)

def generate_password_button_click():
    min_length = int(min_length_entry.get())
    min_uppercase = int(min_uppercase_entry.get())
    min_digits = int(min_digits_entry.get())
    min_special = int(min_special_entry.get())

    password = generate_password(min_length, min_uppercase, min_digits, min_special)
    password_label.config(text=f"Generated Password: {password}")

window = tk.Tk()
window.title("Password Generator")

# labels
min_length_label = tk.Label(window, text="Minimum Length:")
min_uppercase_label = tk.Label(window, text="Minimum Uppercase Letters:")
min_digits_label = tk.Label(window, text="Minimum Digits:")
min_special_label = tk.Label(window, text="Minimum Special Characters:")

min_length_entry = tk.Entry(window)
min_uppercase_entry = tk.Entry(window)
min_digits_entry = tk.Entry(window)
min_special_entry = tk.Entry(window)

generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_click)
password_label = tk.Label(window, text="Generated Password: ")

# widgets layour
min_length_label.grid(row=0, column=0, padx=10, pady=5)
min_length_entry.grid(row=0, column=1, padx=10, pady=5)
min_uppercase_label.grid(row=1, column=0, padx=10, pady=5)
min_uppercase_entry.grid(row=1, column=1, padx=10, pady=5)
min_digits_label.grid(row=2, column=0, padx=10, pady=5)
min_digits_entry.grid(row=2, column=1, padx=10, pady=5)
min_special_label.grid(row=3, column=0, padx=10, pady=5)
min_special_entry.grid(row=3, column=1, padx=10, pady=5)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
password_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# start tkinter window
window.mainloop()
