import requests as re
img_url="https://ahmadullah.info/site/contents/cropped/1190x512x1x100xffffffx0/whatsapp-image-2024-12-03-at-10.39.11-am.jpeg/"
r= re.get(img_url)
with open("ahmadullahinfo.png","wb") as f:
    print(f.write(r.content))
