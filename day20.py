'''
#read the file in txt doc
f=open('file.txt','r')
print(f.read())
#read the txt doc upto 5 letter
f=open('file.txt','r')
print(f.read(5))

#it  read the txt doc line by line
f=open('file.txt','r')
print(f.readline())

#it  read the txt doc word by word 
f=open('file.txt','r')
for i in f:
    for j in i.split():
        print(j)
        
#write in the txt doc
f=open('file1.txt','w')
f.write('hai hello \n how r you \n ok bye')
f.close()

# append in the txt doc
f=open('file1.txt','a')
f.write('\n what are you doing')
f.close()
#create the file and write in txt doc

f=open('file2.txt','x') 
f.write('\n what are you doing')
f.close()
'''
'''

a=input('user name:')
b=input('pwd:')
f=open('file3.txt','w')
f.write('username:'+a+'pwd:'+b)
f.close()
'''
'''
while True:
    a=input('username:')
   
    if a=='exit':
        break
    b=input('pwd:')
    f=open('file4.txt','a')
    f.write('\n username:'+a+'pwd:'+b)
f.close()
'''
f=open('file5.txt','w')
for i in f:
    for j in i.split():
        if j=='agalya':
            f.write('hello')
f.close()

















