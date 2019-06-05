from urllib import request,parse
import json

url = "https://movie.douban.com/j/chart/top_list?"

# post的参数
parameter = {
    "type":"11",
    "interval_id":"100:90",
    "action":"",
    "start":"0",
    "limit":"20"
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
for item in jsonRes:
    print(item['title'])