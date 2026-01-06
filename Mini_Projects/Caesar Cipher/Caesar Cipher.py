# import string
# alphabet = list(string.ascii_lowercase)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == 'decode':
                shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result:{output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))

    caesar_cipher(text, shift, direction)
    restart = input("type 'yes' if you want to go again otherwise type 'no':\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")