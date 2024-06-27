# Caesar Cipher.

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(message, encode, shift):

    if encode == 'decode':
        shift *= -1

    result = ''
    for letter in message:
        new_index = alphabet.index(letter) + shift
        result += alphabet[new_index % 26]

    return result


print(logo)
encrypt = input("Type 'encode' to encrypt; type 'decode' to decrypt")
message = input("Type your message:\n>> ")
shift = int(input("Type the shift number:\n>>"))

new_message = caeser(message, encrypt, shift)
print(f"Your new message is : {new_message}")