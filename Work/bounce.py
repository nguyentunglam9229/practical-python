# bounce.py
#
# Exercise 1.5
decay_factor = 3/5
current_height = 100
for i in range(1, 11):
    print(round(current_height * decay_factor**i, 4))
