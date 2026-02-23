

#1
def divide(a, b):
  try:
    return f"{a/b:.2f}"
  except ZeroDivisionError:
    return "Loi chia khong"
divide(3, 0)

#2
def get_item(lst, idx):
  try:
    return lst[idx]
  except IndexError:
    return "Truy cap chi so sai"
my_list = list(input().split())
n = int(input())
get_item(my_list, n)

#3
def check(a):
    lst = set()
    while a != 1 and a not in lst:
      lst.add(a)
      a = sum(int(i)**2 for i in str(a))
      if a in lst:
        raise ValueError
    if a == 1:
      return True
a = int(input())
try:
 if check(a):
   print("a la so hanh phuc")
except ValueError:
   print("a khong la so hanh phuc")

#4
def tong(a, b):
  try:
   print(float(a) + float(b))
  except:
   print("Nhap sai kieu du lieu")
  finally:
    print("Kết thúc chương trình")
x, y = input().split()
tong(x, y)

#5
def tran(lst):
  try:
    for i in range(len(lst)):
      lst[i] = int(lst[i])
    print(lst)
  except:
    print("Canh bao")
    lst.remove(lst[i])
    tran(lst)
mylist = list(input().split())
tran(mylist)

#6
import math
def can(n):
  try:
    a = math.sqrt(n)
    print(f"{a:.2f}")
  except ValueError:
    print("So am")
n = float(input())
can(n)

#7
def tuoi(n):
  try:
    print(2025 - int(n))
  except ValueError or n < 0:
    print("Tuoi khong hop le")
n = input()
tuoi(n)

#8
def check(n):
  try:
    n = list(n)
    if n[1] == "TXT" or n[1] == "txt" or n[1] == "zip":
      print("Doc file thanh cong")
  except:
    print("Flie khong hop le")
file1 = input().split(".")
check(file1)

#9
def tran(n):
  try:
    a = int(n)
    print(a)
  except:
    print("Chuoi khong hop le")

#10
def check(n):
  lst = []
  for i in range(n):
    k = int(input())
    lst.append(k)
  tong = 0
  if len(set(lst)) == len(lst):
    for i in lst:
      tong += i
    return tong
  else:
    return "Mang khong hop le"
n = int(input())
check(n)

