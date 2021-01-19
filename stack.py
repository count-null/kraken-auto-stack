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
        tb[alt['name']] = float(bal[alt['name']])      
    return tb

    
def getPrice(asset, units):
    pair = asset+units
    print(pair)
    ticker = k.query_public('Ticker', {'pair': pair})
    print(ticker)
    last_close_raw = ticker["result"][pair]["c"]
    last_close = last_close_raw[0]
    return float(last_close)

def getAltConfig(ticker):
    for alt in c['alts']:
        if alt['name'] == ticker:
            return alt

def getSellableUnits(tradable):
    # units of each tradable asset can be sold
    sellable = {}
    for alt in tradable:
        a = getAltConfig(alt)
        unitsOfMin = a['minBalance'] / getPrice(alt, a['quote'])
        if tradable[alt] > unitsOfMin:
            sellable[alt] = tradable[alt] - unitsOfMin
        else:
            sellable[alt] = 0
    return sellable

def main():
    bal = getBalance()
    tradable = getTradableBalance(bal)
    print(tradable)
    print(getSellableUnits(tradable))
    print("Done.")

if __name__ == "__main__":
    main()
