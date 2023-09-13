from nltk.corpus import words


word_list = set(words.words())


def encrypt(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            encrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


def crack(encrypted_text):
    for shift in range(26):
        potential_plain_text = decrypt(encrypted_text, shift)
        word_count = sum(1 for word in potential_plain_text.split() if word.lower() in word_list)

        # If a significant number of valid English words are found, return the decrypted text
        if word_count > len(potential_plain_text.split()) / 2:
            return potential_plain_text
    return ""


if __name__ == "__main__":
    text = "Hello, World!"
    shifted_text = encrypt(text, 3)
    print(f"Original: {text}")
    print(f"Encrypted: {shifted_text}")
    print(f"Decrypted: {decrypt(shifted_text, 3)}")
