"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one whole number N tyepd by user
# 2. Process:the program first checks that N is allowed (from 1 to 100).If it is, a loop goes through every number from 1 to N, and for each
#    one it checks the remainder of the division by 2 (% 2).
# 3. Out:N lines, one per number, like "3 odd" or "4 even".
#    If N is not allowed, one line with an error message instead
# 4. What happens on 0, on a negative number, on a very large number:
#0: the program prints "Put number bigger than 0" and stops.
#   negative number: the same message, because there are no numbers from 1 to N.
#   very large number (more than 100): the program prints
#      "Put number less than 100" and stops.


# Your code below
n = int(input("Enter a number N: "))

if n < 1:
    print("Put number bigger than 0")
elif n > 100:
    print("Put number less than 100")
else:
    for number in range(1, n + 1):
        if number % 2 == 0:
            print(number, "even")
        else:
            print(number, "odd")
# CHECK: 
# N = 6:    1 odd 2 even 3 odd 4 even 5 odd 6 even
# N = 0:    Put number bigger than 0, as expected.
# N = -4:   Put number bigger than 0, as expected
# N = 5000: Put number less than 100, as expected.