'''
chardet第三方库，

用来判断编码的模块

使用chardet.detect()方法，判断网页的编码方式

安装方法：pip install chardet
'''
from urllib import request
import chardet

# 定义URL
url = "http://www.baidu.com"
# 请求一个URL地址
response = request.urlopen(url)
# 读取页面信息
html = response.read()
# 自动获取网页编码
encode = chardet.detect(html)
print(encode)
print(type(encode))
# 拿到网页编码
result = html.decode(encode['encoding'])
print(result)