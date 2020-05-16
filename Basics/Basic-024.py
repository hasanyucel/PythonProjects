# Write a Python program to test whether a passed letter is a vowel or not.

def vowel_or_not(str):
    if(str.upper() in ["A", "E", "I", "O", "U"]):
        return "Vowel Letter"
    else:
        return "Not Vowel Letter"

print(vowel_or_not("A"))