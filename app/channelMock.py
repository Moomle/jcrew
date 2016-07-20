import requests

url = "http://supergw-d8419.alipay.net/OPENAUTO01/OPENAUTO010001.htm"

entity = '<M name="message"><F name="applyId">123456啊啊7</F><F name="content">{key:value}</F><F name="applyDownUrl">测试sfsfile.zip</F><F name="respCode">00</F><F name="outOrderNo">0011111</F><F name="instChannelApi">abc901</F><F name="respMsg">测试</F></M>'

r = requests.post(url, data=entity)
print r.text