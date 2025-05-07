#E Creamer
#5/5/2025
#String Function Demo
import random
#list of all possible winning guess
guess_list = ["Everett", "Colton", "math", "electricity", "gay", "leaves", "are", "terrible", "one", "second", "stranger", "danger", "persona", "summer"]
#finding length of the guess list
length = len(guess_list)
#picking the winning guess at a random index between 0 and the length, then making it uppercase
winning_guess = guess_list[random.randrange(0, length)].upper()
#creating an empty array that is the size of the winning answer
empty = ["_"] * len(winning_guess)
#while loop
while True:
    #printing the empty array
    print(empty)
    #getting user input, and making it uppercase
    user = input("What is your guess? ").upper()
    #a for loop that loops through all letters in the winning guess
    for i in range(len(winning_guess)):
        #if the users input matches
        if user == winning_guess[i]:
            #add it to the empty array at the same index
            empty[i] = winning_guess[i]
    #if there is no _ in the array, then you win and it breaks the for loop
    if not "_" in empty:
        print(empty, "\nYOU WIN")
        break