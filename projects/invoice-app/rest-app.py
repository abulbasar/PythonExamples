from flask import Flask
from flask_restful import reqparse, Api, Resource
from sqlalchemy.orm import sessionmaker
from models import Base
import models

import sqlalchemy
import logging
from logging.config import fileConfig
fileConfig('logging.ini')
logger = logging.getLogger()

app = Flask(__name__)
api = Api(app)

username = "root"
password = "masterkey"
dbname = "billing"
host = "localhost"
port = 3306

connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}"

engine = sqlalchemy.create_engine(connection_string, isolation_level="AUTOCOMMIT")
Base.metadata.create_all(engine)
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()


class AddressListController(Resource):
    def get(self):
        addresses = session.query(models.Address).all()
        addresses = [v.as_dict() for v in addresses]
        return addresses

    post_parser = (reqparse
                   .RequestParser(bundle_errors=True)
                   .add_argument("street", type=str, required=False, location="json")
                   .add_argument("city", type=str, required=False, location="json")
                   .add_argument("state", type=str, required=False, location="json")
                   .add_argument("postal_code", type=str, required=False, location="json")
                   .add_argument("country", type=str, required=False, location="json"))

    def post(self):
        args = self.post_parser.parse_args()
        logger.info("args", args)
        address = models.Address()
        address.street = args.get("street")
        address.city = args.get("city")
        address.state = args.get("state")
        address.postal_code = args.get("postal_code")
        address.country = args.get("country")
        session.add(address)
        session.flush()

        return {"status": "Success", "id": address.id}


class AddressController(Resource):

    def get(self, id):
        address = session.query(models.Address).get(int(id))
        if address is None:
            return {"status": "Failed", "message": f"Record does not exists with id {id}"}, 404

        return address.as_dict()

    patch_parser = (reqparse
               .RequestParser(bundle_errors=True)
               .add_argument("street", type=str, required=False, location="json")
               .add_argument("city", type=str, required=False, location="json")
               .add_argument("state", type=str, required=False, location="json")
               .add_argument("postal_code", type=str, required=False, location="json")
               .add_argument("country", type=str, required=False, location="json"))

    def patch(self, id):
        args = self.patch_parser.parse_args()
        logger.info("args", args)

        address = session.query(models.Address).get(int(id))
        address.street = args.get("street")
        address.city = args.get("city")
        address.state = args.get("state")
        address.postal_code = args.get("postal_code")
        address.country = args.get("country")
        session.add(address)
        session.flush()

        return {"status": "Success"}

    def delete(self, id):
        address = session.query(models.Address).get(int(id))
        if address is None:
            return {"status": "Failed", "message": f"Record does not exists with id {id}"}, 404
        session.delete(address)
        session.flush()
        return {"status": "Success"}


@app.route('/')
def home():
    return "Hello! welcome to api."

api.add_resource(AddressController, "/address/<int:id>")
api.add_resource(AddressListController, "/addresses")


if __name__ == '__main__':
    app.run(debug=True, port = 5001)
    
    
    