#end of lessons
a=int(input())
l=45
br1=5
br2=15
if a%2==0:
    timeh=((a*l)+((a//2)-1)*br2+(a//2)*br1)//60
    timem=((a*l)+((a//2)-1)*br2+(a//2)*br1)%60
    print(9+timeh)
    print(0+timem)
else:
    timeh=((a*l)+(a//2)*br2+(a//2)*br1)//60
    timem=((a*l)+(a//2)*br2+(a//2)*br1)%60
    print(9+timeh)
    print(0+timem)

#snail route
h=int(input())
a=int(input())
b=int(input())
import math
x=math.ceil((h-a)/(a-b))+1
print(x)

#hourArrowAngle
H=int(input())
M=int(input())
S=int(input())
sec=360/(60*12*60)
print((H*3600+M*60+S)*sec)

#minutesArrowAngle
a=float(input())
sec=360/(60*12*60)
q_sec=a/sec
hours=q_sec%3600
angle=360*hours/3600
print(angle)

#whatTimeIs
a=float(input())
sec=360/(60*12*60)
q_sec=a/sec
H=int(q_sec//3600)
M=int((q_sec%3600)//60)
S=int((q_sec%3600)%60)
print(H, M, S)

#bankIncom
P=int(input())
X=int(input())
Y=int(input())
coins=X*100+Y
profit=coins+coins*P/100
Xnew=int(profit//100)
Ynew=int(profit%100)
print(Xnew, Ynew)

#ladder
n=int(input())
for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, sep=" ", end=" ")
    print()
#standartnoe otklonenie
from math import sqrt
x=int(input())
s=0
sum_x=0
sum_x_sq=0
n=0
otkl=0
while x!=0:
    sum_x+=x
    sum_x_sq+=x**2
    x=int(input())
    n+=1
result=(sum_x_sq-(sum_x**2/n))/(n-1)
print(sum_x_sq)
print(sum_x**2/n)
print(sqrt(result))
