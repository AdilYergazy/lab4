# 1
print("#1")
N = int(input())
gen = (i ** 2 for i in range(N))
for i in gen:
    print(i)
# 2
print("#2")
n = int(input())
gen = (i for i in range(n) if i % 2 == 0)
print(*gen, sep=',')

# 3

print("#3")
def func(n):
    sas = (i for i in range(n) if i % 3 == 0 and i % 4 == 0)
    return (sas)


print(*func(n), sep=',')


# 4
print("#4")
def sq(a, b):
    for i in range(a, b + 1):
        yield i ** 2


for i in sq(1, 4):
    print(i, end=' ')
print()
# 5
print("#5")
n = 4
gen = (i for i in range(n, -1, -1))
for i in (gen):
    print(i)