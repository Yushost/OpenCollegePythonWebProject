# for 문은 in 뒤에 있는 것들을 하나씩 차례로 꺼내와서 for 앞에 집어넣고 수행하는 것


a = {"USC" : "1, December", "Manoa" : "15, January"}

for name in a:
    print(name)

for value in a.values():
    print(value)

for item in a.items():
    print(item)

# 특정횟수만큼 반복하고 싶을 떄 - range 사용 ( 위에꺼랑 상관없음 )
for a in range(10):
    print(a)




