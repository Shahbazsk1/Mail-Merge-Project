PLACEHOLDER = "[name]"

with open("./Input/Names/invited_name.txt") as name:
    names = name.readlines()
    print(names)

with open("./Input/Letter/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
