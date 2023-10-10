from tkinter import *

# Словарь соответствий символов азбуки Морзе
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '/': '-..-.', '@': '.--.-.',
    ' ': ' '
}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' '

    return cipher


def encrypt_message():
    plaintext = entry.get()
    encrypted_message = encrypt(plaintext)
    output_text.set(encrypted_message)


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


def decrypt_message():
    ciphertext = entry.get()
    decrypted_message = decrypt(ciphertext)
    output_text.set(decrypted_message)


root = Tk()
root.geometry('400x400')
root.title('Morse Code Converter')

label = Label(root, text='Enter your message:')
label.pack()

entry = Entry(root, font=('Arial', 14))
entry.pack()

encrypt_button = Button(root, text='Encrypt', command=encrypt_message)
encrypt_button.pack()

decrypt_button = Button(root, text='Decrypt', command=decrypt_message)
decrypt_button.pack()

output_text = StringVar()
output_label = Label(root, textvariable=output_text, wraplength=350, font=('Arial', 14))
output_label.pack()

root.mainloop()
