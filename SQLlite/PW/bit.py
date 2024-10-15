import requests
import traceback
import  sqlite3
from peewee import *
from peewee import Model
from peewee import IntegerField, FloatField, CharField, PrimaryKeyField, TimestampField, fn
from peewee import InternalError

db=SqliteDatabase('peewee.db')
class Coins(Model):
    id = PrimaryKeyField(null=False)
    symbol = CharField(unique=True)
    priceChange = FloatField()
    priceChangePercent = FloatField()
    weightedAvgPrice = FloatField()
    prevClosePrice = FloatField()
    lastPrice = FloatField()
    lastQty = FloatField()
    bidPrice = FloatField()
    askPrice = FloatField()
    openPrice = FloatField()
    highPrice = FloatField()
    lowPrice = FloatField()
    volume = FloatField()
    quoteVolume = FloatField()
    openTime = TimestampField()
    closeTime = TimestampField()
    firstId = IntegerField()
    lastId = IntegerField()
    count = IntegerField()
 
    class Meta:
        db_table = 'coins'
        database = db
try:
    db.connect()
    Coins.create_table()
    
except InternalError as px:
    print(str(px))

data=requests.get('https://api.binance.com/api/v1/ticker/24hr').json()

for coin in data:
    exists=Coins.select().where(Coins.symbol==coin['symbol'])

    if bool(exists):
        print('ОБновляем цены:', coin['symbol'])
        Coins.update(
            lastPrice=coin['lastPrice'],
            lastQty=coin['lastQty'],
            bidPrice=coin['bidPrice'],
            askPrice=coin['askPrice'],
            ).where(Coins.symbol==coin['symbol']).execute()
    else:
        print('Добавляем новую:', coin['symbol'])
        Coins.create(
            symbol=coin['symbol'],
            priceChange=coin['priceChange'],
            priceChangePercent=coin['priceChangePercent'],
            weightedAvgPrice=coin['weightedAvgPrice'],
            prevClosePrice=coin['prevClosePrice'],
            lastPrice=coin['lastPrice'],
            lastQty=coin['lastQty'],
            bidPrice=coin['bidPrice'],
            askPrice=coin['askPrice'],
            openPrice=coin['openPrice'],
            highPrice=coin['highPrice'],
            lowPrice=coin['lowPrice'],
            volume=coin['volume'],
            quoteVolume=coin['quoteVolume'],
            openTime=int(coin['openTime'] / 1000),
            closeTime=int(coin['closeTime'] / 1000),
            firstId=coin['firstId'],
            lastId=coin['lastId'],
            count=coin['count'],
        )
        

sorted_coins=Coins.select().order_by(Coins.volume.desc())
print("Sort for 24 hour in volume")
for coin in sorted_coins:
    print(coin.symbol, coin.volume)
print("-"*30)
bnb_count=Coins.select().where(Coins.symbol.endswith('BNB')).count()
print("Кол-во монет в паре с BNB:", bnb_count)
print('-'*30)

print('Random monets')
random=Coins.select().order_by(fn.Random()).limit(5)
for coin in random:
    print(coin.symbol)

    
