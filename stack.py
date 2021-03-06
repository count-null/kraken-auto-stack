#!/usr/bin/env python

import krakenex
import json

projectPath = '/home/admin/download/kraken-auto-stack/'

k = krakenex.API()
k.load_key(projectPath + 'kraken.key')

def getConfig():
    with open(projectPath + 'config.json') as f:
        return json.load(f)

c = getConfig()

def configLegit():
    keys = ['minBalance', 'minSell', 'maxSell', 'quote', 'buy']
    for alt in c['alts']:
        # Check all the config keys are there
        for key in keys:
            if key not in c['alts'][alt]:
                print("Configuration error!")
                print("%s is missing key [%s]" % (alt, key))
                return False
        # Check minBuy is less than maxBuy (if maxBuy is set)
        maxSell = c['alts'][alt]['maxSell']
        minSell = c['alts'][alt]['minSell']
        if maxSell and minSell > maxSell:
            print("Configuration error!")
            print("[maxBuy] must be less than [minBuy] for %s" % (alt))
            return False
    return True

def getBalance():
    return k.query_private('Balance')['result']

def getTradableBalance(bal):
    tb = {}
    for alt in c['alts']:
        tb[alt] = float(bal[alt])
    return tb

def getMinOrder(alt):
    a = getAltConfig(alt)
    pair = alt+a['quote']
    response = k.query_public('AssetPairs', {'pair': pair})
    orderMin = response['result'][pair]['ordermin']
    return orderMin

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
    response = k.query_private('AddOrder', {
        'pair': pair,
        'type': 'sell',
        'ordertype': 'market',
        'volume': str(amt)
    })
    print("%s txid %s" % (response['result']['descr']['order'], response['result']['txid'][0]))

def worthIt(alt, amt):
    a = getAltConfig(alt)
    return getPrice(alt, a['quote'])*amt > a['minSell']

def getVolume(alt, amt):
    a = getAltConfig(alt)
    if a['maxSell']:
        stackSize = a['maxSell'] / getPrice(alt, a['quote'])
        if amt > stackSize:
            return round(stackSize, 4)
    return round(amt, 4)

def processTrades():
    bal = getBalance()
    printTable(bal, "Account Balances:")
    tradable = getTradableBalance(bal)
    reserves = getReserveUnits(tradable)
    printTable(reserves, "Minimum Required Balances:")
    sellable = getSellableUnits(tradable, reserves)
    if sellable:
        aboutToSell={}
        minOrders={}
        for alt in sellable:
            amt = sellable[alt]
            if worthIt(alt, amt):
                vol = getVolume(alt, amt)
                minOrder = getMinOrder(alt)
                aboutToSell[alt] = vol
                minOrders[alt] = minOrder
        printTable(aboutToSell, "Eligible to Trade:")
        printTable(minOrders, "Kraken Min Orders:")
        for alt in aboutToSell:
            if aboutToSell[alt] > float(minOrders[alt]):
                marketBuy(alt, aboutToSell[alt])
            else:
                print("%s volume does not meet Kraken's minimum requirements for trade." % (alt))
    else:
        print("No alts to trade. Good job!")


def printTable(vals, desc):
    print()
    print(desc)
    for key in vals:
        print("%s %s" % (key, vals[key]))
    print()

def main():
    if configLegit():
        processTrades()
    print("Done.")

if __name__ == "__main__":
    main()
