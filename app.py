from scraper import crypto_scraper
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from waitress import serve

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptodata.db'
db = SQLAlchemy(app)

# creating a database with the following column names
# table_headers = ["Rank", "CryptoCurrency", "Market Cap", "Price", "Circulating Supply", "Volume(24h)", "Change(24h)"]

class CryptoData(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    cryptocurrency = db.Column(db.String(120), nullable=False)
    marketcap = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(120), nullable=False)
    supply = db.Column(db.String(120), nullable=False)
    volume = db.Column(db.String(120), nullable=False)
    change = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return "{self.name} - {self.price}"

def load_data():

    # deleting all previously stored data
    data = CryptoData.query.all()    
    for row in data:
        db.session.delete(row)
        db.session.commit()
    
    # grabbing scraped data from scraper.py
    final_data = crypto_scraper()

    # adding data row by row to the database (cryptodata.db)
    for i in range(len(final_data)):
        row = final_data[i]
        curr = CryptoData(index = i+1, rank = row[0],cryptocurrency = row[1].lower(), marketcap=row[2],
          price = row[3], supply=row[4], volume=row[5], change=row[6])
        db.session.add(curr)
        db.session.commit()



@app.route('/')
def home_page():
    st = '''
    <h1>
    Welcome to the Cryptocurrency API<br><br>
    To find the data, go here <a href="http://127.0.0.1:5000/api/all">http://127.0.0.1:5000/api/all</a>
    </h1>

    '''
    return st


@app.route('/api/all')
def get_all_data():
    load_data()
    data = CryptoData.query.all()


    output = []
    for row in data:
        output.append({"Rank": row.rank, 
        "CryptoCurrency": row.cryptocurrency,
        "Market Cap" : row.marketcap,
        "Price": row.price,
        "Circulating Supply": row.supply,
        "Volume(24h)": row.volume,
        "Change(24h)": row.change
        })
    
    return {"CryptoData": output}


@app.route('/api/<string:cryptocurrency>')
def get_crypto_data(cryptocurrency):
    
    crypt = CryptoData.query.filter_by(cryptocurrency=cryptocurrency.lower()).first()
    
    return jsonify({"Rank": crypt.rank, 
        "CryptoCurrency": crypt.cryptocurrency,
        "Market Cap" : crypt.marketcap,
        "Price": crypt.price,
        "Circulating Supply": crypt.supply,
        "Volume(24h)": crypt.volume,
        "Change(24h)": crypt.change
        })


if __name__ == "__main__":
    # app.run(debug=True)
    serve(app, host='0.0.0.0')