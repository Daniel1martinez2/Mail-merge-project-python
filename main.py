#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()
    print(names_list)
    new_names_list = []
    names = [name.replace("\n", "") for name in names_list]

    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        for name in names:
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as user_letter:
                user_letter.write(letter_content.replace("[name]", name))
        print("done")


