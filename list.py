list=["afganistan","bangladesh","pakistan", "nepal","bhutan"]
print(list)
list.append("india")
print(list)

list.sort()
print(list)
list.reverse()
print(list)

list.insert(2,"maldeev")
print(list)
item="india"
if item in list:
    list.remove(item)
else:
    print("india is not in list")


#list comprehention
list1=[1,2,3,4,5,6,7,78]
new_list=[]
for x in list1:
    new_list.append(2*x)

print(new_list)


#NESTED LIST


list=[22354,6,34623,2,[3456436,546,62,214,56],(2335,32463,45743,412)]
print(list,type(list))
for x in list:
    print(x, type(x))


