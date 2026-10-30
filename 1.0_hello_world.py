"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In: My name as a string
# 2. Process: The program repeats my name 5 times and numbers each line
# 3. Out: My name is displayed 5 times, numbered from 1 to 5
# 4. My message, and why: I chose my name because it is a simple personal message


# Your code below

# Professor's code adapted with my name
# print("Otmane")
# print("1. Otmane")
# print("2. Otmane")
# print("3. Otmane")
# print("4. Otmane")
# print("5. Otmane")

# Improved version using a loop
for i in range(1, 6):
    print(i, "Otmane")