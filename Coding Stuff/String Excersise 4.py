#E Creamer
#5/1/2024
#Ask the user to enter two words separated by a space. Print the words out in reverse order. 

#input from user
user = input("Enter a two words with a space ")
#finding the space/the two words
space = user.find(" ")
#the character on the first half is the first word
first_word = user[:space]
#the characters on the second half is the second word
second_word = user[space:]
#printing the second word than the first word
print(second_word, first_word)