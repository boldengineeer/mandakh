n = int(input())
s = 0

for i in range(1, n//2+1):
    if n % i == 0:
        s += i

if n == s:
    print('YES')
else:
    print('NO')
