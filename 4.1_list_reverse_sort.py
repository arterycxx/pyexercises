"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. The list of 8 budgets from the exercise 4.0
#    is written directly in the program.
# 2. Process: the list is put in four different orders. Two use sorted()
#    (returns a new list), one uses a copy + .reverse() (changes the copy
#    in place), one uses a copy + .sort(key=str) (changes the copy in place).
#    The original is never touched.
# 3. Out: four lines, one per order, and a last line with the original list.
# 4. My four orders, and which ones modify the original:
#    - ascending:       sorted(budgets)                 -> new list, original safe
#    - descending:      sorted(budgets, reverse=True)   -> new list, original safe
#    - reversed:        copy + .reverse()               -> changes the COPY in place
#    - sorted as text:  copy + .sort(key=str)           -> changes the COPY in place
#    .reverse() and .sort() modify a list in place and return None.
#    sorted() returns a new list. If I called .sort() or .reverse() directly
#    on budgets, the original would be modified. I used copies to avoid that.

# Your code below
budgets = [283000, 150000, 95000, 210000, 60000, 120000, 45000, 175000]

ascending = sorted(budgets)
descending = sorted(budgets, reverse=True)

reversed_copy = budgets.copy()
reversed_copy.reverse()

text_order = budgets.copy()
text_order.sort(key=str)

print("Ascending :", ascending)
print("Descending:", descending)
print("Reversed  :", reversed_copy)
print("As text   :", text_order)

print("Original  :", budgets)

# CHECK: original in 4.0 was [283000, 150000, 95000, 210000, 60000, 120000, 45000, 175000]
# Original printed now: [283000, 150000, 95000, 210000, 60000, 120000, 45000, 175000]
# I compared them item by item and they are the same, same order. The original
# was not changed because .reverse() and .sort() were used only on copies,
# and sorted() returns a new list.
