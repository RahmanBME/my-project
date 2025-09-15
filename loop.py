#use of for loop
for i in range (10):
    print("I want to be a great programmer.")


for i in range(5):
    print(i)


result=0
for _ in range(50):
    result=result+1
print(result)


result=0
num=1
for _ in range(50):
    result=result+num
    num=num+1
print(result)

#loop in list
list1=[1,23,63,7,654,252,46,672,35,3]
max_n=list1[0]
for n in list1:
    if n>max_n:
        max_n=n


print(max_n)

# 1 to 100 er summation
result=0
for num in range(100):
    if num%5==0:
        print(num)
        result=result+num

print("the sum is :",result)


result=0
for num in range(5,101, 5):
    print(num)
    result=result+num

print(" the sum is :",result)

#loop in list, lets make a list

list1=list(range(11))
print(list1)


#while loop
i=0
while i <5:
    print(i)
    i+=1


i=5
while i>=0:
    print(i)
    i-=1


#print the multip[lication table\
n=int(input("enter your desiresd numkber:"))
m=1
while m<=10:
    print(n,'x',m,'=',n*m)
    m+=1


#break and continue
while True:
    n=int(input("enter your number:"))
    if n==0:
        break
    print("square of ",n, "is",n*n)



# only for the positive number

while True:
    n=int(input("enter your desired number:"))
    if n<0:
        break
    print("the square of ",n,"is",n*n)
