import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?query=%EA%BF%88%ED%95%B4%EB%AA%BD&nso=&where=blog&sm=tab_viw'
plusUrl = (input('검색어를 입력하세요:') + '꿈해몽')
soup = BeautifulSoup(baseUrl, 'html.parser')

titles = soup.find_all(class_='sh_blog_title')

comments = soup.find_all(class_='sh_blog_passage')

titles = soup.find_all(class_='sh_blog_title')
comments = soup.find_all(class_='sh_blog_passage')
images = soup.find_all(class_='sh_blog_thumbnail')
days = soup.find_all(class_='txt_inline')

if len(titles) == len(comments) and len(comments) == len(images) and len(images) == len(days):
    for i in range(len(titles)):
        title = titles[i]
        comment = comments[i]
        image = images[i]
        day = days[i]
