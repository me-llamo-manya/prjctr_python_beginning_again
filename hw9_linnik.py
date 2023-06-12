# Algo-Riddles: The Coding Conundrum


# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).


# Write a program that simply outputs which cats have hats at the end.

# Optional: Make a function that can calculate hats with any amount of rounds and cats.

# Here you should write an algorithm, and after that, try to make pseudo code. Only after that start to work. The code is simple here, but you might struggle with the algorithm. 
# Therefore don`t try to write a code from the first attempt. 
# Don't forget to calculate the complexity of your algorithm.

# at the start we have a list with cat's order number (as an index ) and it's state 
#  -- initially it will be 0 -- no hat
# (whether he has a hat - 1 or not - 0)

rounds = 100
cats = [0] * 100

for i in range(1, rounds + 1): #-- iteration through 100 rounds 
    for j in range(0, 100, i): #--iteration through cats with a step
        if cats[j] == 0:
            cats[j] = 1
        else:
            cats[j] = 0
# print(cats)
for x in range(len(cats)):
    if cats[x] == 1:
        print(x, end =" ")