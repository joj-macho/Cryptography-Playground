import string

CHARACTERS = string.ascii_lowercase

def main():
    '''Main function to execute encryption/decryption using Atbash Cipher.'''

    print('\nWelcome to Atbash Cipher.\n')
    
    while True:
        print('Atbash Cipher Menu:')
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            plaintext = input('Enter the plaintext to encrypt:\n> ').lower()
            encrypted_message = atbash_cipher(plaintext)
            print(f'\nEncrypted message:\n{encrypted_message}\n')

        elif choice == '2':
            ciphertext = input('Enter the ciphertext to decrypt:\n> ').lower()
            decrypted_message = atbash_cipher(ciphertext)
            print(f'\nDecrypted message:\n{decrypted_message}\n')

        elif choice == '3':
            print('Bye!')
            break

        else:
            print('\nInvalid choice. Please try again.\n')


def atbash_cipher(text):
    '''Encrypt/Decrypt text using the Atbash cipher.'''
    # Initialize string for storing encrypted/decrypted result
    result_text = ''

    # Iterate through each character in text
    for char in text:
        if char in CHARACTERS:
            char_index = CHARACTERS.find(char)

            # Replacing a letter with its mirror image in the alphabet
            char_index = 25 - char_index
            result_text += CHARACTERS[char_index]
        else:
            result_text += char

    return result_text


if __name__ == '__main__':
    main()
