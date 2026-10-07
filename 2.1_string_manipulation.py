"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: sentence typed by user.
# 2. Process:the sentences is cleaned and transformed into four different ways.
# 3. Out: four lines, one per transformation, each with a different transformation of the original sentence.
# 4. My four transformations, and when each is useful:
# strip():   removes spaces at both ends. Useful when a user accidentally types a space before or after an email or a name in a form.
# lower():   makes everything lowercase. Useful to compare answers without caring about capitals ("Yes", "YES" and "yes" become the same).
# title():   capitalises each word. Useful to display a customer's name icely in a report even if they typed it in lowercase.
# replace(): swaps one piece of text for another. Useful to turn a title into a file name by replacing spaces with underscores.



# Your code below
sentence = input("Enter a sentence: ")

print("strip()  :", repr(sentence.strip()))
print("lower()  :", sentence.strip().lower())
print("title()  :", sentence.strip().title())
print("replace():", sentence.strip().replace(" ", "_"))

# CHECK: I love to RUN in the MoRnings 
# strip():   changed nothing, no spaces in the beginning or end, as expected.
# lower():   all letters are lowercase, as expected.
# title():   each word  is capitalised, but RUN is transformed to Run and MoRnings to Mornings.
# replace(): led i_love_to_RUN_in_the_MoRning. Each space was replaced with _, and the case letters remained as entered (RUN and MoRning have not changed). 