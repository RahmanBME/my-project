#now lets see how to save the webpage into the file


import requests
url="https://www.rcsb.org/"

response=requests.get(url)

with open("rcsb.html","w") as f:
    print(f.write(response.text))
