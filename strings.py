# 1. What is a String?
# A string is a sequence of characters.
# name = "Ashish"
# Think of it like an array of characters:

#  A   s   h   i   s   h
#  0   1   2   3   4   5

# 2. Accessing Characters (Indexing)
# name = "Python"

# print(name[0])
# print(name[1])
# print(name[5])

# Output

# P
# y
# n

# Negative Indexing

# Python lets you access characters from the end.

# name = "Python"

# print(name[-1])
# print(name[-2])
# print(name[-3])

# Output

# n
# o
# h

# Visualize it:

#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

# 3. String Length
# name = "Ashish"

# print(len(name))

# Output

# 6


# 4. Traversing a String
# Method 1
# name = "Python"

# for ch in name:
#     print(ch, end="")

# Output

# P
# y
# t
# h
# o
# n

# Method 2 (Using Index)
# name = "Python"

# for i in range(len(name)):
#     print(i, name[i])

# Output

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n



# 5. Slicing 

# Syntax

# string[start:end:step]

# Remember:

# start → included
# end → excluded

# Example

# text = "Programming"

# print(text[0:4])

# Output

# Prog

# From Beginning
# print(text[:5])

# Output

# Progr
# Till End
# print(text[4:])

# Output

# ramming

# Entire String
# print(text[:])

# Output

# Programming
# Every Second Character
# print(text[::2])

# Output

# Pormig

#Reverse a String

# name = "Python"

# for i in range(len(name)-1, -1, -1):
#     print(name[i], end="")

#OR

# text = "Python"

# print(text[::-1])

# Output

# nohtyP

# text = "Python"

# rev = ""

# for ch in text:
#     rev = ch + rev

# print(rev)
# This is one of Python's most useful shortcuts.

# 6. Strings are Immutable

# ❌ This will give an error:

# name = "Google"

# name[0] = "M"

# Strings cannot be changed directly.

# Correct way:

# name = "Google"

# name = "M" + name[1:]

# print(name)

# Output

# Moogle

# 7. Membership Operator
# text = "Programming"

# print("gram" in text)
# print("cat" in text)

# Output

# True
# False


# 8. String Concatenation
# first = "Hello"
# second = "World"

# print(first + " " + second)

# Output

# Hello World
# 9. String Repetition
# print("*" * 5)

# Output

# *****

# Useful for pattern problems.



# 10. Common String Methods ⭐⭐⭐
# upper()
# name = "python"

# print(name.upper())

# Output

# PYTHON
# lower()
# name = "PYTHON"

# print(name.lower())

# Output

# python
# capitalize()
# print("python".capitalize())

# Output

# Python
# title()
# print("hello world".title())

# Output

# Hello World
# strip()

# Removes spaces from both ends.

# text = "   Python   "

# print(text.strip())

# Output

# Python
# replace()
# text = "I love Java"

# print(text.replace("Java","Python"))

# Output

# I love Python
# count()
# text = "banana"

# print(text.count("a"))

# Output

# 3
# find()

# Returns the first index or -1.

# text = "Programming"

# print(text.find("g"))

# Output

# 3
# print(text.find("z"))

# Output

# -1
# startswith()
# text = "Google"

# print(text.startswith("Go"))

# Output

# True
# endswith()
# text = "resume.pdf"

# print(text.endswith(".pdf"))

# Output

# True
# 11. split() ⭐⭐⭐⭐⭐

# One of the most used methods.

# sentence = "Python is awesome"

# words = sentence.split()

# print(words)

# Output

# ['Python', 'is', 'awesome']

# Split using a delimiter

# date = "20-07-2026"

# print(date.split("-"))

# Output

# ['20', '07', '2026']
# 12. join()

# Opposite of split().

# words = ["I","Love","Python"]

# print(" ".join(words))

# Output

# I Love Python
# 13. enumerate()

# Very useful in DSA.

# word = "Python"

# for index, ch in enumerate(word):
#     print(index, ch)

# Output

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
# 14. Reverse Using Loop
# text = "Python"

# rev = ""

# for ch in text:
#     rev = ch + rev

# print(rev)

# Output

# nohtyP
# 15. Palindrome Check

# Method 1 (Pythonic)

# text = input()

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Method 2 (Two Pointers)

# text = input()

# left = 0
# right = len(text) - 1

