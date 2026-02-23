#W7A1
def tim(a, l, r, x):
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

mang = list(map(int, input().split()))
k = int(input())
print(tim(mang, 0, len(mang) - 1, k))

#W7A2
a = list(map(int, input().split()))
k = int(input())
print(a.count(k))

#W7A3
a = list(map(int, input().split()))
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

#W7A4
a = list(map(int, input().split()))
max_lan = 0
kq = a[0]
for x in a:
    dem = a.count(x)
    if dem > max_lan:
        max_lan = dem
        kq = x
print(f"{kq} xuat hien nhieu nhat, som nhat, {max_lan} lan")

#W7A5
a = list(map(int, input().split()))
k = int(input())
dem = 0
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            dem += 1
print(dem)

#W7A6
chuoi = input()
a = eval(chuoi)
kq = []
for x in a:
    for y in x:
        kq.append(y)
print(kq)

#W7A7
a = eval(input())
n = len(a)
f = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j]:
            f[i] = max(f[i], f[j] + 1)
kq = 0
for i in range(n):
    if f[i] > kq:
        kq = f[i]
print(kq)

#W7A8
def tim_kiem(x, b):
    l = 0
    r = len(b) - 1
    kq = -1
    while l <= r:
        m = (l + r) // 2
        if x <= b[m][1]:
            if x >= b[m][0]:
                kq = b[m][1] - b[m][0] + 1
                r = m - 1
            else:
                l = m + 1
        else:
            l = m + 1
    return kq

doan = eval(input())
doan.sort(key=lambda y: (y[1], y[1] - y[0] + 1))
a = eval(input())
for k in a:
    print(tim_kiem(k, doan), end=" ")

#W7A9
a = list(map(int, input().split()))
n = len(a)
kq = []
for i in range(n):
    dem = 0
    for j in range(i + 1, n):
        if a[j] < a[i]:
            dem += 1
    kq.append(dem)
for x in kq:
    print(x, end=" ")

#W7A10
a = list(map(int, input().split()))
m = int(input())
n = len(a)
kq = 0
for i in range(n):
    tong = 0
    for j in range(i, n):
        tong = (tong + a[j]) % m
        if tong > kq:
            kq = tong
print(kq)

#W7A11
a = list(map(str, input().split()))
b = list(map(str, input().split()))

for i in range(len(a)):
    while a[i][-1].isalpha() == 0:
        a[i] = a[i][:-1]

dem = 0
n = len(a)
k = len(b)
for i in range(n - k + 1):
    if a[i:i + k] == b:
        dem += 1
print(dem)

#W7A12
a = []
ten = ['A', 'B', 'C', 'D']
for i in range(4):
    chuoi = input()
    a.append([chuoi, i])
a.sort()
for x in a:
    print(ten[x[1]], end=" ")

#W7A13
a = list(map(int, input().split()))
kq = 1
tap_hop = set(a)
for x in tap_hop:
    if x + 1 in tap_hop:
        dem = a.count(x) + a.count(x + 1)
        if dem > kq:
            kq = dem
print(kq)

#W7A14
n = int(input())
a = list(map(int, input().split()))
kq = []
for i in range(len(a)):
    if a[i] == 7:
        kq.append(i)
if len(kq) == 0:
    print("Not found")
else:
    kq.sort(reverse=True)
    print(*kq)

#W7A15
n = int(input())
a = []
for _ in range(n):
    chuoi = input()
    a.append(chuoi)
for i in range(len(a)):
    if a[i] == 'Nemo':
        if i == 0:
            print(f"{a[-1]} and {a[i + 1]}")
        elif i == len(a) - 1:
            print(f"{a[i - 1]} and {a[0]}")
        else:
            print(f"{a[i - 1]} and {a[i + 1]}")
