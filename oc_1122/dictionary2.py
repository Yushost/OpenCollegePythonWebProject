
menu = {'라면' : 4000, '만두' : 3500, '보쌈': 28000 }

while True:
    menu1 = input("메뉴를 입력하세요:")
    if menu1 in menu:
        cost = menu.get(menu1)
        print(menu1 + "의 가격은 " + str(cost) + "원입니다")
    else:
        print(menu1 + '란 메뉴는 없습니다')

