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

# 1. In: An answer entered by the user
# 2. Process: The program keeps asking until the user answers yes or reaches the attempt limit
# 3. Out: A summary showing how many attempts were made and how the loop ended
# 4. My stop condition, my attempt limit, my summary:
# The loop stops when the user answers yes or after 5 attempts
# Yes, yes and answers with extra spaces are treated the same
# The summary shows the number of attempts and whether the user answered yes or reached the limit


# Your code below
i = 0
while i < 5:
    print("Attempt number:", i + 1)
    i = i + 1


while True :
    answer = input("Do you want to continue? (yes/no): ")
    if answer.strip().lower() == "yes":
        print("You chose to continue.")
        break
    elif answer.strip().lower() == "no":
        print("You chose not to continue.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

attempts = 0
max_attempts = 5
success = False

while attempts < max_attempts:
    answer = input("Type yes to stop: ").strip().lower()
    attempts += 1

    if answer == "yes":
        success = True
        break

if success:
    print("Summary: you answered yes after", attempts, "attempt(s)")
else:
    print("Summary: maximum of", max_attempts, "attempts reached")
# Test with no expected answer: the loop stopped after 5 attempts
# Test with " YES ": spaces and capitals were accepted and the loop stopped after 1 attempt