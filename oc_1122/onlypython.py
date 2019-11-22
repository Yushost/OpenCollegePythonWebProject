# List Comprehension

numbers = [1,2,3,6]
numbers_double = []
for a in numbers:
    numbers_double.append(a * 2)


number_double = [ number * 2 for number in numbers ]
print(number_double)


names = ["신봉건", "고유빈", "김진옥", "이광우"]
nimNames = []

for name in names:
    nimNames.append(name + "님")

for nicName in nimNames:
    print(nimNames)

# 파이썬에서만 되는 경우
nimNames2 = [ name + "님" for name in names ]

for nimName in nimNames2:
    print(nimNames)
