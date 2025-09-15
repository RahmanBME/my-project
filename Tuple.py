#A tuple is an ordered, immutable collection of items in Python. In the contrast with the list tuple uses parenthese bracjet
t=(12,23,34,45,56)
print(t)
print(type(t))


t2=1,2,3,4,5,6,7
print(type(t2))
print(t2[3])


#tuple is immutable
tuple=(1,2,3,4,5,6,7,8,9)
print(tuple)


#we can pack sevaeral variable in a tuple

numbers=(912,3,4556,7,65743)

n1,n2,n3,n4,n5=numbers

print(n1)

t=n1,n3
print(t)

print(type(t))

# we can keep manythings in tuple and we can use loop within the lopp

items=(12,3443456,36543,2425,43,[1,2,3,45,6,],("apple","bannanannan"))
for item in items:
    print(item,type(item))

type(items)

