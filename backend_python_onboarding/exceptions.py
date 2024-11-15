# a = 10
# b = 0
# a / b


fruits = ['apple', 'banana', 'strawberry']


# try:
#     fruits[2]
# except:
#     print("인덱스를 참조할 수 없습니다.")
# else:
#     print("정상 수행")

try:
    fruits[3]
except:
    print("인덱스를 참조할 수 없습니다.")
finally:
    print("명령 수행")

print(fruits)