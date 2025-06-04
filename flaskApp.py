import atexit
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from binance import Client
from flask import Flask, render_template
from flask import jsonify
from flask import redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy

import config

# USED FOR DETECTING AND DISPLAYING SQLAlchemy errors
# from sqlalchemy.exc import SQLAlchemyError

app = Flask("__name__")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdbTEMP.db'
db = SQLAlchemy(app)

epoch = datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class trackedTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(10), nullable=False)

    # def __init__(self, token):
    #     self.token = token

    # def __repr__(self):
    #     return '<trackedTokens %r>' % self.tokenName


class preloadDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    time = db.Column(db.DateTime)
    token = db.Column(db.String(100), nullable=False)
    open = db.Column(db.Float(8), nullable=True)
    close = db.Column(db.Float(8), nullable=True)
    high = db.Column(db.Float(8), nullable=True)
    low = db.Column(db.Float(8), nullable=True)

    # def __init__(self, price):
    #     self.price = price

    # def __repr__(self):
    #     return '<preloadDB %r>' % self.price


jermClient = Client(config.apiKey, config.apiSecret)
info = jermClient.get_account()
balance = info['balances']
token1 = 'BTCUSDT'
token2 = 'CAKEBUSD'


def printt():
    print('test')


@app.route('/update')
def updateTokenLines():
    print("Updating Token data...")
    for token in getTokenList():
        kline30min_DB(token.token)
    return "Done"


scheduler = BackgroundScheduler()
scheduler.add_job(func=updateTokenLines, trigger="interval", minutes=30)
scheduler.start()

# Exit the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


def getBalances():
    # Gets all balances that are not 00.00 and displays price based on # of coins
    tickers = []
    for x in balance:
        if x['free'] not in ['0.00000000', '0.00']:
            temp = x['asset'] + 'USDT'
            tickers.append(temp)
    return [jermClient.get_all_tickers(symbol=x) for x in tickers]


@app.route('/', methods=['POST', 'GET'])
def homepage():
    global token1, token2

    if request.method == 'POST':
        token1 = request.form['ddMenu']
        token2 = request.form['ddMenu2']
        temp = request.form['newToken']
        if temp != "":
            addNewToken(temp)
        return render_template('index.html', title='Shekel Insight', balances=balance, price=getBalances(),
                               token1=token1,
                               token2=token2, tokens=getTokenList())
    return render_template('index.html', title='Shekel Insight', balances=balance, price=getBalances(), token1=token1,
                           token2=token2, tokens=getTokenList())


@app.route('/getTokenName1')
def getTokenName1():
    return token1


@app.route('/getTokenName2')
def getTokenName2():
    return token2


def addNewToken(tokenName):
    tokens = getTokenList()
    flag = 0
    for token in tokens:
        if token.token == tokenName:
            flag = 1
    if flag != 1:
        temp = trackedTokens(token=tokenName.upper())
        db.session.add(temp)
        db.session.commit()


def getTokenList():
    return trackedTokens.query.all()


@app.route('/account')
def account():
    return 'account'


@app.route('/test', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        tokenPrice = request.form['testt']
        newToken = preloadDB(price=tokenPrice)
        # Commit files to DATABASE
        try:
            db.session.add(newToken)
            db.session.commit()
            return redirect('/test')
        except:
            return "Error occurred trying to add Token to database, maybe wrong input??? (FLOAT)"
    else:
        tokens = preloadDB.query.all()
        title = 'Shekel Cave SQL TEST'

        return render_template('test.html', title=title, balances=balance, price=getBalances(), tokens=tokens)


# Preloads database for instant generation of graph. Much quicker than grabbing data from api every time.

@app.route('/preload/<tokenName>')
def preload(tokenName):
    candles = []
    dbRows = preloadDB.query.filter(preloadDB.token == tokenName)
    for row in dbRows:
        candlestick = {
            "time": (unix_time_millis(row.time) / 1000),
            "open": row.open,
            "high": row.high,
            "low": row.low,
            "close": row.close,
            # "volume": lineData[5],
            # "close time": lineData[6]
        }
        candles.append(candlestick)

    return jsonify(candles)


# Gets missing rows from Binance API and commits to database
@app.route('/kline30minDB/<tokenName>')
def kline30min_DB(tokenName):
    tokenName = tokenName.upper()
    obj = preloadDB.query.order_by(-preloadDB.id).filter(preloadDB.token == tokenName).first()
    try:
        start_time = (unix_time_millis(obj.time) / 1000) + 30600  # WILL BREAK CODE IF DATABASE EMPTY
    except:
        start_time = 1609499880
        addNewToken(tokenName)
    kline = jermClient.get_historical_klines(symbol=tokenName, interval=jermClient.KLINE_INTERVAL_30MINUTE,
                                             start_str=str(start_time))
    for lineData in kline:
        tempp = lineData[0] / 1000
        tempTime = datetime.fromtimestamp(tempp)
        temp = preloadDB(time=tempTime, open=float(lineData[1]), close=float(lineData[4]), high=float(lineData[2]),
                         low=float(lineData[3]), token=tokenName)
        try:
            db.session.add(temp)
        except:
            return "Error occurred trying to add Token to database, maybe wrong input??? (FLOAT)"
    db.session.commit()
    return "Done"


@app.route('/dataset')
def dataset():
    # KLINE FORMAT = 0.Open time 1.Open 2.High 3.Low 4.Close 5.Volume 6.Close time 7.etc
    # noinspection PyGlobalUndefined
    global data_json
    # Last row sorted by ID is queried, which is the latest price entry

    return data_json


# noinspection PyGlobalUndefined
@app.route('/dataset2')
def dataset2():
    # KLINE FORMAT = 1. Open time 2. Open 3. High 4. Low 5. Close 6. Volume 7. Close time 8. etc
    global data_json
    kline = jermClient.get_historical_klines(symbol='CAKEBUSD', interval=jermClient.KLINE_INTERVAL_30MINUTE,
                                             start_str="1 June, 2021")
    candles = []
    for lineData in kline:
        candlestick = {
            "time": lineData[0] / 1000,
            "open": float(lineData[1]),
            "high": float(lineData[2]),
            "low": float(lineData[3]),
            "close": float(lineData[4]),
            # "volume": lineData[5],
            # "close time": lineData[6]
        }
        candles.append(candlestick)
    data_json = jsonify(candles)
    return data_json


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
