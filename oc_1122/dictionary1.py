# 딕셔너리의 key만 빼오고 싶거나 value만 빼오고 싶을 때 - key, value 함수 사용하여 빼온 뒤 리스트 사용 / items 함수는

a = {"맥북13인치2015" : 80, "ps4slim": 20, "desktopPC": 40}
b = a.values()
print(b)
print(type(b))

b = list(a.keys())
print(b)
print(type(b))



