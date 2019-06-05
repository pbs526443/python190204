import requests

def con(start):
    url = "https://movie.douban.com/j/chart/top_list?"

    params = {
        "type": "24",
        "interval_id": "100:90",
        "action": "",
        "start": start,
        "limit": "20"
    }

    response = requests.get(url, params=params).json()
    # print(response)

    for i in response:
        print(i["title"], i['rating'][0], i['vote_count'])


if __name__ == '__main__':
    for i in range(10):
        start = i*20
        con(start)