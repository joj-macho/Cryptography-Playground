# Caesar Cipher 

## Description

This Python program implements the Caesar Cipher, a simple encryption technique where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. This program provides options for encrypting and decrypting messages using the Caesar Cipher.


## How it Works

- The program first defines the `CHARACTERS` constant, which represents the set of characters that the program can encrypt and decrypt. It includes lowercase letters, digits, and a set of common symbols. This constant acts as a reference for valid characters that the cipher can operate on.

- The `main()` function starts by displaying a simple menu for the user to choose between encryption and decryption. Depending on the user choice, the `caesar_cipher()` function is invoked to perform the selected action.

- The `caesar_cipher(text, shift, mode)` function takes the text to be encrypted or decrypted (plaintext or ciphertext respectively, or simply `text`), the shift value (`shift`), and the mode of operation (`mode`), which can be either 'encrypt' or 'decrypt'. This function applies the Caesar cipher algorithm to the `text` to return the `result_text`.

- The `caesar_cipher` function iterates through each character in the input text and applies the Caesar Cipher algorithm accordingly. If the character is a letter or other valid character (i.e. in `CHARACTERS`), it shifts the character by the specified amount (`shift`) either forward (for encryption) or backward (for decryption) in the alphabet. The shifted character is then added to the result text. If the character is not a letter or a valid character (i.e. not in `CHARACTERS`), it remains unchanged in the result text. Finally, the function returns the resulting encrypted or decrypted text.


## Program Input & Output

When you run `caesar_cipher.py`, the output will look like this:

```

Welcome to Caesar Cipher.

Choose an option:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1

Enter the text to encrypt:
> hello world!
Enter the shift value: 12

Encrypted message:
tqxx1*914xp(

Choose an option:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 2

Enter the text to decrypt:
> tqxx1*914xp(
Enter the shift value: 12

Decrypted message:
hello world!

Choose an option:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1

Enter the text to encrypt:
> This program can also encrypt numbers and symbols like 12345 and +-*/~.
Enter the shift value: 20

Encrypted message:
.23?]0!91!u7]wu8]u6?9]y8w!$0.]8`7vy!?]u8x]?$7v96?]635y]^&*()]u8x]ghct:|

Choose an option:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 2

Enter the text to decrypt:
> .23?]0!91!u7]wu8]u6?9]y8w!$0.]8`7vy!?]u8x]?$7v96?]635y]^&*()]u8x]ghct:|
Enter the shift value: 20

Decrypted message:
this program can also encrypt numbers and symbols like 12345 and +-*/~.

Choose an option:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 3

Bye!
```
