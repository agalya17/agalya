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
