a = input()
b = input()
if a.upper() == b.upper():
    print("0")
elif a.upper() < b.upper():
    print("-1")
else:
    print("1")