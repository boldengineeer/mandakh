n = int(input())
s = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        s += a
    n = n//10
print(s)
