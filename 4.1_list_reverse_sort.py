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

# 1. In: The list of 8 monthly investment budgets from exercise 4.0
# 2. Process: The program displays the list in four different orders without changing the original
# 3. Out: Four reordered lists and the original list at the end
# 4. My four orders, and which ones modify the original:
# Ascending, descending, reversed and shifted by one position
# None of them modify the original. sorted() and slicing create new lists


# Your code below
budgets = [200, 350, 150, 500, 300, 400, 250, 450]

ascending = sorted(budgets)
print("Ascending:", ascending)

descending = sorted(budgets, reverse=True)
print("Descending:", descending)

reversed_list = budgets[::-1]
print("Reversed:", reversed_list)

shifted = budgets[1:] + budgets[:1]
print("Shifted:", shifted)

print("Original list:", budgets)
# Test: the final original list is unchanged compared with exercise 4.0
