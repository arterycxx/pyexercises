"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. The campaign is written directly
#    in the program as a dictionary.
# 2. Process: one field is read, one field is changed, one field is removed,
#    then a loop goes through the dictionary. At the end the program asks
#    for a field that does not exist, in a safe way.
# 3. Out: the campaign name, the new budget, then one line per remaining
#    field ("field: value"), then the answer for the missing field.
# 4. My object, my five fields, and why those:
#    Object: an advertising campaign.
#    - name:       to tell campaigns apart in reports.
#    - channel:    to know where the money goes (Meta Ads, Google Ads...).
#    - budget:     the number a manager asks about first.
#    - status:     to know if it is active, paused or finished.
#    - start_date: to compare results over time.
#    A sixth field, draft_note, is temporary: I add it only to practise removing.

# Your code below
campaign = {
    "name": "Winter Sale",
    "channel": "Meta Ads",
    "budget": 283000,
    "status": "active",
    "start_date": "2026-12-01",
    "draft_note": "check with manager",
}

# read
print("Campaign name:", campaign["name"])

# change
campaign["budget"] = 310000
print("New budget:", campaign["budget"])

# remove
del campaign["draft_note"]

# display every field with its value
for field, value in campaign.items():
    print(field, ":", value)

# a field that does not exist, made safe with .get()
print("End date:", campaign.get("end_date", "not set"))

# CHECK: first I wrote print(campaign["end_date"]) instead of the .get() line.
# What happened: the program printed all the fields, then crashed on line 67
# with KeyError: 'end_date', because the dictionary has no field with that name.
# Then I replaced it with .get("end_date", "not set") and it printed: not set
# The program no longer crashes, it prints the default value I chose.