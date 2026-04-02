import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送GET请求
response = requests.get(url=target_url)

# 输出响应内容
# print(response.text)

# 解析HTML内容，将其转换为一个HTML树对象
document = html.fromstring(response.text)

# 解析表头
th_list = document.xpath('//table[@id="top20"]/thead/tr/th/text()')
print(th_list)

# 解析表格内容
tr_list = document.xpath('//table[@id="top20"]/tbody/tr')
td_list = []
for tr in tr_list:
    td_list.append(tr.xpath('./td/text()'))
print(td_list)

