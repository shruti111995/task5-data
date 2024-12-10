import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from getbook import extractBook

bookurl="https://books.toscrape.com/"
bookheader={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
bookresp=rq.get(url=bookurl,headers=bookheader)
booksoup=BeautifulSoup(bookresp.content,'html.parser')

#ratings= booksoup.find_all('p', attrs={'class':'star-rating'})

#for r in ratings:
   # print(r.attrs['class'][1])
  # pass
#bookprice= booksoup.find_all('p',attrs={'class':'price_color'})

#for p in bookprice:
  # print(p.text)

#booklist= booksoup.find_all('ul',attrs={'class':"nav nav-list"})

#for  ul in booklist:
   #print(ul.text)

#img = booksoup.find_all('div', attrs = {'class': 'image_container'})

#for div in img:

  # print(img)

booksoup=[extractBook(book) for book in booksoup.find_all('article',{'class':"product_pod"})]

bookdata=pd.DataFrame(booksoup)
bookdata.to_csv('book.csv')