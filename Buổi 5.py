def f(x, y):
  if x > y:
    return x
  else:
    return y

def g(x, y) ->int:
  return [x if x>y else y]
u, v = map(float, input().split())
print(*g(u, v))

#1

def h(x, y):
  x, y = y, x
  return x, y
h(3,4)

#2

def p(x):
  if x < 2:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True

#3

def q(x):
  if x == 0: return False
  s = sum([i for i in range(1, x // 2 + 1) if x % i == 0])
  return s == x

def r():
    assert q(6) == True, "The max of 34 and 56 should be 56"
    return True
if r():
    print("True")

#4

def s():
  global u
  global v
  u = input()
  v = int(input())

def t(x, y):
  for i in range(len(x)):
    if int(x[i]) == y:
      return i
  return -1

def k():
    assert t([1, 2, 3, 4, 5, -6, 7, 8, 19, 1, 2, 3, 4, 5], 5) == 4, "Test1 is wrong"
if __name__ == "__main__":
    k()
    print("pass")

#5

# cách 1
def f1(x):
  if x == 0 or x == 1:
    return 1
  return x * f1(x - 1)
f1(3)

# cách 2
def f2(x):
  import math
  return math.factorial(x)

def k2():
  assert f1(3) == 6, "Tese wrong"

if __name__ == "__main__":
    k2()
    print("All tests passed!")

#6

def c(x, y, z):
  if z == "+":
    return x+y
  elif z == "-":
    return x-y
  elif z == "*":
    return x*y
  elif z == "/":
      if y == 0:
        if x == 0:
          print("Lỗi: Toán tử không xác định")
          return None
        return "Lỗi: Không thể chia cho không"
      return x/y

c(0, 0, "/")

#7

m, n = map(int, input().split())
def b(x, y):
  return(bin(x^y).count("1"))
b(m, n)

#8

def d(x):
  return sum(int(i) for i in str(x))

def k3():
  assert d(34) == 7, "Test wrong"
if __name__ == "__main__":
    k3()
    print("All tests passed!")

#9

u, v = input().split()
z = [0]*len(u)

def a(x, y):
  r = []
  for i, j in enumerate(x):
    if j == y:
      r.append(i)
  return r

def m_1(x, y):
  if len(x) != len(y): return False
  d1, d2 = {}, {}
  for i, j in zip(x, y):
    if i not in d1 and j not in d2:
      d1[i] = j
      d2[j] = i
    elif d1.get(i) != j or d2.get(j) != i:
      return False
  return True
print(m_1(u, v))

#10
