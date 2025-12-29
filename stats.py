def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_count = {}
    split_text = text.split()
    for word in split_text:
        for letter in word:
            letter = letter.lower()
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count
