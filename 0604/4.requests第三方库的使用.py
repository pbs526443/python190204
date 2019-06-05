# urllib的封装
import requests

url = "http://www.baidu.com/s?"
params = {"wd":"笔记本"}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
}

response = requests.get(url,params=params,headers=headers)
# <Response [200]>
print(response)
# <class 'requests.models.Response'>
print(type(response))
# 获取字节数据 相当于 read()
htmlBytes = response.content
# 解码
print(htmlBytes.decode())
