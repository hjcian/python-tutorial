from bs4 import BeautifulSoup

HTML = """
<!doctype html>
<html>
    <head>
        <title> Title 1 </title>
    </head>
    <body>
        <h1> Head 1 </h1>
        <a href="https://www.google.com"> This is a Google Site </a>
        <a href="https://example.com"> This is exmaple.com </a>
        <a> 這個元素沒有超連結 </a>
    </body>
</html>
"""

if __name__ == "__main__":

    soup = BeautifulSoup(HTML, 'html.parser')

    print(soup.prettify()) # 排版顯示 HTML 文件
    
    print(soup.title) # 印出 HTML 的 <title>
    print(soup.a)