#phone keypad using dict
'''
keypad={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
key=int(input('key:'))
click=int(input('click:'))
if key==7 or key==9:
    print(keypad[key][click%4-1])
else:
    print(keypad[key][(click%3)-1])
'''
#to check it is secret code within 3 chance
'''
secretno=5
n=int(input('enter the number'))
if n==secretno:
    print('you won')
else:
    print('second chance')
    n2=int(input('enter the number'))
    if n2==secretno:
        print('you won')
    else:
        print('third chance')
        n3=int(input('enter the number'))
        if n3==secretno:
            print('you won')
        else:
            print('not a secretno')
'''
secretno=5
count=0
while count<3:
    n=int(input('enter the number'))
    if n==secretno:
        print('you won')
    else:
        print('try again')
        count=count+1
        
else:
        print('over')






    
