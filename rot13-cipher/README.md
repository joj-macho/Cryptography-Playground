# ROT13 Cipher 

## Description

This Python program implements the ROT13 cipher, a simple letter substitution encryption technique. ROT13 replaces each letter in the alphabet with the letter 13 positions ahead (or behind) in the alphabet. It is a special case of the Caesar cipher, where the shift is always 13.

## How it Works

- The program first defines the `CHARACTERS` constant, which consists of the lowercase English alphabet. These are the characters that can be encrypted and decrypted.

- The `main()` function starts by displaying a simple menu for the user to choose between encryption and decryption. Depending on the user choice, the `rot13_cipher()` function is invoked to perform the selected action.

- The `rot13_cipher(text)` function takes the text to be encrypted or decrypted (plaintext or ciphertext respectively, or simply `text`). This function applies the ROT13 cipher algorithm to the `text` to return the `result_text`.

- The `rot13_cipher` function iterates through each character in the input text and applies the ROT13 Cipher Algorithm accordingly. If the character is in the set of characters (`CHARACTERS`), it finds the index of that character in `CHARACTERS` and then applies the ROT13 shift by adding 13 to the index and taking the remainder when divided by 26 (the number of characters in the alphabet). The shifted character is then added to the result text. If the character is not in `CHARACTERS` (e.g., whitespace or special characters), it remains unchanged. Finally, the function returns the resulting encrypted or decrypted text.

- Note that ROT13 is its own inverse, that is, applying ROT13 twice to any text will result in the original text. For encryption and decryption in this program, the same function `rot13_cipher` is used. This property is leveraged to handle both encryption and decryption in the program by using the same function for both operations. This is shown in the program output below.


## Program Input & Output

When you run `rot13_cipher.py`, the output will look like this:

```

Welcome to ROT13 Cipher.

ROT13 Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1

Enter the plaintext to encrypt:
> Hello World!

Encrypted message:
uryyb jbeyq!

ROT13 Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1

Enter the plaintext to encrypt:
> uryyb jbeyq!

Encrypted message:
hello world!

ROT13 Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 2

Enter the ciphertext to decrypt:
> uryyb jbeyq!

Decrypted message:
hello world!

ROT13 Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 3

Bye!
```
