"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A
 passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""
from typing import Dict


def is_valid(input) -> bool:
    words = []

    for word in input.split():
        word_map = generate_word_map(word)

        for existing in words:
            # print("word: {word} | existing: {existing}".format(word=word, existing=existing))
            existing_word_map = generate_word_map(existing)
            if not compare_map(word_map, existing_word_map):
                return False

        words.append(word)

    return True

def generate_word_map(word: str) -> Dict[str, int]:
    word_map = {}
    for letter in word:
        if word_map.get(str(letter)) == None:
            word_map[str(letter)] = 0
        word_map[str(letter)] = word_map[str(letter)] + 1
    return word_map


def compare_map(a, b) -> bool:
    if len([k for k in a.keys() if a.get(k) != b.get(k)]) == 0\
            and len([k for k in b.keys() if a.get(k) != b.get(k)]) == 0:
        return False
    return True

with open('day_04/input') as file:
    lines = file.readlines()

valid_count = 0

for line in lines:
    test = is_valid(line)
    print(test, line)
    if test:
        valid_count = valid_count + 1

print("valid count: ", valid_count)

# print("valid:   ", is_valid("aa bb cc dd ee"))
# print("invalid: ", is_valid("aa bb cc dd aa"))
# print("valid:   ", is_valid("aa bb cc dd aaa"))

"""
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words 
that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any 
other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?

"""

print("valid: ", is_valid("abcde fghij"))
print("in valid: ", is_valid("abcde xyz ecdab"))
print("valid: ", is_valid("a ab abc abd abf abj"))
print("valid: ", is_valid("iiii oiii ooii oooi oooo"))
print("in valid: ", is_valid("oiii ioii iioi iiio"))
