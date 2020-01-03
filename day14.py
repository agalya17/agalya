#convert string into int
'''
a=input('enter :').split()
for i in range(len(a)):
    a[i]=inta[i]
print(a)
'''
#to print 0 no of times by the given input
'''
a=int(input('enter the value'))
b=[]
for i in range(a):
    b.append(0)
print(b)
'''
#list comprihension
'''
x=int(input('enter :'))
a=[0 for i in range(x)]
print(a)
'''
'''
x=int(input('enter :'))
a=[i for i in range(x) if i%3==0 or i%5==0]
print(a)
'''
'''
x=int(input('enter:'))
a=[int(i) for i in input('enter:').split()]
print(a)
'''
# add the value by using pointer func
def add(*a):
    sum1=0
    for i in a:
        sum1=sum1+i
    print(sum1)
add(10,20,30)
