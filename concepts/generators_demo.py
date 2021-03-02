def gen(n):
    while n<20:
        yield n
        n+=1

g=gen(10)

print(next(g))
print(next(g))
print(next(g))