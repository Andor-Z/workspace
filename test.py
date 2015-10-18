import urllib.request  as ur #2中的urllib2
import http.cookiejar  as hc #2中的cookielib
url = input('please enter url:')

cookie = hc.CookieJar()  #声明一个cookjar对象实例来保存cookie
handler = ur.HTTPCookieProcessor(cookie)  #利用urllib.request中的HTTPCookieProcessor来创建cookie处理器
opener = ur.build_opener(handler)
response = opener.open(url)
for item in cookie:
	print('Name = ' + item.name)
	print('Value = ' + item.values)
