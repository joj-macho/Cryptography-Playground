# Atbash Cipher 

## Description

This Python program implements the Atbash cipher, a simple substitution cipher that replaces each letter with its mirror image in the alphabet.

## How it Works

- The program first defines the `CHARACTERS` constant, which consists of the lowercase English alphabet. These are the characters that can be encrypted and decrypted.

- The `main()` function starts by displaying a simple menu for the user to choose between encryption and decryption. Depending on the user choice, the `atbash_cipher()` function is invoked to perform the selected action.

- The `atbash_cipher(text)` function takes the text to be encrypted or decrypted (plaintext or ciphertext respectively, or simply `text`). This function applies the Atbash cipher algorithm to the `text` to return the `result_text`.

- The `atbash_cipher` function iterates through each character in the input text and applies the Atbash Cipher Algorithm accordingly. If the character is in the set of characters (`CHARACTERS`), it finds the index of that character in `CHARACTERS` and then applies the Atbash transformation which involves replacing a letter with its mirror image in the alphabet that is, a simple substitution where 'a' becomes 'z', 'b' becomes 'y', and so on. The replaced character is then added to the result text. If the character is not in `CHARACTERS` (e.g., whitespace or special characters), it remains unchanged. Finally, the function returns the resulting encrypted or decrypted text.

- Similar to the ROT13 cipher, the Atbash cipher is its own inverse. This can be observed when decrypting using the program. Decryption using the Atbash cipher is the same as encryption since the mirror image of a letter is the same in both directions. Applying the Atbash cipher twice on the same message retrieves the original message. This is shown in the program output below.


## Program Input & Output

When you run `atbash_cipher.py`, the output will look like this:

```

Welcome to Atbash Cipher.

Atbash Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1
Enter the plaintext to encrypt:
> hello world!

Encrypted message:
svool dliow!

Atbash Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 1
Enter the plaintext to encrypt:
> svool dliow!

Encrypted message:
hello world!

Atbash Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 2
Enter the ciphertext to decrypt:
> svool dliow!

Decrypted message:
hello world!

Atbash Cipher Menu:
1. Encrypt
2. Decrypt
3. Quit
Enter your choice: 3
Bye!
```
