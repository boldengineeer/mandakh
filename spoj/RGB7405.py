n = int(input())

for i in range(n):
    for j in range(n, i, -1):
        print(j, end=" ")
    print('')