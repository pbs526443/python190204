from urllib import request,parse
import json

# 有道翻译url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# post的参数
parameter = {
    "i":"中国",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15577378774445",
    "sign":"44163461e046a197ba4681e91aa49524",
    "ts":"1557737877444",
    "bv":"e2a78ed30c66e16a857c5b6486a1d326",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME",
}

data = parse.urlencode(parameter).encode("utf-8")

res = request.urlopen(url,data=data).read().decode()
print(res)
# <class 'str'>
print(type(res))
# 拿到的是json字符串，把字符串转化为Python对象dict，list
jsonRes = json.loads(res)
print(jsonRes)
# 按索引取结果
print(jsonRes["translateResult"][0][0]['tgt'])