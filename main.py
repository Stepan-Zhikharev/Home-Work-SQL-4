import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = ''
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

def search_author():
    name_author = input('Введите фамилию искомого автора: ')
    result = session.query(Book, Shop, Sale, Publisher).join(Book).join(Stock).join(Sale).join(Shop).filter(Publisher.name == name_author)
    for x in result:
        print(x.Book, x.Shop, x.Sale)

session.close()