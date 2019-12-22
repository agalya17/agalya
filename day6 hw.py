#equal or not
'''
a=[10,20,30]
b=[10,20,30]
for i in range(len(a)):
    if a[i]==b[i]:
        print('yes')
    else:
        print('not')
'''
#factorial(5*4*3*2*1)
'''
a=int(input('enter the value'))
fact=1
for i in range(1,a+1,):
        fact=fact*i
print(fact)
'''
#factorial(reverse1*2*3*4*5))
'''
a=int(input('enter the value'))
fact=1
for i in range(a,0,-1):
        fact=fact*i
print(fact)
'''
#fibanacci
'''
a=int(input('enter the a value'))
b=int(input('enter the b value'))
for i in range(0,7):
    c=a+b
    a=b
    b=c
    print(c)
'''
#prime number
'''a=int(input('enter the a value'))
for i in range(2,a):
    if a%i==0:
      print(' not prime')
    else:
        print('prime')
        break
'''
#seperate digit,alpha
'''
a='abc$123$#92fg'
for i in a:
    if i.isdigit():
        print(i,end=' ')
print()
for i in a:
    if i.isalpha():
        print(i,end=' ')
print()
for i in a:
    if not i.isalnum():
        print(i,end=' ')
'''

    
#anagram
'''
a=list('listen')
b=list('silent')
a.sort()
b.sort()

for i in range(len(a)):
    if a[i]==b[i]:
        print('yes')
    else:
        print('not')
'''





















