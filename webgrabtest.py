import urllib.request

#抓取一個網頁的原始碼
web = urllib.request.urlopen(" https://www.google.com.tw/ ")
content = web.read()
print(content)
