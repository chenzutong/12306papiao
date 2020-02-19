import requests
proxy = {"http":"157.255.144.77:80"}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}
url = "https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=2020-02-26&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT"
response = requests.get(url, headers=header, proxies=proxy)
print(response.url)
# result = response.json()
# result = result["data"]["result"]
# print(result)