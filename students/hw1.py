import json
import urllib.request as req # built in
import bs4

def getdata(url) :
    #url="http://example.com/"
    with req.urlopen(url) as response:
        data = response.read().decode("utf-8")
    soup = bs4.BeautifulSoup(data, "html.parser")
    a_tags = soup.findAll("a") #用"li"下面print 不能跑,使用"a"可以但會搜到class    

    hrefs = []
    for idx, nextlink in enumerate(a_tags):
        # print(type(nextlink))
        print(idx, nextlink["href"])#問老師為什麼要用[] , 我要的是尋找href標籤
        hrefs.append(nextlink["href"])
    return hrefs

#主程序 抓取多個頁面
url = "https://www.iana.org"
urls = getdata(url) #拿到第二層的url
print("Hello~", urls)

##拿到第三層的url
# count = 0
# while count < 2:
#     urls = getdata(urls)
#     # str: "/aaa/bbb/ccc.htm"
#     if urls[0] != "h":
#         urls = "https://www.iana.org"+urls
#         count += 1
#         print(urls)