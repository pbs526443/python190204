from urllib import request,parse

url = "https://tieba.baidu.com/f?"
parameters = {
    "kw":"景品",
    "ie":"utf-8",
    "pn":50,
}
params = parse.urlencode(parameters)
url = url + params

# 构建一个字典传入一个代理地址
proxy = {"http":"58.54.222.204:3128"}
# 传递代理地址
proxyHandler = request.ProxyHandler(proxy)
#构造urllib要求的urlopener打开器
opener = request.build_opener(proxyHandler)
# 进行安装
request.install_opener(opener)

req = request.Request(url)
htmlBytes = request.urlopen(req).read()
print(htmlBytes.decode())
with open('第'+str(50/50+1)+'页.html',"wb") as f:
    f.write(htmlBytes)