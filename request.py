#rewuest is the thireds party module

import requests
url="https://www.rcsb.org/"
response=requests.get(url)
print(type(response))
#to check the conditions
print(response.ok)
print(response.status_code)
print(response.reason)

# to get the content

print(response.text)


print(type(response.text))


#now we would like to save the string in a file.


fp=open("test.text","w")
fp.write("This file was created using python")

fp.close()

fp=open("text.txt","w")
print(fp.write("hello"))


fp.close()

#print(fp.write("hello again"))


#lets do the work of the file in another way


with open("text.txt","w") as f:
    print(f.write("Hello,python\n"))

print(f)


print(f.write("hello"))  # in this case when we will exit from this with block then file will autmatically be clsoed




