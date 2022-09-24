n = int(input())
for i in range(0, n):
    a = input()
    if len(a) <= 10:
        print(a)
    else:
        s = len(a) - 2
        print(f"{a[0]}{s}{a[-1]}")