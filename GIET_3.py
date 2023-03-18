'''
a=int(input())
b=int(input())
'''
'''
result=[]
for i in range(a,b+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)
'''
'''
array=[i for i in range(a,b+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1]for i in range(i,len(array)) for j in range(i,len(array))]#list comprehension
print(result)
c=0
for i in result:
    if sum(i)%2!=0:
        c+=1
print(result)
'''
'''
result=[]
for i in range(15):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(15)])
'''
'''
res=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for  i in mat:
    res1=[]
    for j in (i):
        if (j%2==0):
            res1.append(j**3)
        else:
            res1.append(j**2)
    res.append(res1)
print(res)
print([j**2 if j%2!=0 else j**3 for j in i for i in mat])
'''
'''
mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
res=[]
for i in list_b:
    res.append((i,mylist.index(i)))
print(res)
print([(i,mylist.index(i)) for i in list_b])
res1=dict([(i,mylist.index(i)) for i in list_b])
print(res1)
'''
'''
sen=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakhs diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stop=['for','a','of','the','and','to','in','on','with']
result=[]
for s in sen:
    row=[]
    for word  in s.split():
        if word not in stop:
            row.append(word)
    result.append(row)


print([[word for word in s.split() if word not in stop]for s in sen])
'''
'''
n=0
num=[3,2,6,5,1,4,8,9]
for i in num:
    if(i==5):
        a=n.index(i)
    elif (i==8):
        b=n.index(i)
res=num[a:b+1]
del n[a:b+1]
print(num)
print(res)
for i in num:
    sum+=1
print(sum)
a="".join(map(str,res))
r=int(a)
r=sum+r
print(r)
'''
'''
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=stt(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))
'''

    
    

        
    
       
        
    
