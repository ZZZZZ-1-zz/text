import requests
from lxml import etree

url = 'http://114.67.246.176:18475/'
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KH' +
    'TML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
session = requests.Session()
response = session.get(url=url, headers=header)
# print(response.status_code)
tree = etree.HTML(response.text)
t = tree.xpath('//div/text()')[0]
t = str(t)
# print(type(t))
t = t.split('=')
# print(t[0])
sum = eval(t[0])
# print(sum)
data = {
    'value': sum,
}
result = session.post(url=url, headers=header, data=data).text
print(result)
