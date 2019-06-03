from urllib import request

url = "https://weibo.com/"

# 构造字典 修改请求头信息
headers = {
    "Cookie":"Ugrow-G0=1ac418838b431e81ff2d99457147068c; SUB=_2A25x8XKUDeRhGeRK6VUU8y3NyTuIHXVSh-NcrDV8PUJbmtBeLXHgkW9NU00aLXQnJDyJc-UkcMeam9fyk59SV9SF; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QWu7oYD6c0IHq6WD3n9_05JpX5K2hUgL.FozXeoMfe0epeoM2dJLoI0.LxKnL122LBo2LxK.LBKeL1KnLxKMLBo-LB-HydJBLxKqLBKzLBKqLxK.L1-2L12qLxK-LB.qL1het; login_sid_t=2acd0ea2dbbb398c0c9a177181d48bf2; cross_origin_proto=SSL; YF-V5-G0=4e19e5a0c5563f06026c6591dbc8029f; WBStorage=ce875ff0f41a253d|undefined; _s_tentry=passport.weibo.com; wb_view_log=1366*7681; Apache=7556220665995.662.1559560699291; SINAGLOBAL=7556220665995.662.1559560699291; ULV=1559560699295:1:1:1:7556220665995.662.1559560699291:; crossidccode=CODE-gz-1HxL0H-2gmSSN-FAeVycbuF4QsjJL09f9a0; UOR=,,graph.qq.com; appkey=; SCF=AntCj5nuWM58vHx6xvQLyHsQ1BMDuDVzHLOM1CTOln74bF0RVpa3_iu9j0u_4YsA6CpFies8RfKPYyrkk1vgGuU.; SUHB=0D-EID23LY9mhh; SSOLoginState=1559560899; un=15108948903; wvr=6; YF-Page-G0=02467fca7cf40a590c28b8459d93fb95|1559560912|1559560912; wb_view_log_2427533127=1366*7681; webim_unReadCount=%7B%22time%22%3A1559560924123%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D",
}

# 通过urllib的Request对象替换身份信息
req = request.Request(url,headers=headers)

htmlBytes = request.urlopen(req).read().decode()
print(htmlBytes)