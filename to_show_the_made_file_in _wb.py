import requests
import os
import webbrowser as wb

url="https://www.rcsb.org/"
response=requests.get(url)

with open("rcsb,txt","w") as f:
    print(f.write(response.text))

file_path=os.path.realpath("rcsb.html")
print(file_path)
print(wb.open("file://" +file_path))