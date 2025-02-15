# a,b =map(int,input().split())
# if a==0: 
#     if b==0:
#         print('WOW')
#     else:
#         print('NO')
# else:
#     x=-b/a
#     print(round(x,2))

# a,b,c=map(int,input().split())
# import math
# if a==0:
#     if b==0:
#         if c==0:
#             print('WOW')
#         else:
#             print('NO')
#     else:
#         x=-c/b
#         print(round(x,2))
# else:
#     d=b**2-4*a*c
#     if d>0:
#         x1=(-b+math.sqrt(d))/(2*a)
#         x2=(-b-math.sqrt(d))/(2*a)
#         print(round(x2,2),round(x1,2))
#     elif d==0:
#         x=-b/2*a
#         print(round(x,2))
#     else:
#         print('NO')



# def Nhap():
#     print('Nhap mot so nguyen:')
#     n=int(input('n='))
#     return n
# def Tinh(n):
#     S=0
#     for i in range(1,n+1):
#         S=S+i
#     return S
# def Inkq(n,S):
#     print('Tong cua ',n,' so nguyen duong dau tien= ',S,sep='')
# n=Nhap()
# S=Tinh(n)
# Inkq(n,S)

# a,b=map(int,input().split())
# for i in range(a,b+1):
#     print(i,end=" ")

# a=int(input())
# S=0
# for i in range(1,a+1):
#     S=S+i
# print(S)

# a=int(input())
# S=sum(range(2,a+1))+2*a
# print(S)


# n=int(input())
# S=0
# for i in range(2,n+1):
#     S=S+1/i
# print("{:.4f}".format(S))
# L=[]
# print('Nhap day so:')
# while True:
#     n=int(input())
#     L=L+[n]
#     if n==0:
#         break
# a=int(input('n='))
# if a in L:
#     print(f'{a} co ton tai')
# else:
#     pass    


# n=int(input())
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)

# a,b=map(int,input().split())
# n=1
# for i in range(1,a+1):
#     n*=i
# m=1
# for i in range(1,b+1):
#     m*=i
# c=1
# for i in range(1,a-b+1):
#     c*=i
# d=n/(m*c)
# print(int(d))

# a,b=map(int,input().split())
# S=0
# for i in range(a,b+1):
#     if i%2==0:
#         S+=i
# print(S)
# while True:
#     n=int(input())
#     count=0
#     if n==0:
#         count=1
#     elif n<0:
#         n=abs(n)
#     while n>0:
#         n//=10
#         count+=1
#     print(count)

# import math
# def is_prime(n):
#     if n<2:
#         return False
#     elif n<=3:
#         return True
#     elif n%2==0 or n%3==0:
#         return False
#     i=5
#     while i*i<=n:
#         if n%i==0 or n%(i+2)==0:
#             return False
#         i+=6
#     return True
# n=int(input())
# if is_prime(n):
#     print('YES')
# else:
#     print('NO')

# def Nhap(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def kiemtra(n):
#     if not Nhap(n):
#         return False
#     if Nhap(n-2) and Nhap(n+2):
#         return True
#     return False
# def inkq():
#     n=int(input())
#     if kiemtra(n):
#         print('YES')
#     else:
#         print('NO')
# inkq()
# n=int(input())
# S=0
# for i in range(1,n+1):
#     S=S+i
# if S==n:
#     print('YES')
# else:
#     print('NO')

# m=int(input())
# if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
#     print(31)
# elif m==2:
#     print(28)
# else:
#     print(30)
# n=str(input())
# a=n.count('W')
# b=n.count('L')
# if a==5 or a==6:
#     print(1)
# elif a==3 or a==4:
#     print(2)
# elif a==2 or a==1:
#     print(3)
# else:
#     print(-1)

# a,b=map(int,input().split())
# if 1<(a-b)<=20:
#     print(f'You are speeding and your fine is $100.')
# elif 21<(a-b)<=30:
#     print(f'You are speeding and your fine is $270.')
# elif (a-b)>=31:
#     print(f'You are speeding and your fine is $500.')
# else:
#     print('Congratulations, you are within the speed limit!')

# n=input()
# if len(n)!=2:
#     quit
# else:
#     A=n[0]
#     B=n[1]
# if A=='b' and B=='d' or A=='p' and B=='q':
#     print('mirrored')
# elif A=='d' and B=='b' or A=='q' and B=='p':
#     print('mirrored')
# else:
#     print('ordinary')

n=int(input())
for i in range(n):
    m=input()
    array=m.split()
    if len(m)!=n:
        quit
    # a=None
    # b=None
    # c=None
    # d=None 
    for i in range(0, len(array)):
        if i==0:
            a = int(array[i])
        if i==1:
            b = int(array[i])
        if i==2:
            c = int(array[i])
        if i==3:
            d = int(array[i])
max=None
min=None
if max is None or a>max:
    max=a
elif min is None or a<min:
    min=a
if max<b:
    max=b
elif min>b:
    min=b
if max<c:
    max=c
elif min>c:
    min>c
if max<d:
    max=d
elif min>d:
    min=d
print(max,min)