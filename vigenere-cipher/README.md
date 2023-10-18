# Vigenère cipher

## Description

This Python program implements the Vigenère Cipher. The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. A polyalphabetic cipher uses multiple substitution alphabets to encrypt the text, making it more secure than monoalphabetic ciphers.


## How it Works

- - The `main()` function starts by displaying a simple menu for the user to choose between encryption and decryption. Depending on the user choice, the `vigenere_cipher()` function is invoked to perform the selected action.

- The `vigenere_cipher(text, key, decrypt=False)` function performs the Vigenère encryption or decryption on the given text using the provided key. It iterates through each character in the text and applies the Vigenère table to find the ciphered or deciphered letters based on the key.

- The `generate_vigenere_table()` function generates the Vigenère table, which is a 26x26 grid of shifted alphabets. Each row of this table corresponds to a shifted alphabet, and the table is used for encryption and decryption in the Vigenère Cipher.

- The `expand_key(text, key)` function repeats the key to match the length of the text, ensuring that each character in the text has a corresponding key character for the Vigenère encryption or decryption.

## Program Input & Output

When you run the program `vigenere_cipher.py`, the output will look like this;

```
```