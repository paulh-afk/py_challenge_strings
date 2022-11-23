# 1 - Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# exercise | + fast for little word
def unique_english_letters(word):
    unique_chars = str()
    for letter in word:
        if unique_chars.count(letter) == 0:
            unique_chars += letter

    return len(unique_chars)


# solution | + scalability
def unique_english_letters_solution(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1

    return uniques


print("mississippi", unique_english_letters_solution("mississippi"))
# should print 4
print("Apple", unique_english_letters_solution("Apple"))
# should print 4

# 2 - Count X


# exercise / same solution algorithm
def count_char_x(word, x):
    # return word.count(x)
    count = 0
    for letter in word:
        if letter == x:
            count += 1

    return count


print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
