import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(40), nullable=False)
class Book(Base):
    __tablename__ = 'book'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(60), unique=True)
    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'{self.title} |'
class Shop(Base):
    __tablename__ = 'shop'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(40), nullable=False)

    def __str__(self):
        return f'{self.name} |'
class Stock(Base):
    __tablename__ = 'stock'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('book.id'), nullable=False)
    id_shop = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('shop.id'), nullable=False)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')
class Sale(Base):
    __tablename__ = 'sale'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    date_sale = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    id_stock = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('stock.id'), nullable=False)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    stock = relationship(Stock, backref='sales')

    def __str__(self):
        return f'{self.price} | {self.date_sale}'
def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)