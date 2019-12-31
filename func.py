def add(a,b):
    c=a+b
    print(c)



def sub(a,b):
    c=a-b
    return(c)



def mul(a,b):
    c=a*b
    return(c)
x=10+mul(2,4)
print(x)



def palindrome(string):
    if string==string[::-1]:
        print('palindrome')
    else:
        print('not')
palindrome('madam')

def greeting(name,course,inst='bita'):
    print('hi {},welcome to {},ur course is {}'.format(name,inst,course))
if __name__=='__main__':
    greeting('agal','python')
    add()
    sub()

