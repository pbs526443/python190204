import requests

# response = requests.get("http://www.baidu.com")
# # 获取cookies信息
# cookies = response.cookies
# print(cookies)
# print(type(cookies))
# print(cookies.get_dict())

req = requests.session()
# 人人登录的action地址
url = "http://www.renren.com/PLogin.do"
# form的name属性
data = {
    "email":"15108948903",
    "password":"526443"
}

html = req.post(url,data=data).content.decode()
print(html)

# 保持登录状态 如果登录成功 会访问个人主页 不成功则访问登录注册页面
loginOK = req.get("http://www.renren.com/410043129/profile").content.decode()
print(loginOK)