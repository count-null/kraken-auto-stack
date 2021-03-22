# Kraken Auto Stack Sats

Too many shitcoins in your Kraken account? Trade them for BTC!


## Features

- [x] List the alt tickers you want to sell
- [x] Set a min balance to keep for each alt
- [x] Determine worthwhile trades (user-defined)
- [x] Create market buy orders
- [x] Support for fiat/shitcoin cost averaging (when used with cron)
- [ ] Send an email report after every stack
- [ ] Auto widthdraw to saved address

## Warning

You are responsible for the code you run.

## Dependencies

This script depends on [krakenex](https://github.com/veox/python3-krakenex) which itself depends on [requests](https://github.com/psf/requests)

## Installation

From the repo folder,

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

## Usage

`mv example.kraken.key kraken.key`

Put your API keys in `kraken.key`

`cp example.config.json` `config.json`

Edit `config.json` (See Config Options)

`python3 stack.py` or schedule with cron.

## Config Options

The `alts` section defines the selling rules for each alt.

e.x. Sell ETH for BTC. Sell all of it at once. Only if more than 0.1 ETH available.

```
"ETH": {
  "minBalance": 0,
  "minSell": 0.1,
  "maxSell": false,
  "quote": "ETH",
  "buy": "XBT",
  "pair": "ETHXBT"
},
```

e.x. Sell STORJ for BTC. Sell only 10 USD worth of STORJ. Keep at least 50 USD worth of STORJ at all times. 

```
"STORJ": {
  "minBalance": 50,
  "minSell": 10,
  "maxSell": 10,
  "quote": "USD",
  "buy": "XBT",
  "pair": "STORJXBT"
},
```

e.x. Sell USDT for BTC. Sell only 50 USDT at a time. Sell all of it.. 

```
"XXBT": {
  "minBalance": 0,
  "minSell": 0,
  "maxSell": 50,
  "quote": "USDT",
  "buy": "USDT"
  "pair": "XBTUSDT"
},
```

Note that with stablecoins, you must "buy" the stablecoin and list XXBT as the alt. Don't worry, it sells them.


e.x. Sell XMR for BTC. Keep at least 100 USD worth on hand. Dollar cost average 10 USD. Warning: a zero `minSell` may incur cost prohibitive fees by trying to sell dust.

```
"XXMR": {
  "minBalance": 100,
  "minSell": 0,
  "maxSell": 10
  "quote": "ZUSD",
  "buy": "XXBT",
  "pair": "XXMRXXBT"
},
```

Older pairs use the X/Z prefix for crypto/fiat tickers. You will need to specify those explicitly. [Find your pair!](https://support.kraken.com/hc/en-us/articles/360000920306-Ticker-pairs)
