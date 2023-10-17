# Set of characters that can be encrypted and decrypted
CHARACTERS = 'abcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

def main():
    '''Main function to execute encryption/decryption using Caesar Cipher.'''

    print('\nWelcome to Caesar Cipher.\n')
    
    while True:
        print('Choose an option:')
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Quit')

        # Get user choice for encryption or decryption
        choice = input('Enter your choice: ')
        print()

        if choice == '1':
            mode = 'encrypt'
            plaintext = input('Enter the text to encrypt:\n> ').lower()
            try:
                shift = int(input('Enter the shift value: '))
                encrypted_message = caesar_cipher(plaintext, shift, mode)
                print(f'\nEncrypted message:\n{encrypted_message}\n')
            except ValueError:
                print('\nInvalid shift value. Please enter an integer.\n')

        elif choice == '2':
            mode = 'decrypt'
            ciphertext = input('Enter the text to decrypt:\n> ').lower()
            try:
                shift = int(input('Enter the shift value: '))
                decrypted_message = caesar_cipher(ciphertext, shift, mode)
                print(f'\nDecrypted message:\n{decrypted_message}\n')
            except ValueError:
                print('\nInvalid shift value. Please enter an integer.\n')

        elif choice == '3':
            print('Bye!')
            break

        else:
            print('Invalid choice. Please try again.\n')


def caesar_cipher(text, shift, mode):
    '''Encrypt/Decrypt text using the Caesar cipher.'''
    # Initialize string for storing encrypted/decrypted result
    result_text = ''

    # Iterate through each character in text
    for char in text:
        if char in CHARACTERS:
            # Get the index of the character in the CHARACTERS string
            char_index = CHARACTERS.find(char)
            
            # Apply the shift for encryption or decryption based on the mode and handle wrapping around to the beginning if necessary
            if mode == 'encrypt':
                char_index = (char_index + shift) % len(CHARACTERS)
            elif mode == 'decrypt':
                char_index = (char_index - shift) % len(CHARACTERS)

            result_text += CHARACTERS[char_index]

        else:
            # If the character is not in CHARACTERS, keep it unchanged
            result_text += char
            
    return result_text


if __name__ == '__main__':
    main()
