import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = ''
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_shops(id_or_name):
    request = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop).\
        join(Stock).join(Book).join(Publisher).join(Sale)
    if id_or_name.isdigit():
        result = request.filter(Publisher.id == id_or_name)
    else:
        result = request.filter(Publisher.name == id_or_name)
    for book, shop, price, date in result:
        print(f"{book: <40} | {shop: <10} | {price: <8} | {date.strftime('%d-%m-%Y')}")

session.close()

if __name__ == "__mane__":
    enter_data = input('Введите имя или id автора: ')
    get_shops(enter_data)