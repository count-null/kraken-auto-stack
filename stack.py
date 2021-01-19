#!/usr/bin/env python

import krakenex
import json

k = krakenex.API()
k.load_key('kraken.key')

def getConfig():
    with open('config.json') as f:
        return json.load(f)

c = getConfig()

def getBalance():
    return k.query_private('Balance')['result']

def getTradableBalance(bal):
    tb = {}
    for alt in c['alts']:
        tb[alt] = float(bal[alt])
    return tb

def getPrice(asset, quote):
    pair = asset+quote
    ticker = k.query_public('Ticker', {'pair': pair})
    last_close_raw = ticker["result"][pair]["c"]
    last_close = last_close_raw[0]
    return float(last_close)

def getAltConfig(ticker):
    for alt in c['alts']:
        if alt == ticker:
            return c['alts'][alt]

def getReserveUnits(tradable):
    reserve = {}
    for alt in tradable:
        a = getAltConfig(alt)
        reserve[alt] = a['minBalance'] / getPrice(alt, a['quote'])
    return reserve

def getSellableUnits(tradable, reserves):
    # units of each tradable asset can be sold
    sellable = {}
    for alt in tradable:
        unitsOfMin = reserves[alt]
        if tradable[alt] > unitsOfMin:
            sellable[alt] = tradable[alt] - unitsOfMin
    return sellable

def getPair(alt):
  return "%s%s" % (alt, c['alts'][alt]['buy'])

def marketBuy(alt, amt):
    pair = getPair(alt)
    k.query_private('AddOrder', {
        'pair': pair,
        'type': 'buy',
        'ordertype': 'market',
        'volume': amt
    })
    print("BUY %s %s" % (pair, amt))

def worthIt(alt, amt):
    a = getAltConfig(alt)
    return getPrice(alt, amt) > a['minSell']

def getVolume(alt, amt):
    a = getAltConfig(alt)
    if a['maxSell']:
        stackSize = a['maxSell'] / getPrice(alt, a['quote'])
        if amt > stackSize:
            return stackSize
    return amt

def processTrades():
    #bal = getBalance()
    bal = {"STORJ": 1234.2342234, "XXMR": 3423.232355}
    printTable(bal, "Account Balances:")
    tradable = getTradableBalance(bal)
    reserves = getReserveUnits(tradable)
    printTable(reserves, "Minimum Required Balances:")
    sellable = getSellableUnits(tradable, reserves)
    if sellable:
        printTable(sellable, "Ready to Trade:")
        for alt in sellable:
            amt = sellable[alt]
            if worthIt(alt, amt):
                vol = getVolume(alt, amt)
    	        marketBuy(alt, vol)
    else:
        print("No alts to trade. Good job!")


def printTable(vals, desc):
    print()
    print(desc)
    for key in vals:
        print("%s %s" % (key, vals[key]))
    print()

def main():
    processTrades()
    print("Done.")

if __name__ == "__main__":
    main()
