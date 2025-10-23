# Jonathan Sonnek
# October 22 2025
# Program #2: Word Separator


def word_separator(sentence):

    result = ""
    #    Add your logic here
    result += sentence[0]
    for i in range(1, len(sentence)):
        char = sentence[i]
        if char.isupper():
            char = char.lower()
            result += " "
        result += char
    return result.strip()

# Get User input
user_input = input("Enter a sentence: ")

# Call Function and print
new_sentence = word_separator(user_input)
print(new_sentence)