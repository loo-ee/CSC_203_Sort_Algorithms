import math

def minimize(a: int, b: int):
    greater = max([a, b])

    for i in range(greater, 1, -1):
        if a % i == 0 and b % i == 0:
            return i

    return -1


a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

A: int
B: int
C = a * c

for i in range(1, C):
    for j in range(1, C):
        if i * j == C and i + j == b:
            A = i
            B = j

X = minimize(a, A)
Y = minimize(a, B)

print(f'{a}x + {A}')
print(f'{a}x + {B}')

print()

print(f'{a / X}x + {A / X}')
print(f'{a / Y}x + {B / Y}')
