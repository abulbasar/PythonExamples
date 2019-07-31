from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import csv

app = Flask(__name__)
api = Api(app)
"""
$ curl -i \
  --header "Content-type: application/json" \
  --request POST \
  --data '{"date": "2016-08-04","open": "28.01","high": "28.190001","low": "27.9","close": "28.049999","volume": "3899900.0","adjclose": "28.049999","symbol": "CSX - update","id": 1845}' \
xhttp://127.0.0.1:5001/
"""

class StockEntity(Resource):
    
    def __init__(self):
        with open("/data/stocks.small.csv") as f:
            csv_reader = csv.DictReader(f)
            rows = list(csv_reader)
            for i in range(len(rows)):
                rows[i]["id"] = i
            self.rows = rows

    post_parser = (reqparse
                    .RequestParser(bundle_errors=True)
                    .add_argument('id', type = int)
                    .add_argument('date', type = str)
                    .add_argument('date', type = str)
                    .add_argument('open', type = float)
                    .add_argument('close', type = float)
                    .add_argument('high', type = float)
                    .add_argument('low', type = float)
                    .add_argument('adjclose', type = float)
                    .add_argument('volume', type = float)
                    .add_argument('symbol', type = str))
        
    def post(self):
        args = self.post_parser.parse_args(strict = True)
        print(args)
        index = args["id"]
        self.rows[index] = args
        return args

    def get(self):
        return self.rows
        

api.add_resource(StockEntity, '/')

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
    
    
    