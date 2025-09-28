n="bangladesh!"

#to measure the length use the len():
print(len(n))

print(n[4])
print(n[6])

#slicing (positive slicing)
#print(n[0:6])

#negative slicing
#print(n[6:])
print(n[-11:-5])
#print(n[-6:-11])
print(n[-9:-6])


#string modify
p='Bnagladesh'
print(p.lower())
print(p.upper())

#replace the letter
print(p.replace('a','o'))


#white spacer removing using strip() function

v='     Bangladesh  is my country'

print(v)

#removing
print(v.strip())

print(v.split())

#concatanation

a= 'abdur'
b= 'rahman'
print(a+'   '+b)

#Fromat string


name='Abdur Rahman'

age=25

print("my name is ",name, "and my age is ",age)

#formatting
print(f"my name is {name} and my age is {age}")