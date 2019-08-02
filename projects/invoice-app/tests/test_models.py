import unittest
from models import *


class ModelsTests(unittest.TestCase):

    def setUp(self) -> None:
        engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        from sqlalchemy.orm import sessionmaker
        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        self.session = session_maker()

    def test_model_integrity(self):
        session = self.session

        address = Address(street = "100 Main", postal_code = "12345"
                          , state = "KA", city = "Bangalore", country="IN")
        session.add(address)
        session.flush()
        print(address)

        user = User(first_name = "Ed", last_name = "Sherin"
                    , email = "ed@sample.com", address_id= address.id)
        session.add(user)
        session.flush()
        print(user)
        self.assertTrue(user.id == 1)

        product = Product(name = "Galaxy Phone", family = "Mobile"
                          , list_price = 1000.0, inventory = 100, tax_rate = 18.0)
        session.add(product)
        session.flush()
        print(product)
        self.assertTrue(product.id == 1)

        account = Account(name="Samsung", email = "info@samsung.com"
                          , tax_id = "123abc", address_id = address.id)
        session.add(account)
        session.flush()
        print(account)
        self.assertTrue(account.id == 1)

        invoice = Invoice(account_id = account.id, status = "Submitted")
        session.add(invoice)
        session.flush()
        print(invoice)
        self.assertTrue(invoice.id == 1)

        invoice_line_item = InvoiceLineItem(invoice_id = 1
                                    , product_id = 1, list_price = 1200.0, quantity = 1)
        session.add(invoice_line_item)
        session.flush()
        print(invoice_line_item)
        self.assertTrue(invoice_line_item.id == 1)


        for row in session.query(Address).all():
            print(row)
        for row in session.query(User).all():
            print(row)
        for row in session.query(Account).all():
            print(row)
        for row in session.query(Product).all():
            print(row)
        for row in session.query(Invoice).all():
            print(row)
        for row in session.query(InvoiceLineItem).all():
            print(row)