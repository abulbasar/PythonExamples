from datetime import datetime

class Stock():
    
    @staticmethod
    def parse_utc_date(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")
    
    def __init__(self, line):
        parts = line.split(",")
        self.date = self.parse_utc_date(parts[0])
        self.open = float(parts[1]) 
        self.high = float(parts[2])
        self.low = float(parts[3])
        self.close = float(parts[4])
        self.volume = float(parts[5])
        self.adjclose = float(parts[6])
        self.symbol = parts[7]
        
    def __repr__(self):
        return "{date} {symbol} {adjclose}".format(**self.__dict__)
    
    def __eq__(self, other):
        return self.date == other.date and self.symbol == self.symbol
    
    @property
    def pct_change(self):
        return (self.close - self.open) * 100/ self.open

