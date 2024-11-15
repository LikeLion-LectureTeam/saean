# f = open('literature\poem.txt', 'r', encoding='UTF-8')

# print(f.read())
# print(f.readline())
# print(f.readlines())

# f.close()

# with open('literature\poem.txt', 'r', encoding='UTF-8') as f:
#     print(f.read())

f = open('literature\poem.txt', 'a', encoding='UTF-8')

f.write("\n새로운 글이 작성되었습니다.")

f.close()

