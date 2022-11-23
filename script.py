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

# 3 - Count Multi X

# exercise / same solution algorithm
def count_multi_char_x(word, x):
    # return word.count(x)
    return len(word.split(x)) - 1


print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

print('assaa'.index('s'))

# 4 - Substring Between

# exercise / same solution algorithm
def substring_between_letters(word, start, end):
    start_index = word.find(start)
    end_index = word.find(end)

    if start_index > -1 and end_index > -1:
        return word[start_index + 1:end_index]

    return word


print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5 - X Length

# exercise / same solution algorithm
def x_length_words(sentence, x):
    for word in sentence.split(' '):
        if len(word) < x:
            return False
    return True


print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
