#E Creamer
#5/1/2024
#In the first line, print the third character of this string.
#In the second line, print the second to last character of this string.
#In the third line, print the first five characters of this string.
#In the fourth line, print all but the last two characters of this string.
#In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).
#n the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
#In the seventh line, print all the characters of the string in reverse order.
#In the eighth line, print every second character of the string in reverse order, starting from the last one.
#In the ninth line, print the length of the given string.

#input from user
user = input("Enter a string ")
length = len(user)

print(user[2])# In the first line, print the third character of this string.

print(user[length-2])# In the second line, print the second to last character of this string.

print(user[:5])# In the third line, print the first five characters of this string.

print(user[:length-2])# In the fourth line, print all but the last two characters of this string.

print(user[::2])# In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).

print(user[1::2])# In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

print(user[::-1])# In the seventh line, print all the characters of the string in reverse order.

print(user[::-2])# In the eighth line, print every second character of the string in reverse order, starting from the last one.

print(length)#In the ninth line, print the length of the given string.
