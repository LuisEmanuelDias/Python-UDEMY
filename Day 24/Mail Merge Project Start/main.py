# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# import re

file1 = open("./Input/Letters/starting_letter.txt")
file2 = open("./Input/Names/invited_names.txt")

letter = file1.read()
names = file2.read()

names = names.splitlines()
letter = letter.splitlines()

for x in names:
    with open(f".\Output\ReadyToSend\letters_for_{x}.txt", "w") as f:
        text = letter[0].replace("[name]", x)
        for m in range(1, len(letter)):
            text += letter[m]
        f.write(text)

file1.close()
file2.close()
