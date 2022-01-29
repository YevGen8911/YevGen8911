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
