def mygen(n):
    for i in range(1, n + 1):
        yield i**2

n = int(input())
print(list(mygen(5)))
