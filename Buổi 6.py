

#1
a = input().split()
b = []
for i in range(len(a)):
  if i == 0 or a[i] != a[i-1]:
    b.append(a[i])
print(b)

#2
x = map(int, input().split())
y = []
t = 0
for i in x:
  t += i
  y.append(t)
print(y)

#3
t = tuple(map(int, input("Nhap day").split()))
m = int(input())
m = m % len(t)
l = list(t)
for _ in range(m):
  l.append(l.pop(0))
print(tuple(l))

#4
s = input().split()
d = {}
for x in s:
  u, v = x.split(":")
  if u not in d:
    d[u] = [v]
  else:
    d[u].append(v)
print(d)

#5
arr = list(map(int, input().split()))
p = 0
am = 0
z = 0
for x in arr:
  if x > 0: 
    p += 1
  elif x < 0: 
    am += 1
  else: 
    z += 1
kq = {"positive": p, "negative": am, "zero": z}
print(kq)

#6
ds = list(map(int, input("Nhap day").split()))
s = 0
for x in ds:
  s += x
print(s)

#6
a = list(map(int, input().split()))
print(sum(a))

#7
t = tuple(input().split())
a = list(t)
a.reverse()
print(t[0], t[-1])
print(tuple(a))

#8
a = input().split()
d = {}
for x in a:
  if x not in d:
    d[x] = 1
  else:
    d[x] += 1
print(d)

#9
def f(x):
  d = {}
  for i in x:
    u, v = i.split(":")
    d[u] = int(v)
  return d
a = input().split()
b = input().split()
d1 = f(a)
d2 = f(b)
c = {}
for k in d1:
  if k in d2:
    c[k] = d1[k] + d2[k]
print(c)

#10
a = list(map(int, input().split()))
m = int(input())
s = set()
for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] + a[j] == m:
      s.add((a[i], a[j]))
kq = sorted(s)
print(kq)

#11
t = tuple(map(int, input().split()))
c = []
l = []
for x in t:
  if x % 2 == 0:
    c.append(x)
  else:
    l.append(x)
print(tuple(c))
print(tuple(l))

#12
a = input().split()
d = {}
for x in a:
  u, v = x.split(":")
  d[u] = v
print(d)

#13
a = input().split()
d = {}
for i in range(1, len(a), 2):
  d[a[i]] = a[i-1]
print(d)

#14
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
kq = []
for x in a1:
  if x in a2 and x not in kq:
    kq.append(x)
print(kq)

#15
a = input().split()
m = int(input())
d = {}
for i in range(1, len(a), 2):
  if int(a[i]) > m:
    d[a[i-1]] = a[i]
print(d)

#17
x = int(input("Nhap so hang"))
mt = []
for i
