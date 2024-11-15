# tup = (1, 20, 40)
# print(tup[0])

# tup = (100, 30, 4)
# print(tup)

# for x in tup:
#     print(x)

tup = (1, 20, 40)

list_1 = list(tup)
print(list_1)

list_2 = [x for x in tup]
print(list_2)

list_3 = []

for x in tup:
    list_3.append(x)

print(list_3)

