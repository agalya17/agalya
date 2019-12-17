#greeting
'''
name=input('enter ur name')
inst=input('enter ur inst')
course=input('enter ur course')
print('hi',name,'welcome to',inst,'ur course is',course)
print('hi '+name+' welcome to '+inst+' ur course is '+course)
print('hi {} welcome to {} ur course is {}'.format(name,inst,course))
'''
#add input
'''
a=int(input('enter a number'))
b=int(input('enter b number'))
c=a+b
print('sum of two number is:',c)
'''

#list
'''
a='abcd'
b=int(input('enter the number:'))
print(a[b:]+a[:b])
'''
#if else(age)
'''
age=int(input('enter the age'))
if(age<10):
    print('child')
if(10<age<25):
    if(age<18):
        print('school')
    else:
        print('college')
if(25<age<50):
    if(age<35):
        print('employee')
    elif(age<45):
        print('manager')
    else:
        print('senior manager')
if(50<age<60):
    print('vrs')
elif(age>60):
    print('senior citizon')
'''
#leap or not
'''
year=int(input('enter the year'))
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print('leap')
        else:
            print('not')
    else:
        print('leap')
else:
    print('not leap')
'''
#evaluate
'''
a='8 plus 2'
a=a.replace('plus','+')
print(eval(a))
'''
#for loop
'''
b=10
for i in range(0,b):
    print(i,end=' ')      #end represent space and join between i value
print('')
for i in range(b-1,-1,-1):
    print(i,end=' ')
'''
'''
a=[10,20,30,40,50,60,80]
for i in a:
    print(i)
for i in range(5):
    print(a[i])
'''
#nested for loop
'''
for i in range(5):
    for j in range(5):
        print(i,j,end='|',sep='-') # sep represent the seperate function it seperate the value
'''
#length of a
'''
a=[2,3,2,9,3,3,1,6]
count=0
for i in a:
    count=count+1
print(count)
'''
#sum of a
'''
a=[2,3,2,9,3,3,1,6]
sum=0
for i in a:
    sum=sum+i
print(sum1)
'''
#count the single value
'''
a=[2,3,2,9,3,3,1,6]
b=int(input('enter b value'))
count=0
for i in a:
    if(i==b):
        count=count+1
print(count)
'''
'''
a=[2,'str',9,3,3,1,6]
sum=0
for i in a:
    if(type(i)==int):
        sum=sum+i
print(sum)
'''
#maximum value
'''
a=[2,3,2,9,3,3,1,6]
max_val=a[0]
for i in range(0,8):
    if a[i]>max_val:
        max_val=a[i]
print(max_val)
'''
#minimum value
'''
a=[2,3,2,9,3,3,1,6]
min_val=a[0]
for i in range(0,8):
    if a[i]<min_val:
        min_val=a[i]
print(min_val)
'''
#duplicate
a=[2,3,2,9,3,3,1,6]
dup=a[0]
for i in range(0,8):
    if a[i]==dup:
        





















































