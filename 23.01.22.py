#1st ex (min number)
a=int(input())
b=int(input())
print(min(a,b))

#2nd ex (sing (x))
x=int(input())
if x>0:
    print(1)
elif x<0:
    print(-1)
else:
    print(0)
    
#3rd ex (chess tile)
a=int(input())
b=int(input())

c=int(input())
d=int(input())
if (a+b+c+d)%2==0:
    print("YES")
else:
    print("NO")
    
#4th ex 
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("YES")
else:
    print("NO")
    
#5th ex (min)
a=int(input())
b=int(input())
c=int(input())

print(min(a, b, c))

#6th ex (equal numbers)
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print(0)
#7th ex (
