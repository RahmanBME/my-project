#define a funtion
def add(n1,n2):
    return n1+n2
n=84956
m=89653

result=add(n,m)
print(result)

def myfunction(x):
    print("inside myfuntion",x)
    x=10
    print("inside myfunction", x)

x=20
myfunction(x)


def myfunc(y):
    print("y=",y)
    print("x=",x)

x=20
myfunc(x)

#set the default value of the funtion
def myfun(y=10):
    print("y=",y)

x=20
myfun(x)
myfun()


#add the numbers using the funtion
def add_numbers(numbers):
    result=0
    for num in numbers:
        result+=num
    return result
result=add_numbers([1,2,3,4,5,6,7,5,674,6,4,7,5,6,5,6764])
print(result)

#check palindrom
s=str(input("enter your word"))
reverse=s[::-1]
if s==reverse:
    print("palindrom")

else:
    print("it is not palindromic")