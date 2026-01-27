def Max_Of_Two(a, b):
  if a > b:
    return a
  else:
    return b


def Max_Of_Int(a, b) ->int:
  return [a if a>b else b]
a, b = map(float, input().split())
print(*Max_Of_Int(a, b))

#1

def swap(a, b):
  a, b = b, a
  return a, b
swap(3,4)

#2

def check(x):
  for i in range(2, x):
    if x%i == 0:
      return False
  return x >1
#3

def check(n):
  count = 0
  if n == 0: return False
  for i in range(1,n):
    if n%i == 0:
      count+=i
  return count == n
def PerfectNumbers():
    assert check(6) == True, "The max of 34 and 56 should be 56"
    return True
if PerfectNumbers():
    print("True")

  #4

def nhapso():
  global n
  global k
  n = input()
  k = int(input())
def check(n, k):
  for i in range(len(n)):
    if int(n[i]) == k:
      return i
  return -1
def ktra():
    assert check([1, 2, 3, 4, 5, -6, 7, 8, 19, 1, 2, 3, 4, 5], 5) == 4, "Test1 is wrong"
if __name__ == "__main__":
    ktra()
    print("pass")
#5

# cách 1
def giaithua(n):
  count = 1
  if n == 0:
    return 1
  for i in range(1,n+1):
    count = count*i
  return count
  print(count)
giaithua(3)
# cách 2
def giaithua(n):
  count = 1
  if n == 0 or n == 1:
    return 1
  while n >1:
    count = count*n
    n -=1
  return count


def kiemtra():
  assert giaithua(3) == 6, "Tese wrong"

if __name__ == "__main__":
    kiemtra()
    print("All tests passed!")

#6

def caculator(a, b, dau):
  if dau == "+":
    return a+b
  elif dau == "-":
    return a-b
  elif dau == "*":
    return a*b
  elif dau == "/":
      if b == 0:
        if a == 0:
          print("Lỗi: Toán tử không xác định")
          return None
        return "Lỗi: Không thể chia cho không"
      return a/b



caculator(0, 0, "/")

#7

a, b = map(int, input().split())
def hamming(a, b):
  return(bin(a^b).count("1"))
hamming(a, b)

#8

def tong(n):
  count = 0
  while n>0:
    count += n%10
    n = n //10
  return count
def kiemtra():
  assert tong(34) == 7, "Test wrong"
if __name__ == "__main__":
    kiemtra()
    print("All tests passed!")
#9

a, b = input().split()
list = [0]*len(a)

def find_pos(word, char):
  list_pos = []
  for i in range(len(word)):
    if word[i] == char:
      list_pos.append(i)
  return list_pos

def word_mapping(a, b):
  for i in range(0, len(a)):
    if list[i] == 0:
      if find_pos(a, a[i]) != find_pos(b, b[i]):
        return False
      for j in find_pos(a, a[i]):
        list[j] = 1
  return True 
print(word_mapping(a, b))
#10