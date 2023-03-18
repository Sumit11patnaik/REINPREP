'''
list1=[]
print(list1,type(list1))
list2=[10,20.45,400,True,"Sumit"]
print(list2,type(list2))
list2.extend([44,555,577])
print(list2,type(list2))
list2.insert(0,3445)
print(list2,type(list2))
list2.insert(3,45)
print(list2,type(list2))
list2.remove(555)
print(list2,type(list2))
list2.pop()
print(list2,type(list2))
del list2[2]
print(list2,type(list2))
'''
'''

def func(str):
    d_count=0
    l_count=0
    for i in str:
        if i.isalpha():
            d_count+=1
        elif i.isdigit():
            l_count+=1
        else:
            continue
    return(d_count,l_count)
print(func("Sumit 11"))
'''

'''
def fun(str):
    if len(str)<2:
        return -1
    else:
        return str[0:2]+str[-2:]
print(fun("Sumit"))
'''
'''

def fun(str):
    
    if len(str)>2:
        if str[-3:]=="ing":
            str += 'ly'
        else:
            str += 'ing'
    return str
print(fun("Sleeping"))
        
   '''
'''
a=int(input())
b=a*2
res=list(map(int,str(a)))
res1=list(map(int,str(b)))
if(sorted(res)==sorted(res1)):
          print("True")
else:
    print("False")
'''
'''
def fun(rama,list1):
    list2=[]
    for i in list1:
        list2.append(dict[i])
    return list2    
        
dict={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
print(fun("merry","christmas"))
'''

a=int(input())
b=int(input())
'''
result=[]
for i in range(a,b+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)
'''
array=[i for i in range(a,b+1)]
print(array)
result=[]
for i in range(len(array)):
    for j in range(i,len(array))):
        result.append(array[i:j+1])
print(result)
        
        
        

