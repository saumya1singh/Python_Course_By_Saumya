import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
           "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-", "_"]

print("Welcome to Password Generator!!!")
num_letters = int(input("Enter how many letters would you like in your password? "))
num_numbers = int(input("Enter how many numbers would you like in your password? "))
num_symbols = int(input("Enter how many symbol would you like in your password? "))

random_letters = random.sample(letters, k=num_letters)
random_numbers = random.sample(numbers, k=num_numbers)
random_symbols = random.sample(symbols, k=num_symbols)

password_list = random_letters + random_numbers + random_symbols
print(password_list)
random.shuffle(password_list)
random_password = ''.join(password_list)
print(f"your password is: {random_password}")