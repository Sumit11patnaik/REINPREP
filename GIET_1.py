'''a = int(input("Read a number"))
b= int(input("Read a number"))
res=a*b

if (res%3==0 and res%5==0):
    print("Multiple by both")
elif (res%5==0):
    print("Multiple by 5")
elif (res%3==0):
    print("Multiple by 3")
else:
    print("Invalid number")
'''


'''
for i in range(1,101,2):
        print(i,end=' ')
for i in range(2,101,2):
        print(i,end=' ')
   '''
'''
print("ODD")
for i in range(99,1,-2):
        print(i,end=' ')
print("\nEVEN")
for i in range(100,0,-2):
        print(i,end=' ')
'''

'''
for i in range(0,100):
    print(i,end =" ")
    if (i==60):
        break
else:
    print("ELse")
'''
'''
for i in range(0,100):
    if (i==60):
        pass
    print(i,end =" ")
'''
'''
def fun(x,y):
    print("num1=",x,"num2=",y)
fun(2,4)
'''
'''
def fun(x,y):
    num3=x+y
    return num3
print("Values returned ",fun(x,y))
fun(10,30)
'''
'''
def function(num1,num2):
    num3=float(num1)+num2
    return num3
print("Values returned",function('10',40.5))
'''
#categories of function
#positional arguement
'''
def funtion(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=","num4=",num4)
funtion(10,20,30,40)
funtion(100,"200",300,400)
'''
'''
#Keyword arguements
def function(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=","num4=",num4)
function(num4=10,num1=20,num2=30,num3=40)
'''

'''
def function(name,rollno,branch,college_name="Giet"):
    print(name,rollno,branch,college_name)
function("Sumit","003","CST","GIET")
function("Srinath",9,"CST","GIET")
function("Amruta",91,"CSE","GIET")
function("Harsha",328,"CSE","GIET")
'''
'''
def function(*var):
    for i in var:
        print(i,end=" ")
function(10,20)
print()
function(10,20,30,40)
print()
function(10,20,30,40,50,60)
print()
'''
'''
def function(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(function(10,20))
print(function(50,50))
'''
'''
num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
else:
    print(num1*num2*num3)
'''
'''

def currency(AmountINR,curr):
    if curr=="euro":
        print(AmountINR*0.01417)
    elif curr=="Pound":
        print(AmountINR*0.100)
    elif curr=="B dollar":
        print(AmountINR*0.2140)
    elif curr=="A dollar":
        print(AmountINR*0.2027)
    else:
        print("Invalid")
curr=input()
AmountINR=input()
print(fun(AmountINR,curr))
'''
'''
a=37550.0
c=1/3*37550.0
na=int(input())
nc=int(input())

sum=(na*a)+(c*nc)
sum1=sum*0.07
sum2=sum+sum1
sum2=sum2*0.09
print(sum2)
'''

sum=int(input())
oav=int(input())
fav=int(input())
fa=int(sum/5)
oa=int(sum%5)
def fun():
    if(fav>=fa):
        return True
    elif(oav>=oa):
        return True
    else:
        print(-1)
print(fa,oa)
    























































































































