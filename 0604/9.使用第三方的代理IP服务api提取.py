import requests

response = requests.get("http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=302db6bce9fe4098b07847c5a384c544&count=3&expiryDate=0&format=1&newLine=2")
ipInfo = response.json()
ipList = ipInfo['msg']

print(ipList)

for i in ipList:
    Ip = i['ip'] + i['port']
    print(Ip)