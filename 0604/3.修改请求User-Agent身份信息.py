from urllib import request

url = "http://www.useragentstring.com/"
# 构造字典 修改请求头信息
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
}
# 通过urllib的Request对象替换身份信息
req = request.Request(url,headers=headers)

htmlBytes = request.urlopen(req).read()
print(htmlBytes)