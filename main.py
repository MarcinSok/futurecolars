from flask import Flask, render_template, redirect, url_for
import requests
import matplotlib.pyplot as plt
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'  # Klucz do obsługi formularza (zmień na swój własny)

@app.route("/")
def index():
    # Pobierz dane o kryptowalutach z zewnętrznego API (np. CoinGecko API)
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,litecoin")
    crypto_data = response.json()

    # Pobierz dane dotyczące skupu/sprzedaży z innego źródła (np. lokalna baza danych)
    buy_sell_data = {
        "bitcoin": {"buy": 38000, "sell": 38500},
        "ethereum": {"buy": 2500, "sell": 2550},
        "litecoin": {"buy": 150, "sell": 155},
    }

    # # Wygeneruj wykresy dla wybranych kryptowalut
    # for crypto in crypto_data:
    #     symbol = crypto["symbol"]
    #     prices = [100, 200, 300]  # Przykładowe dane wykresu (dla uproszczenia)
    #     plt.plot(prices)
    #     plt.title(f"Wykres dla {symbol}")
    #     plt.xlabel("Okres")
    #     plt.ylabel("Cena")
    #     plt.savefig(f"static/{symbol}.png")  # Zapisz wykres jako plik statyczny

    return render_template("index.html", crypto_data=crypto_data, buy_sell_data=buy_sell_data)



class WalletForm(FlaskForm):
    wallet_name = StringField('Nazwa portfela', validators=[InputRequired()])
    time_range = SelectField('Zakres czasu', choices=[('daily', 'Dobowy'), ('weekly', 'Tygodniowy'), ('monthly', 'Miesięczny')])
    submit = SubmitField('Pokaż informacje')

@app.route("/portfele", methods=['GET', 'POST'])
def portfele():
    form = WalletForm()

    if form.validate_on_submit():
        wallet_name = form.wallet_name.data
        time_range = form.time_range.data

        # Pobierz informacje na temat wybranego portfela z zewnętrznego API
        # Przetwórz dane i przekieruj na stronę z informacjami

        return redirect(url_for('wallet_info', wallet_name=wallet_name, time_range=time_range))

    return render_template("portfele.html", form=form)

@app.route("/portfele/<wallet_name>/<time_range>")
def wallet_info(wallet_name, time_range):
    # Pobierz informacje na temat wybranego portfela i wybranego zakresu czasu z zewnętrznego API

    # Przetwórz dane i wygeneruj stronę z informacjami na temat portfela

    return render_template("wallet_info.html", wallet_name=wallet_name, time_range=time_range)

# Dane dotyczące kryptowalut
crypto_data = [
    {"symbol": "BTC", "name": "Bitcoin", "price": 12000},
    {"symbol": "ETH", "name": "Ethereum", "price": 7800},
    {"symbol": "LTC", "name": "Litecoin", "price": 350},
    {"symbol": "Doge", "name": "Dogecoin", "price": 0.60}
]

# Dane dotyczące publicznie dostępnych portfeli
wallet_data = [
    {"name": "Portfel A", "balance": 10},
    {"name": "Portfel B", "balance": 5},
    {"name": "Portfel C", "balance": 2},
    {"name": "Portfel D", "balance": 7}
]

# @app.route("/")
# def index():
#     return render_template("index.html", crypto_data=crypto_data)

# @app.route("/portfele")
# def portfele():
#     return render_template("portfele.html", wallet_data=wallet_data)

if __name__ == "__main__":
    app.run(debug=True)
