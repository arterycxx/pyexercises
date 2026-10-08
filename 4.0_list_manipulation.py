"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:nothing typed by the user. The data (8 monthly campaign budgets)
# is written directly in the program.
# 2. Process:the list is stored in a variable, one item is picked by its
#    position, a sorted copy is made, and the total, the average and the
#    biggest budget are calculated with sum(), len() and max()
# 3. Out: the whole list, the first budget, the sorted list, the total,
#    the average and the maximum.
# 4. What my list is about, and what I computed from it:The list holds monthly budgets of 8 ad campaigns. I computed the total
#    (how much I spend in all), the average (what a "typical" campaign costs)
#    and the maximum (the most expensive campaign). The total is interesting
#    because it is the number a manager asks about first. Comparing the
#    maximum with the average shows if one campaign eats most of the money.


# Your code below
budgets = [283000, 150000, 95000, 210000, 60000, 120000, 45000, 175000]

print("All budgets:", budgets)
print("First budget:", budgets[0])
print("Sorted budgets:", sorted(budgets))

total = sum(budgets)
average = total / len(budgets)
biggest = max(budgets)

print("Total:", total)
print("Average:", average)
print("Biggest:", biggest)

# CHECK: I worked out by hand the sum of three items:
# 283000 + 150000 + 95000 = 528000
# The program agrees: yes. I temporarily changed the list to these three
# numbers, ran the program, and it printed Total: 528000.