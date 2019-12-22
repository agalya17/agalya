'''
started=0
stopped=1
while True:
    a=input('enter the string').lower()
    if a=='start':
        if started==1:
            print(' car already started')
        else:
            print('car started')
            started=1
    elif a=='stop':
        if stopped==0:
            print('car is already stopped')
        else:
            print('car stopped')
            stopped=0
    elif a=='help':
         print(''start-----start the car
stop----stop the car
help---enter the help')
    elif a=='exit':
            break
    else:
        print('not understand')

'''
#covert kg to pound and pound to kg
'''
name=input('enter the name')
weight=float(input('enter your weight'))
a=input('enter kg or lbs')
if a=='kg':
    ans=weight*float(2.2046)
    print('hai',name,'your weight in pound',ans)
if a=='lbs':
    ans=weight/float(2.2046)
    print('hai',name,'your weight in kg',ans)
'''
#salary goods
'''
salary=int(input('enter your salary'))
goods=100000
if salary>=50000:
    ans=10/100*goods
    print(ans)
if salary<50000:
    ans=50/100*goods
    print(ans)
''' 




























