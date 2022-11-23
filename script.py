letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
    unique_chars = str()
    for letter in word:
        if unique_chars.count(letter) == 0:
            unique_chars += letter

    return len(unique_chars)


print("mississippi", unique_english_letters("mississippi"))
# should print 4
print("Apple", unique_english_letters("Apple"))
# should print 4
