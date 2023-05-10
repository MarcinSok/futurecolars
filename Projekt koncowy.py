from flask import Flask, render_template

app = Flask(__name__)

# Dane dotyczące kryptowalut
crypto_data = [
    {"symbol": "BTC", "name": "Bitcoin", "price": 12000},
    {"symbol": "ETH", "name": "Ethereum", "price": 7800},
    {"symbol": "LTC", "name": "Litecoin", "price": 350},
    {"symbol": "Doge", "name": "Dogecoin" "price": 0,60}
]

# Dane dotyczące publicznie dostępnych portfeli
wallet_data = [
    {"name": "Portfel A", "balance": 10},
    {"name": "Portfel B", "balance": 5},
    {"name": "Portfel C", "balance": 2},
    {"name": "Portfel D", "balance": 7}
]

@app.route("/")
def index():
    return render_template("index.html", crypto_data=crypto_data)

@app.route("/portfele")
def portfele():
    return render_template("portfele.html", wallet_data=wallet_data)

if __name__ == "__main__":
    app.run()
