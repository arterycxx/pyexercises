"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. The list of 8 budgets from exercise 4.0
#    is copied directly into the program.
# 2. Process: the total is calculated once, before the loop. Then a loop goes
#    through every budget with enumerate(), which gives the position and the
#    item together. For each budget, its share of the total is calculated.
# 3. Out: 8 lines, one per budget, like "1. 283000 -> 24.9% of the total".
# 4. What I compute for each item, and why it is worth showing:
#    The share of the total budget, in percent. A raw number like 95000 says
#    little by itself. "8.3% of everything I spend" shows at once which
#    campaigns carry the money and which ones are small.

# Your code below
budgets = [283000, 150000, 95000, 210000, 60000, 120000, 45000, 175000]

total = sum(budgets)

for position, budget in enumerate(budgets, start=1):
    share = budget / total * 100
    print(f"{position}. {budget} -> {share:.1f}% of the total")

# CHECK: lines printed: 8, items in the list: 8. No off-by-one.
# Share of the first item by hand: 283000 / 1138000 * 100 = 24.87, about 24.9
# The program printed: 24.9%, the same as my hand calculation.
