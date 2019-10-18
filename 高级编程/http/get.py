
import requests


r = requests.get('http://localhost:8081/v1/status')
r.close()
print(r.text)


#参数
#header
# cookie
# 超时
d = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'my-app/0.0.1'}
cookies = {'cookies_are': 'working'}
timeout = 5
r = requests.get('http://localhost:8081/v1/status', params=d, headers=headers, cookies=cookies, timeout=timeout)
print(r.url)
print(r.text)
print(r.headers)
print(r.cookies)
print(r.json())
print(r.status_code)