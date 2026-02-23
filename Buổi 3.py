

#W2A1
print("Hello, World")

#W2A2
name = input("Nhập tên của bạn")
print(f"Xin chào '{name}'")

#W2A3
a = int(input())
b = int(input())
print("Kết quả là", a+b, a-b, a*b, a//b, a%b)

#W2A4
a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
print("Số điểm trung bình là:", ((a1 + b1 + c1)+(a2 + b2)*2 + a3 *3)/10)

#W2A6
x = input()
print(ord(x))
print(chr(ord(x) + 32))

#W2A7
a = int(((13 ** 2) * 3) + 5)
print(a)
b = int(13**2*3 + 5)
print(b)

#W2A8
a = int(input("Nhập độ C :"))
print("Độ F là:", 1.8 * a + 32)

#W2A9
x = float(input("Nhập giá đồng hồ (USD): "))
tong_tien = x * 1.4 + 10
print("Số tiền phải trả:", round(tong_tien, 2), "USD")

#W2A10
a, b, c = input("Nhập tên 3 người").split()
print("xin chào", c, b, a)

#W2A11
h = int(input("Số giờ là:"))
k = int(input("Số giây là:"))
print("Số giây là: ", h*3600 + k*60)

#W2A12
n = int(input('Nhập số n: '))
print("Số miếng dãn cần thiết là:", n**2 *6)

#W2A13
a = int(input())
b = int(input())
print("Kết quả:", float(a*b%10))

#W2A14
a = 5
b = 7
a, b = b, a
print("a =", a)
print("b =", b)

#W2A16
print("Spring\nSummer\nAutumn\nWinter")

#W2A17
print("*\n***\n*****")

#W2A18
print("### # #  ### ###\n #  #  #  #   # \n #  #   # #   #\n #  #  #  #   #\n #  # #   #   #  ")

#W2A19
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in days:
  print(i)

#W2A20
x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in x:
  print(i)

#W2A21
print("Hello, World\n" *10)

lab 02

#W2A1
a = 7
b = 5
c = a - b
print(c) in c

#W2A2
city = "Hà Nội"
year = 2025
print("Thành phố: ", city, " - Năm: ", year)

#W2A3
n = 4
t = 0
for i in range(1, n+1):
    t += i
print(t)

#W2A4
numbers = [1, 2, 3, 4]
for x in numbers:
  if x % 2 == 0:
    print(x, "là số chẵn")
  else:
    print(x, "là số lẻ")

#W2A5
animals = ["cat", "dog", "cat", "bird"]
count = 0
for a in animals:
    count += 1
    print("Số phần tử trong danh sách là:", count)

#W2A6
=== AI Prediction System ===
1) Sentiment analysis
2) Weather forecast
3) Exit
Please choose an option:

#W2A7
num = int(input("Nhập số: "))
if num % 2 == 0:
  print("Chẵn")
else:
   print("Lẻ")

#W2A8
for i in range(3):
  print("AI đang học lần", i + 1)
  print("Huấn luyện xong!")

#W2A9
for x in ["cat", "dog", "fish"]:
 print("Dự đoán con vật:", x)

#W2A10
# Simple menu
print("=== AI Prediction System ===")
print("1) Sentiment analysis")
print("2) Weather forecast")
print("3) Exit")
print("Please choose an option:")
