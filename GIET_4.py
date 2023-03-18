#Nearest palindrome
'''
import sys
def fun(b):
    if  str(i)==str(i)[i::-1]:
        return i
def func(a):
    for i in range(a+1,sys.maxsize):
        if str(i)==str(i)[i::-1]:
            return i
print(func(99))
print(func(1221))
'''
#make a dict to check the patient
'''
def max_visited(pms,ms):
    max_visit=0
    P=pms.count('P')
    E=pms.count('E')
    O=pms.count('O')
    if P>O and P>E:
        speaciality=ms['P']
    elif E>0:
        speaciality=ms['E']
    else:
        speaciality=ms['O']
    return speaciality
pms=[1,'P',2,'P',3,'O',4,'E']
ms={"P":"Pediatrics","O":"Ortho..","E":"ENT"}
speaciality=max_visited(pms,ms)
print(speaciality)
'''
#to check the similarity btw strings
'''
s1=[]
s2=[]
str1=input()
str2=input()
for i in str1: 
    for j in str2:
        if (i==" "):
            continue
        elif (i.lower==j.lower):
            s1.append(i)
        elif (i.upper==j.upper):
            s2.append(i)
res=[*set(s1)]
res="".join(map(str,res))
print(res)
'''
#OOPs
''' 
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
''' 
'''
class student:
    def __init__(self,id):
        self.id=100

c1.student(200)
print(c1.id)
 '''
'''
class Book:
     def __init__(self):
         self.title=None
my_fav=Book()
my_fav.title="Head first programming"
your_fav=Book()
your_fav.title="Learn Python the hard way "

my_fav.title="Learning Python"

print("My Favorite is",my_fav.title)
print("Your's is",your_fav.title)
'''
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material = material
s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
'''
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material = material
s1=Shoe(1000,"Canvas")
print(id(s1))
  '''
'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material = material
    def __str__(self):
        return "Shoe with price:"+str(self.price)+" and material:"+self.material
    
s1=Shoe(1000,"Canvas")
print(s1)
'''
'''
class fun:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")
fun().purchase()
m1=fun()
print(m1)
'''
'''
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price = None
    def purchase(self):
        if self.brand == 'Apple':
            discount =10
        else:
            discount=5
        self.total_price=self.price - self.price*(discount/100)
        print("Total price of ",self.brand,"mobile is",self.total_price)
    def amount_returned(self):
        return (self.price-self.total_price)
    
mob1=mobile("Apple",2000) 
mob1.purchase()
print(mob1.amount_returned())
'''
'''
class customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
        print("The balance is ",self.__wallet_balance)
    def get_wallet_balance(self):
        return self.__wallet_balance
        
c1=customer(100,"Rama Krishna",24,100)
c1.update_balance(500)
c1.show_balance() 
print(c1.get_wallet_balance())
'''
#Jennifier is python developer
'''
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
    def jit_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length:",dam1.jit_length())
 '''
'''
class Table: 
    def assign_data(self,glass_top,wooden_top):
     self.__glass_top=glass_top
     self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
         self.assign_data(glass_top,wooden_top)
         if(self.__glass_top==True):
             rate=20000
         elif(self.__wooden_top==True):
             rate=30000
         else:
             rate=0
         return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)       
 '''
'''
class table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)
  '''
'''
class table:
    def __init__(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None           
m1=table()
m2=table()
m3=m2
m1=m2
print(id(m1),id(m2),id(m3))
'''
'''
class Wecare:
    def __init__(self,vid,vtype,cost,pre,amount):
        self.__vid=vid
        self.__vtype=vtype
        self.__cost=cost
        self.__pre=pre
        self.__amount=amount
    def vehicle(self):
        if (self.__vtype=='Two Wheeler'):
            amount=(2/100)*self.__cost 
            
        elif(self.__vtype=='Four Wheeler'):
            amount=(6/100)*self.__cost
        
        else:
            print("invalid ")   
        return amount
    def set_(self):
        print(self.__amount)    
    
    def disp(self):
        print("the vehicle details are",self.__vtype)

f1=Wecare(1,"Two Wheeler",40,0,0)
print(f1.vehicle())
f1.disp()
'''
'''
sum=1
a=int(input())
for i in range(1,a+1):
    sum*=i
print(sum)
 '''
'''
class university:
    def __init__(self,s_id,age,marks,c_id):
         self.s_id=s_id
         self.age=age
         self.marks=marks
         self.c_id=c_id
    def valid(self):
        if (self.age>20) and (self.marks>=0 and self.marks<=100):
            return True
        else:
            return False
    def Qua(self):
        if (self.age>20) and (self.marks>=65) and (self.marks<=100):
            return True
        else:
            return False
    def course(self,c_id):
        if(self.marks>=85 and self.marks<=100):
            if(c_id==101):
                fees=25575.0
            if(c_id==102):
                fees=15500.0
            return fees
f1=university(1,21,79,101)
print(f1.valid())
print(f1.Qua())+3
print(f1.course(101))
  '''
#pizza 

class customer:
    def __init__
    
    def valid_quantity(self,p_q):
        if (p_q<5):
            return True
    def pizza_service(self,topping):
        if (topping=="Yes"):
            return True
        else:
            return -1
            
    
    def validate_pizzatype(self,p_t):
        if (p_t=="small"):
            return True
        elif (p_t=="medium"):
            return True
        else:
            return False
    def pizza_cost(self,p_c):
        if self.validate_pizzatype() and self.validate_pizzatype():
            
            
                
                  
       
        
       
    
