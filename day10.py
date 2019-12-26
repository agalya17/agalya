#largest palidrom number between range
'''
max_val=0
for i in range(1,100):
    for j in range(1,100):
        c=i*j
        d=str(c)
        if(d==str(c)[::-1]):
            if c>max_val:
                max_val=c
                x,y=i,j
print(max_val,x,y)
'''
#replace vowels with someother
'''
a=['a','e','i','o','u']
b='bita'
for i in b:
    if i in a:
        b=b.replace(i,chr(ord(i)+2))
print(b)
'''
#bracket equal or not
bracket=input('enter the bracket')
a=['(','[','{']
b=[')',']','}']
count=-1
for i in range(len(bracket)//2):
    if b[a.index(bracket[i])]!=bracket[count]:
        count=count-1
        print('invalid')
        break
else:
    print('valid')
        

        
        
        
        
      
