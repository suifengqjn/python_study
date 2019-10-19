import requests
import json

# Content-Type字段来获知请求中的消息主体是用何种方式进行编码，再对消息主体进行解析。具体的编码方式包括：
#
# application/x-www-form-urlencoded
# 最常见post提交数据的方式，以form表单形式提交数据。
# application/json
# 以json串提交数据。
# multipart/form-data


# form 形式发送post
url = 'http://httpbin.org/post'
d = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=d)
print(r.text)



# json 形式发送post

url = 'http://httpbin.org/post'
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
r = requests.post(url, data=s)
print(r.text)


# 以multipart形式发送post请求
url = 'http://httpbin.org/post'
files = {'file': open('report.txt', 'rb')}
r = requests.post(url, files=files)