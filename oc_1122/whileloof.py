# while 뒤에 bool type(true / false)가 오면 처리가 됨

sum = 0
n = 0

while n < 11:
    sum = sum + n
    n = n + 1

print(sum)

# break continue

n = 0
while n < 10:
    n = n + 1
    if n == 3:
        continue
    print("현재 n은" + str(n) + "입니다.")
