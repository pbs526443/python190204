import requests

url = 'http://ip.27399.com/'
proxies = {"http":"1.198.73.157:9999"}

html = requests.get(url,proxies=proxies).content.decode()
print(html)