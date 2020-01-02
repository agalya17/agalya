#sorting the num without using sort method and using algorithm

a=[4,2,4,9,6,3,5]
for i in range(len(a)):
    min_val=min(a[i:])
    min_index=a.index(min_val)
    a[i],a[min_index]=a[min_index],a[i]
print(a)

    



    
    
