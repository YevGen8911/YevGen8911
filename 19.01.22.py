#1st practice
print('What is your name?')
name=input()
print('Nice to meet you '+name+'!')

#2nd practice
a=int(input())
b=int(input())
c=int(input())
print(a+b+c)

#3rd practice (rectangle area)
b=int(input())
h=int(input())
print(b*h/2)

#4th practice (apples for kids)
n=int(input())
k=int(input())
print(k//n)
print(k%n)

#5th practice (electronic watch)
n=int(input())
hours=n//60
days=hours//24
time=hours-days*24
minutes=n%60
print(time)
print(minutes)

#6th practice (hello, Harry!)
print('Type your name here: ')
name=input()
print('Hello, '+name+'!')

#7th practice (next and previous)
num=int(input())
follow=int(num+1)
prev=int(num-1)
print('The next number for the number '+str(num)+' is '+str(follow)+'.')
print('The previous number for the number '+str(num)+' is '+str(prev)+'.')

#8th practice (desks for students)
a=int(input())
b=int(input())
c=int(input())
desk_a=a//2+a%2
desk_b=b//2+b%2
desk_c=c//2+c%2
print(desk_a+desk_b+desk_c)

#9th practice (lace length)
a=int(input())
b=int(input())
l=int(input())
N=int(input())
print(a*(2*N-1)+2*l+b*(2*N-2))
