
#W4A1
x = int(input())
print(x * (x + 1) // 2)

#W4A2
def f(a):
    if a == 2 or a == 3: return True
    for k in range(2, int(a**0.5) + 1):
        if a % k == 0: return False
    return True

x = int(input("Enter n: "))
while x <= 0:
    x = int(input("n must be positive: "))
print(f(x))

#W4A3
a = int(input())
b = 1
while a > 1:
    b *= a
    a -= 1
print(b)

#W4A4
u = input()
print(len(u.replace('-', '')))

#W4A5
q = list(map(int, input().split()))
w = "I've found the meaning of life!" if 42 in q else "It's a joke!"
print(w)

#W4A6
import math
def g(x):
  for j in range(2, int(math.sqrt(x)) + 1):
    if x % j == 0:
      return False
  return True

m, n = map(int, input().split())
print(sum(k for k in range(m, n + 1) if g(k)))

#W4A7
def h(x):
    y = [1] * (x + 1)
    y[0] = y[1] = 0
    z = 2
    while z * z <= x:
        if y[z]:
            for w in range(z * z, x + 1, z):
                y[w] = 0
        z += 1
    return y

a = int(input())
b = h(a)
for c in range(a, -1, -1):
    if b[c] and a % c == 0:
        print(c)
        break

#W4A8
def f2(x):
    y = 0
    while x != int(str(x)[::-1]):
        x += int(str(x)[::-1])
        y += 1
    return f'{y} {x}'

z = int(input())
print(f2(z))

#W4A9
def g1(x):
    y = int(x**0.5)
    if y * y != x: return False
    z = []
    for w in str(x):
        if w not in z:
            z.append(w)
        else:
            return False
    return True

a = int(input())
for b in range(1, a + 1):
    if g1(b):
        print(b, end=' ')

#W4A10
def h1(x):
    y = 1
    while x != 1:
        x = x * 3 + 1 if x & 1 else x // 2
        y += 1
    return y

a = int(input())
b = 0
c = 0
for d in range(1, a + 1):
    e = h1(d)
    if e > b:
        c = d
        b = e
print(f'{c} {b}')

#W4A11
x = int(input())
y = 0
for z in range(1, int(x**0.5) + 1):
    if x % z == 0:
        w = x // z
        if not z & 1: y += 1
        if not w & 1: y += 1
print(y)

#W4A12
u, v = map(int, input().split())
print(int(u * ((1 + 0.7 / 100)**v)))

#W4A13
def f3(x):
    y = 1
    for z in range(2, int(x**0.5) + 1):
        if x % z == 0:
            y += (z + x // z)
    return y

p, q = map(int, input().split())
print(f3(p) == q and f3(q) == p)

#W4A14
def f4(x, y):
    if y == 0: return x
    return f4(y, x % y)

m, n = map(int, input().split())
print(f4(m, n))

#W4A15
x, y = map(int, input().split())
if y & 1: print('Invalid')
else:
    d = (y - 2 * x) // 2
    c = x - d
    print(c, '' , d)

#W4A16
for j in range(6, 100, 6):
    print(j)

#W4A17
u = int(input())
for v in range(1, 6):
    print(f'{u} x {v} = {u*v}', end="     ")
    print(f'{u} x {v+5} = {u*(v+5)}',)

#W4A18
x, y = map(int, input().split())
for z in range(1, min(x, y) + 1):
    if x % z == 0 and y % z == 0: print(z)

#W4A19
x = int(input())
for y in range(2, x + 1, 2):
    print(y)

#W4A20
a = int(input())
if not a & (a - 1): print(True)
else: print(False)

#W4A21
b = input()
print(sum(int(i) for i in b))

#W4A22
p = input()
q = sum(int(i) % 2 != 0 for i in p)
print("Odd: ", q)
print("Even: ", len(p) - q)

#W4A23
u = int(input())
v = 0
w = 0
while v < u:
    w += 1
    v += w
print(w - 1)

#W4A24
a = int(input())
b = 0
c = 0
while b <= a:
    c += 1
    b += (1 / c)
print(c)

#W4A25
a = 0
b, c = float('-inf'), float('inf')
while a != -1:
    a = int(input())
    if a > b: b = a
    if a < c: c = a
print("Max:", b)
print("Min:", c)

#W4A26
x = int(input())
y, z = 1, 1
while z <= x:
    y, z = z, y + z
print(y)

#W4A27
x = input()
print(len(x.split()))

#w4A28
x = input()
y = x.split()
print(y[0] if y else "")

#W4A29
x, y, z = map(int, input().split(","))
print(x + y + z)

#W4A30
x = input()
c1, c2, c3 = 0, 0, 0
for z in x:
    c1 += z.islower()
    c2 += z.isupper()
    c3 += z.isdigit()
print("Lower:", c1)
print("Upper:", c2)
print("Digit:", c3)

#W4A31
x = input()
print(sum(int(z) for z in x if z.isdigit()))

#W4A32
def f5(x):
    if len(x) < 6: return False
    y = [0] * 4
    for z in x:
        if z.isdigit(): y[2] = 1
        elif z.isupper(): y[1] = 1
        elif z.islower(): y[3] = 1
        elif z != ' ': y[0] = 1
    return not 0 in y

a = input()
print(f5(a))

#W4A33
x = input()
print(f"{int(x):,}".replace(',', '.'))

#W4A34
x = input()
y = input()
x = x.replace(y, '')
print(x)
