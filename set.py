#A set in Python is an unordered, unindexed, and mutable collection of unique items.

s1={"laptop","computer","bedshit"}

print(s1,type(s1))



li=[1,2,3,4,5,456437,54785474536325,2353426,6346347,233]
print(type(li))
s2=set(li)
print(s2)

# we can make the set from the string

A="Bangladesh"

A=set(A)
print(A)

print('a' in A)

# we can run several opertation on the two sets

A={12,3,45436,57654,412423,65457,54214235,47,4573254}
B={2343,643734,234,534,7,547,43523,545,8678452,47,12}

C=A&B
print(C)
C=A|B
print(C)

print(A^B)
print(A-B)