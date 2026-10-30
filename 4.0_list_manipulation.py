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

# 1. In: A list of 8 monthly investment budgets
# 2. Process: The program displays the list, one item, sorts it and calculates the total
# 3. Out: The whole list, one budget, the sorted list and the total
# 4. What my list is about, and what I computed from it:
# My list contains monthly investment budgets in euros
# I calculate the total to know how much money is invested


# Your code below
number_1 = 4
number_2 = 5
number_3 = 6
number_4 = 7
number_5 = 8
number_6 = 9

print(number_1)
print(number_2)
print(number_3)
print(number_4)
print(number_5)
print(number_6)

list = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]

print(list)
print(list[3])

list.sort()
print("Sorted list:", list)

list.pop()
print("List after removing last item:", list)

# My list of 8 monthly investment budgets
budgets = [200, 350, 150, 500, 300, 400, 250, 450]

print("Budgets:", budgets)
print("One budget:", budgets[3])

budgets.sort()
print("Sorted budgets:", budgets)

total = sum(budgets)
print("Total investment budget:", total)
# Test with 3 budgets: 200 + 350 + 150 = 700, and Python also gives 700