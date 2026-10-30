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

# 1. In: The list of 8 monthly investment budgets from exercise 4.0
# 2. Process: The program goes through every budget, shows its position and calculates its share of the total
# 3. Out: One line for each budget with its position, value and percentage of the total
# 4. What I compute for each item, and why it is worth showing:
# I calculate each budget's percentage of the total
# This shows how important each budget is compared with the whole amount


# Your code below
names = ["Sugumaran", "John", "Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

print("List of names and their lengths:")

i = "Alice"

for i in names:
    length = len(i)
    print("Name: ", i, "Length:" , length)

budgets = [200, 350, 150, 500, 300, 400, 250, 450]

total = sum(budgets)

for position, budget in enumerate(budgets, start=1):
    percentage = (budget / total) * 100
    print("Position:", position, "Budget:", budget, "Percentage:", round(percentage, 2), "%")
# Test: 8 budgets in the list and exactly 8 lines printed
