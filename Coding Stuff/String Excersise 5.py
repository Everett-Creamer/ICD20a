#E Creamer
#5/1/2024
#Ask the user to enter their favourite animal. Print out the name of the animal, except double every character. 

#input from user
user = input("Enter your fav animal ")
blank = ""
for letter in user:
    blank += letter * 2
print(blank)