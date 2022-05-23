import requests

url = 'http://apis.data.go.kr/B552895/openapi/service/OrgPriceExaminService/getExaminPriceList'
params ={'serviceKey' : '서비스키' }

response = requests.get(url, params=params)
print(response.content)