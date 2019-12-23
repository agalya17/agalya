#to sep username
'''
a=input('enter the emailid')
for i in a:
    if i=='@':
        break
    else:
        print(i,end='')
'''
#to sep host
'''
a=input('enter the host')
for i in a[(a.index('@')):(a.index('.'))]:
    print(i,end='')
'''
#leap year
'''
yr=int(input('enter the year'))
valid=False
if yr%4==0:
    valid=True
    if yr%100==0:
        valid=False
        if yr%400==0:
            valid=True
if valid:
    print('leap')
else:
    print('not leap')
'''
#passwrd validation
a=input('enter your password')
valid=True
if len(a)<6:
    print('password should be atleast 6 character')
    valid=False
if len(a)>8:
    print(' passwrd shold be greater than 8 cahracter')
    valid=False
if valid:
    print('valid')
else:
    print('not')





















