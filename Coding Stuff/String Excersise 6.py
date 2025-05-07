#E Creamer
#5/1/2024
#Some words are special. What makes a word special you ask? Special words have exactly the same number of vowels 
# (a,e,i,o,u) and consonants (the other 21 letters in the alphabet). Ask the user to enter a word and output whether or not it is special.

#declaring counting variables
vowels = 0
consonants = 0
#input from user
user = input("Enter a word ").lower()
#looping through all characters in user
for i in range(len(user)):
    #checking to see if it is a vowel
    if user[i] == "a" or user[i] == "e" or user[i] == "i" or user[i] == "o" or user[i] == "u":
        #if so, add 1 to vowel counter
        vowels += 1
    else:
        #else add 1 to consonant counter
        consonants += 1
#comparing vowel and constant, if they are the same, then it is a special word
if vowels == consonants:
    print(user, "is a special word")
else:
    #if not, its not a special word
    print(user, "is not a special word")