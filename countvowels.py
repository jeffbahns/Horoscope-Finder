# Count Vowels

vowels = ["a", "e", "i", "o", "u"]

def countVowels(input_text):
    total = 0
    for letter in input_text.lower():
        for vowel in vowels:
            if letter == vowel:
                total += 1
    return total

