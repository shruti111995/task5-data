import re

def extractprice(booksoup):
    price=booksoup.find('p',attrs={'class':'price_color'}).text
    floatprice=re.sub(r'[^\d.]','',price)

    return float(floatprice)