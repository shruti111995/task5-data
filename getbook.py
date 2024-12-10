from utils1.getprice import extractprice
from utils2.getrate import numberconvert

def extractBook(book):
    img = book.find('div', attrs = {'class': 'image_container'}).a.img
    imgData = {
        'src': img.attrs['src'],
        'alt': img.attrs['alt']
    }
    price = extractprice(book)
    rating = book.find('p', attrs={'class': 'star-rating'}).attrs['class'][1]

    title = book.find('h3').a.attrs['title']
    bookData = {
        
        'imgData': imgData,
        'price': price,
        'rating': rating,
        'title':title
    }

    return bookData