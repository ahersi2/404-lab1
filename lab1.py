import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)
a = requests.get("https://raw.githubusercontent.com/ahersi2/404-lab1/master/lab1.py")
print(a.text)
