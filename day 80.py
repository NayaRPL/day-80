# menggunakan jenis data list
def sequentialsearch(alist, value):
    pos=0
    found=False
    for pos in range (len(alist)) :
        if alist[pos]== value:
            found=True
            print(found)
            break
        else:
            return found
data=[3,7,8,9,4,3]
nilai=sequentialsearch(data,3)
print(nilai)
# menggunakan jenis data tupel        
def sequentialsearch(alist, value):
    pos=0
    found=False
    while pos < (len(alist)) :
        if alist[pos]== value:
            found=True
            print(found)
        else:
            return found
        pos +=1
data=(3,7,8,9,4,3)
nilai=sequentialsearch(data,4)
print(nilai)
           