import string

def main():
    '''Main function to execute encryption/decryption using Vigenère Cipher.'''

    print('\nWelcome to Vigenère Cipher.\n')
    
    while True:
        print('Vigenère Cipher Menu:')
        print('1. Encrypt')
        print('2. Decrypt')
        print('3. Quit')

        choice = input('Enter your choice: ')
        print()

        if choice == '1':
            plaintext = input('Enter the plaintext to encrypt:\n> ').lower()
            key = input('Enter the key: ').lower()
            encrypted_message = vigenere_cipher(plaintext, key)
            print(f'\nEncrypted message: {encrypted_message}\n')

        elif choice == '2':
            ciphertext = input('Enter the ciphertext to decrypt:\n> ').lower()
            key = input('Enter the key: ').lower()
            decrypted_message = vigenere_cipher(ciphertext, key, decrypt=True)
            print(f'\nDecrypted message: {decrypted_message}\n')

        elif choice == '3':
            print('Bye!')
            break

        else:
            print('\nInvalid choice. Please try again.\n')


def vigenere_cipher(text, key, decrypt=False):
    '''Encrypt/Decrypt text using the Vigenère cipher.'''
    
    # Generate the Vigenère table
    vigenere_table = generate_vigenere_table()

    # Ensure the key is repeated to match the length of the text
    expanded_key = expand_key(text, key)

    # Initialize string for storing encrypted/decrypted result
    result_text = ''

    # Iterate through each character in the text
    for i in range(len(text)):
        # Check if the character is a lowercase letter
        if text[i] in string.ascii_lowercase:
            # Get the row and column indices for the Vigenère table
            row = string.ascii_lowercase.index(expanded_key[i])
            col = string.ascii_lowercase.index(text[i])
            # Encrypt or decrypt based on the mode
            if decrypt:
                # Decrypt: use Vigenère table to find the original letter
                result_text += vigenere_table[row].index(col)
            else:
                # Encrypt: use Vigenère table to find the ciphered letter
                result_text += vigenere_table[row][col]
        else:
            # Handle characters that are not lowercase letters
            result_text += text[i]

    return result_text


def generate_vigenere_table():
    '''Generate the Vigenère table.'''
    
    vigenere_table = []

    # Iterate through the 26 letters of the alphabet
    for i in range(26):
        # Shift the alphabet based on the position
        shifted_alphabet = string.ascii_lowercase[i:] + string.ascii_lowercase[:i]
        vigenere_table.append(shifted_alphabet)

    return vigenere_table


def expand_key(text, key):
    '''Repeat the key to match the length of the text.'''
    
    expanded_key = ''
    key_index = 0

    # Iterate through each character in the text
    for i in range(len(text)):
        # Check if the character is a lowercase letter
        if text[i] in string.ascii_lowercase:
            # Append the corresponding character from the key
            expanded_key += key[key_index]
            # Update the key index and handle wrapping
            key_index = (key_index + 1) % len(key)
        else:
            # Handle characters that are not lowercase letters
            expanded_key += text[i]

    return expanded_key


if __name__ == '__main__':
    main()


# TODO: Fix the error when decrypting