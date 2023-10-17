# Set of characters that can be encrypted and decrypted
CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'

def main():
    '''Main function to execute encryption/decryption using ROT13 Cipher.'''

    print('\nWelcome to ROT13 Cipher.\n')
    
    while True:
        print('ROT13 Cipher Menu:')
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Quit')

        # Get user choice for encryption or decryption
        choice = input('Enter your choice: ')
        print()

        if choice == '1':
            plaintext = input('Enter the plaintext to encrypt:\n> ').lower()
            encrypted_message = rot13_cipher(plaintext)
            print(f'\nEncrypted message:\n{encrypted_message}\n')

        elif choice == '2':
            ciphertext = input('Enter the ciphertext to decrypt:\n> ').lower()
            decrypted_message = rot13_cipher(ciphertext)
            print(f'\nDecrypted message:\n{decrypted_message}\n')

        elif choice == '3':
            print('Bye!')
            break

        else:
            print('\nInvalid choice. Please try again.\n')


def rot13_cipher(text):
    '''Encrypt/Decrypt text using the ROT13 cipher.'''
    # Initialize string for storing encrypted/decrypted result
    result_text = ''

    # Iterate through each character in text
    for char in text:
        if char in CHARACTERS:
            char_index = CHARACTERS.find(char)

            # Apply the 13-shift and handle wrapping around to the beginning if necessary
            char_index = (char_index + 13) % 26
            result_text += CHARACTERS[char_index]
        else:
            result_text += char

    return result_text


if __name__ == '__main__':
    main()
