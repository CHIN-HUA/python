#抓取ptt電影版網頁原始嗎 (HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

#建立一個Reqest物件, 附加 Reqest Headers 的資訊
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#解析原始嗎，取得每篇文章標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title") #尋找 class="title" 的 div 標籤
for title in titles:
    if title.a != None: #如國標題有 a 標籤 (沒有被刪除). 印出來
        print(title.a.string)