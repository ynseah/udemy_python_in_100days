alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caesar(in_text, shift_amount, chosen_direction):
    out_text = ""
    for letter in in_text:
        position = alphabet.index(letter)
        if (chosen_direction == "encode"):
            new_position = position + shift_amount
        elif (chosen_direction == "decode"):
            new_position = position - shift_amount
        #else:
            #print (f"Invalid direction: {chosen_direction}. Please either enter encode or decode")
        out_text += alphabet[new_position]
    print (f"The {chosen_direction}d text is {out_text}")

## better code 
def caesar2 (in_text, shift_amount, chosen_direction):
    out_text = ""
    if (chosen_direction == "decode"):
        shift_amount *= -1

    for letter in in_text:
        position = alphabet.index(letter)        
        new_position = position + shift_amount
        out_text += alphabet[new_position]
    print (f"The {chosen_direction}d text is {out_text}")




caesar2 (in_text=text, shift_amount=shift, chosen_direction=direction)