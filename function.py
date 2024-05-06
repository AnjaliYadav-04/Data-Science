'''
python function:
Python Functions is a block of statements that return the specific task.
we can do the function calls to reuse code contained in it over and over again.


types of function:
1.)Built-in library function: These are Standard functions in Python that are available to use.
2.)User-defined function: We can create our own functions based on our requirements.


'''
#exaples:
def test():
  pass



def test1():
  print("hello")
test1()
print(test1())


def test3():
  return "hello"
test3()+"python"
print(test3()+"python")



def tes5():#parameterless function
  a=3*9+5
  return a
tes5()
print(tes5())



def test6(a,d):
  c=a+d
  return c
test6("ansh","  anshu")
print(test6("ansh","  anshu"))
test6([1,2,3,"hello"],[2,4,5,4.5])
print(test6([1,2,3,"hello"],[2,4,5,4.5]))
test6(d="  hello",a=" hiii")
print(test6(d="  hello",a=" hiii"))


#crete a function taking list as a input and print only number from that list
l1=[1,1,2,1.2,6,7,"hi","hello",[1,3,2,2]]
def func(l1):
  l2=[]
  for i in l1:
    if type(i)==int or type(i)==float:
      l2.append(i)
  return l2
func(l1)
print(func(l1))



#crete a function taking list as a input and print only number from that list and also from the inner list
list11=[1,1,2,1.2,6,7,"hi","hello",[1,3,2,2],["harsg",2,3.3,0.9,True,23]]
def funct2(b):
  #create an empty list 
  n=[]
  for i in b:
    if type(i)==list:
      for j in i:
        if type(j)==int or type(j)==float:
          n.append(j)
    else:
      if type(i)== int or type(i)==float:
        n.append(i)
  return n
funct2(list11)
print(funct2(list11))


#function with "n" number of arguments
def  test23(*args):
  return args
test23(1,2,3,[12,34])
print(test23(1,2,3,[12,34]))


#another method
def func(*args,a):
  return args,a
func(1,3,4.4,"hello",(1,3,3,3.3,4),a="hiiii")
print(func(1,3,4.4,"hello",(1,3,3,3.3,4),a="hiiii") )    


def test5(**kwargs):
  return kwargs #**kwargs return a dictionary with key value pair
test5()
type(test5())
test5(a=34,b=90,c=78,d=("sudh",56,"hello"))



#function generator:
def fibonaci(n):
  a,b=0,1
  for i in range(n):
    yield a
    a,b=b,a+b
fibonaci(5)#it will return a generator object

for i in fibonaci(5):
  print("fibbonacci series are:",i)


'''
The* Yield **keyword in Python is similar to a return statement used for
returning values or objects in Python. However, there is a slight difference.
*The yield statement returns a generator object to the one who calls the
function which contains yield, instead of simply returning a

[ ]


'''





#
  
