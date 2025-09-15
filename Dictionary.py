#In Python, a dictionary is a collection of key-value pairs. It allows you to store and retrieve data efficiently using keys, not positions like lists or tuples.

marks={1:34,2:34,3:326}

print(type(marks))

print(marks[2])

#we can also make ab empty key

dt={}
print(type(dict))

dt[1]="one"
print(dt)


# Now we will make a dictionary and e will keep some information about the dicision
bd_division={}
bd_division["Dhaka"]={"district":13,"Upazila":93,"Union":1833}
bd_division["raj"]={"district":14,"Upazila":93,"Union":1833}
bd_division["bari"]={"district":13,"Upazila":93,"Union":1833}
bd_division["khulna"]={"district":13,"Upazila":93,"Union":1833}
bd_division["jassore"]={"district":13,"Upazila":93,"Union":1833}
bd_division["chitagong"]={"district":13,"Upazila":93,"Union":1833}
bd_division["rongpur"]={"district":13,"Upazila":93,"Union":1833}

for division, info in bd_division.items():
    print(f"{division} => district: {info['district']}, Upazila: {info['Upazila']}, Union: {info['Union']}")


divisions=bd_division.keys()
print(divisions)


for division in divisions:
    print("Division:",division)


#to find out the upazila