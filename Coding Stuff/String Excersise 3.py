#E Creamer
#5/1/2024
#Ask the user to enter a word. Cut it into two "equal" parts. If the length of the word is odd,
# place the center character in the first half, so that the first half contains one more character
# than the second. Now print a new word with the first and second halves interchanged (second half first and the first half second)

#input from user
user = input("Enter a word ")
#getting length of input
length = len(user)
#the first half is index 0 to half of the word, and if the word is odd you add 1,
first_half = user[:length // 2 + length % 2]
#the second half of the word starts at index of half the word, and if its odd adding 1, and ends at the end of string
second_half = user[length // 2 + length % 2:]
#printing the second half then first half
print(second_half + first_half)