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

# 1. In:"Hello World"
# 2. Process:the program repeats the prints 5 times 
# 3. Out: five statement 
# 4. My message, and why:# 4. My message, and why: "Hello World" is the first program every programmer writes, so it feels like a good way to start learning Python.


# Your code below
print(1, "Hello World")
print(2, "Hello World")
print(3, "Hello World")
print(4, "Hello World")
print(5, "Hello World")

for number in range(1, 6):
    print(number, "Hello World")
