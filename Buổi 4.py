
#W4A1
n=int(input())
s=0
for i in range(n+1): s+=i
print(s)

#W4A2
def prime(n):
    if n==2 or n==3: return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
n=int(input("Enter n: "))
while n<=0:
    n=int(input("n must be positive: "))
print(prime(n))

#W4A3
n=int(input())
s=1
for i in range(2,n+1): s*=i
print(s)

#W4A4
n=abs(int(input()))
c=0
while n>0:
    n//=10
    c+=1
print(c)

#W4A5
arr=list(map(int,input().split()))
s="I've found the meaning of life!" if 42 in arr else "It's a joke!"
print(s)

#W4A6
import math
def check(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True
a, b = map(int, input().split())
tong = 0
for i in range(a, b + 1):
  if check(i):
    tong += i
print(tong)

#W4A7
def is_prime(b):
    is_prime=[1]*(b+1)
    is_prime[0]=is_prime[1]=0
    i=2
    while i*i<=b:
        if is_prime[i]:
            for j in range(i*i,b+1,i):
                is_prime[j]=0
        i+=1
    return is_prime
n=int(input())
check=is_prime(n)
for i in range(n,-1,-1):
    if check[i] and n%i==0:
        print(i)
        break

#W4A8
def reverse(n):
    res=0
    while n>0:
        res=res*10+n%10
        n//=10
    return res
def palindrome(n):
    c=0
    while n!=reverse(n):
        n+=reverse(n)
        c+=1
    return f'{c} {n}'

n=int(input())
print(palindrome(n))

#W4A9
def check(n):
    i=int(n**0.5)
    if i*i!=n: return False
    digit=[]
    for i in str(n):
        if i not in digit:
            digit.append(i)
        else:
            return False
    return True

n=int(input())
for i in range(1,n+1):
    if check(i):
        print(i,end=' ')

#W4A10
def collatz(n):
    c=1
    while n!=1:
        n=n*3+1 if n&1 else n//2
        c+=1
    return c
n=int(input())
res=0
x=0
for i in range(1,n+1):
    a=collatz(i)
    if a>res:
        x=i
        res=a
print(f'{x} {res}')

#W4A11
n=int(input())
res=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        j=n//i
        if not i&1: res+=1
        if not j&1: res+=1
print(res)

#W4A12
money,n=map(int,input().split())
print(int(money*((1+0.7/100)**n)))

#W4A13
def sum_divisor(n):
    s=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s+=(i+n//i)
    return s
a,b=map(int,input().split())
print(sum_divisor(a)==b and sum_divisor(b)==a)

#W4A14
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

a,b=map(int,input().split())
print(gcd(a,b))

#W4A15
n,m=map(int,input().split())
if m&1: print('Invalid')
else:
    dog=(m-2*n)//2
    chick=n-dog
    print(chick,'' ,dog)

#W4A16
for i in range(3,100,3):
    if not i&1: print(i)

#W4A17
a=int(input())
for i in range(1,6):
    print(f'{a} x {i} = {a*i}',end="     ")
    print(f'{a} x {i+5} = {a*(i+5)}',)

#W4A18
a,b=map(int,input().split())
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0: print(i)

#W4A19
n=int(input())
for i in range(2,n+1):
    if not i&1: print(i)

#W4A20
n=int(input())
if not n&(n-1): print(True)
else: print(False)

#W4A21
n=int(input())
s=0
while n>0:
    s+=n%10
    n//=10
print(s)

#W4A22
n=int(input())
odd,even=0,0
while n>0:
    if (n%10)&1: odd+=1
    else: even+=1
    n//=10
print("Odd: ",odd)
print("Even: ",even)

#W4A23
n=int(input())
s=0
k=0
while s<n:
    k+=1
    s+=k
print(k-1)

#W4A24
n=int(input())
s=0
k=0
while s<=n:
    k+=1
    s+=(1/k)
print(k)

#W4A25
n=0
M,m=float('-inf'),float('inf')
while n!=-1:
    n=int(input())
    if n>M: M=n
    if n<m: m=n
print("Max:" ,M)
print("Min:",m)

#W4A26
n=int(input())
a,b=1,1
while b<=n:
    a,b=b,a+b
print(a)

#W4A27
s=input()
c=0
for i in range(len(s)):
    if i==0 and s[0]!=' ' or (s[i-1]==' ' and s[i]!=' '):
        c+=1
print(c)

#w4A28
s=input()
i=0
while i<len(s) and s[i]==" ":
    i+=1
j=i
while j<len(s) and s[j]!=" ":
    j+=1
print(s[i:j])

#W4A29
a,b,c=map(int,input().split(","))
print(a+b+c)

#W4A30
s=input()
lst=[0]*3
for i in s:
    if i.islower(): lst[0]+=1
    elif i.isupper():lst[1]+=1
    elif i.isdigit(): lst[2]+=1
print("Lower:",lst[0])
print("Upper:",lst[1])
print("Digit:",lst[2])

#W4A31
s=input()
res=0
for i in s:
    if i.isdigit(): res+=int(i)
print(res)

#W4A32
def strong_pass(s):
    if len(s)<6: return False
    lst=[0]*4
    for i in s:
        if i.isdigit(): lst[2]=1
        elif i.isupper(): lst[1]=1
        elif i.islower(): lst[3]=1
        elif i!=' ': lst[0]=1
    return not 0 in lst

s=input()
print(strong_pass(s))

#W4A33
n=int(input())
n=list(str(n))
i=len(n)-3
while i>0:
    n.insert(i,'.')
    i-=3
print(''.join(n))

#W4A34
a=input()
b=input()
a=a.replace(b,'')
print(a)
