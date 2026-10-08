"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answers to one question, typed one by one.
# 2. Process: the program asks "Did you check the campaign budget?" again and
#    again. Each answer is cleaned with .strip().lower(), so "Yes", "yes" and
#    " yes " are the same answer. Every raw answer is saved in a list.
#    The loop stops when the answer is "yes" or when the attempts run out.
# 3. Out: a summary: how many attempts were used, all the answers typed,
#    and whether the budget was confirmed or not.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the cleaned answer is exactly "yes".
#    - Attempt limit: 5. After 5 wrong answers the program stops by itself
#      and says that nothing was confirmed.
#    - Summary: attempts used, the list of answers, the final result.
#    - My decision: "Yes", "YES" and " yes " all count as yes.
#      "y" does NOT count, only the full word "yes".

# Your code below
MAX_ATTEMPTS = 5
attempts = 0
answers = []
confirmed = False

while attempts < MAX_ATTEMPTS and not confirmed:
    answer = input("Did you check the campaign budget? (yes/no): ")
    attempts += 1
    answers.append(answer)
    if answer.strip().lower() == "yes":
        confirmed = True

print("--- Summary ---")
print("Attempts used:", attempts)
print("Answers given:", answers)
if confirmed:
    print("Budget confirmed on attempt", attempts)
else:
    print("Not confirmed after", MAX_ATTEMPTS, "attempts. Stopping.")


# CHECK:
# 1. I never typed "yes": the program asked exactly 5 times, then stopped by
#    itself and printed "Not confirmed after 5 attempts. Stopping."
#    The answers list kept my original text, including a space after the first "no".
# 2. I typed "YeS": it stopped on attempt 1 and counted it as yes.
#    The summary shows ['YeS']. I did not test extra spaces.