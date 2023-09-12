import random
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = []
# for i in range(0,10):
#     v.append(random.choice(values))
v = random.sample(values, 9)
print(v)