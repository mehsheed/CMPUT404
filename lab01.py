import requests

print(requests.__version__)

r = requests.get("http://google.com")

#print (r.text)

raw = requests.get("https://raw.githubusercontent.com/mehsheed/CMPUT404/main/lab01.py")

print (raw.text)