import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

print(sqlalchemy.__version__ )
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), nullable = False)
    address_id = Column(Integer, ForeignKey('address.id'))

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "[User] name: {} {}".format(self.first_name, self.last_name)


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(50))
    state = Column(String(50))
    city = Column(String(50))
    postal_code = Column(String(50))
    country = Column(String(50))

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def __repr__(self):
        return "[Address] {} {} {} {} {} {}".format(self.id, self.street
                                    , self.city, self.postal_code, self.state, self.country)


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    tax_id = Column(String(50))
    email = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship("Address")

    def __repr__(self):
        return "[Account] name: {}".format(self.name)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    family = Column(String(50))
    list_price = Column(Float)
    inventory = Column(Integer)
    tax_rate = Column(Float)

    def __repr__(self):
        return "[Product] name: {}".format(self.name)


class InvoiceStatus(enum.Enum):
    Submitted = 1
    ClosedCancelled = 2
    ClosedPaid = 3


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=False), default=func.now())
    account_id = Column(Integer, ForeignKey('account.id'))
    status = Column(Enum(InvoiceStatus), nullable=False)
    total_tax = Column(Float)
    total_price = Column(Float)
    grand_total = Column(Float)

    account = relationship("Account")

    def __repr__(self):
        return "[Invoice] account name: {}".format(self.account.name)


class InvoiceLineItem(Base):
    __tablename__ = "invoice_line_item"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    list_price = Column(Float, nullable=False)
    tax_rate = Column(Float)

    invoice = relationship("Invoice")
    product = relationship("Product")

    @property
    def total_price(self):
        return self.quantity * self.list_price

    @property
    def tax_amount(self):
        return self.list_price * self.quantity * self.tax_rate




