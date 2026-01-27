#w2A1
print("Hello world!")
#W2A2
print(f"Chao mung{input("Nhap ten cua ban")} da den voi CS1")
#W2A3
a, b = map(int,input("Nhap 2 so nguyen").split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b,2))
#W2A4
a1, b1, c1, a2, b2, a3 = map(float,input("Nhap diem").split())
print("Diem trung binh la:", ((a1+b1+c1)+(a2+b2)*2+a3*30)/10)
#W2A5
a, b = map(int,input("Nhap 2 so").split())
print(a**b)
#W2A6
a = input("Nhap chu cai")
print(ord(a))
print(chr(ord(a)-32))
#W2A7
A = ((13**2)*3)+5
B = 13**2*3+5
print(A)
print(B)
#W2A8
C = float(input("Nhap do C"))
F = 9/5*C + 32
print(f"{F:.2f}")
#W2A9
a = float(input("Nhap gia dong ho"))
print("Tong so tien la:", f"{(10 + a*1,4),2}")
#W2A10
name = input("Nhap ten ba nguoi")
print("Hi", name[::-1])
#W2A11
h , m = map(float,input("Nhap so gio va so phut").split())
print(h*3600 + m*60)
#W2A12
n = int(input("Nhap do dai canh"))
print("So luong mieng dan rieng la:", n*n*6)
#W2A13
a, b = map(float, input("Nhap 2 so").split())
c = a*b
print(f"{c:.2f}")
#W2A14
a,b = map(int, input().split())
a,b = b,a 
print(a)
print(b)
#W2A15
n = int(input("Nhap so nguyen duong n"))
print("So sao thu n:", 6*n*(n-1)+1) 
#W2A16
print("Spring\nSummer\nAutumn\nWinter")
#W2A17 
for i in range(1,6,2):
    print("*"*i)
#W2A18
print("### # #   ### ###\n #  #  #   #   # \n #  #   #  #   # \n #  #  #   #   # \n #  ##     #   # ")
#W2A19
print("Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday")
#W2A20 
print("January\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember")
#W2A21
for i in range(10):
    print("Hello world")
