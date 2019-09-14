import requests
url='http://0.0.0.0:5000'
resp = requests.get(url)
if resp.status_code == 200:
    print ("success")
#print(resp.text)

