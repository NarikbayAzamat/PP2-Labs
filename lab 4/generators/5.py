def down_to_0(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in down_to_0(n):
    print(num)
