# 模块导入
from urllib import request

# 定义URL
url = "http://www.baidu.com"
# 请求一个URL地址
response = request.urlopen(url)
# 返回对象类型http.client.HttpResponse
print(type(response))
# 读取页面信息并解码
html = response.read().decode()
# 网页bytes信息
print(html)
print(type(html))

str = '今天是个好日子'
strEncode = str.encode()
print(type(strEncode))

# 解码
decodeResult = strEncode.decode()
print(decodeResult)
print(type(decodeResult))
