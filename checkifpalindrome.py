# Check if Palindrome

# Takes phrase/word, returns True if palindrome

import re

def check_if_palindrome(phrase):
    phrase = phrase.lower()
    stripped_phrase = re.sub("[^a-z]", "", phrase)
    reverse = stripped_phrase[::-1]
    return reverse == phrase

