
a='agalyaravi@gmail.com'
count=0
indexvalue=a.index('@')
index_val=a.index('.')
valid=True
for i in a:
    if i=='@':
        if i.count('@')==1:
            for i in a[indexvalue+1:indexvalue+4]:
                if not i.isalpha():
                    valid=False
        if i=='.':
            if i.count('.')==1:
                for i in a[index_val+1:]:
                    if not i.isalpha():
                        valid=False
if valid:
    print('valid')
else:
    print('not')

                    
                    
                        
#prime num range
'''
start=1
end=20
for num in range(start,end+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
'''
#bday wishes
'''
a=input('enter the date')
date=['23-dec','24-jan','25-may']
name=['sam','jon','don']
email=['sam@3','jon@12','don@3']
for i in range(len(date)):
    if date[i]==a:
        print('today:',date[i],'To:',email[i],'hii',name[i],'bita academy wishes a happy birthday')  
'''
#find missing val in list
'''
a=[4,5,7,8,11,14]
for i in range(min(a),max(a)):
    if i not in a:
        print(i)
'''
'''
a=int(input('enter the num'))
count=0
for i in range(2,230):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count=count+1
        if count==10:
            print(i)
            break
        
        
   '''     
        
        