# while left < right:
#     if text[left] != text[right]:
#         print("Not Palindrome")
#         break

#     left += 1
#     right -= 1
# else:
#     print("Palindrome")

# This introduces the two-pointer technique, which is common in interviews.

# 16. Count Vowels
# text = input()

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print(count)
# 17. Count Characters
# text = input()

# letters = 0

# for ch in text:
#     letters += 1

# print(letters)

# (Equivalent to len(text).)

# 18. Count Words
# sentence = input()

# words = sentence.split()

# print(len(words))
# 19. Remove Spaces
# text = input()

# print(text.replace(" ",""))
# 20. Frequency of Characters
# text = "banana"

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)

# Output

# {'b': 1, 'a': 3, 'n': 2}

# Later you'll learn to do this more easily with collections.Counter.

# ⭐ IDE Practice
# Easy
# Print the first and last character of a string.
# Print the length of a string.
# Reverse a string.
# Convert a string to uppercase.
# Count vowels.
# Count consonants.
# Remove spaces from a string.
# Replace "Python" with "Java" in a sentence.
# Check whether a string starts with "A".
# Check whether a filename ends with ".pdf".
# Medium
# Check if a string is a palindrome.
# Count words in a sentence.
# Count occurrences of each character.
# Print characters at even indices.
# Reverse each word in a sentence.
# Interview Level
# Check if two strings are anagrams.
# Find the first non-repeating character.
# Find the longest word in a sentence.
# Compress a string (aaabbc → a3b2c1).
# Reverse words without using split().
# 💡 Interview Tips

# Remember these methods:

# len()
# lower()
# upper()
# strip()
# replace()
# split()
# join()
# find()
# count()
# startswith()
# endswith()

# And these slicing patterns:

# text[:]
# text[::-1]
# text[1:]
# text[:-1]
# text[::2]

# Print the first and last character of a string.

# text= input()

# text = text.strip()  # Remove leading/trailing spaces

# if len(text) > 0:
#     print(text[0], text[-1])

#print the length of the string

# print(len(text))

#reverse a string

# text = text[::-1]
# print(text)

# text = text.upper()
# print(text)

#count vowels

# text = input()

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count +=1
# print(count)

#count consonents

# for ch in text.lower():
#     if ch.isalpha() and ch not in "aeiou":
#         count += 1
# print(count)

# Remove spaces from a string

# text = input()

# print(text.replace(" ",""))

# Replace Java with from a string

# text = "I love Java"

# print (text.replace("Java", "Python"))

# Check whether a string starts with "A".
# text = input()

# if text.startswith("A"):
#     print("Yes")
# else:
#     print("No")

# Check whether a filename ends with ".pdf".

# text = "python.pdf"

# if text.endswith(".pdf"):
#     print("yes")
# else:
#     print("no")

# Check if a string is a palindrome.

# name = input("Enter a string: ")

# if name == name[::-1]:
#     print(f"{name} is a palindrome.")
# else:
#     print(f"{name} is not a palindrome.")

# number of words in the sentence
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# print(f"The number of words in the sentence is: {len(words)}")

# Count occurrences of each character.

# text = input("Enter a string: ")
# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] =1

# print("Frequency of characters:")
# for ch, count in freq.items():
#     print(f"{ch}: {count}")


# Reverse each word in a sentence.

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# for i in range(len(words)):
#     words[i] = words[i][::-1]
    
# print(" ".join(words))

# Print characters at even indices.

# text = input("Enter a string: ")
# even_chars = ""

# for i in range(0, len(text), 2):
#     even_chars += text[i]

# print(even_chars)


# Check if two strings are anagrams
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# if sorted(str1) == sorted(str2):
#     print(f"{str1} and {str2} are anagrams.")
# else:
#     print(f"{str1} and {str2} are not anagrams.")


# DSA wise

# str1 = "hint"
# str2 = "thin"

# dict1 = {}
# for ch in str1:
#     if ch in dict1:
#         dict1[ch] += 1
#     else:
#         dict1[ch] = 1

# for ch in str2:
#     if ch not in dict1:
#         print("Not Anagram")
#         break

#     dict1[ch] -= 1

#     if dict1[ch] < 0:
#         print("Not Anagram")
#         break
#     else:
#         print("Anagram")