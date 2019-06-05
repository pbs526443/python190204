from urllib import request,parse

url = "http://www.baidu.com/s?"
paraeters = {
    "wd":"端午节"
}
# 把字典序列转换成url参数格式
params = parse.urlencode(paraeters)
# get方式添加参数 核心拼接字符串
url = url + params

print(url)

# 请求结果
html = request.urlopen(url).read().decode()

print(html)