# Kraken Exchange Auto Stack Sats

Too many shitcoins in your Kraken account? Trade them for BTC!

## Features

- [x] List the alt tickers you want to sell
- [x] Set a min balance to keep for each alt
- [x] Determine worthwhile trades (user-defined)
- [x] Create market buy orders (untested)
- [ ] Auto widthdraw to saved address

## Warning

You are responsible for the code you run.

## Dependencies

This script depends on `krakenex` ([source](https://github.com/veox/python3-krakenex)) which itself depends on ([requests](https://github.com/psf/requests))

## Installation

From the repo folder,

`python3 -m venv venv`

`source venv/bin/activate`

`pip3 install -r requirements.txt`

## Usage

`mv example.kraken.key kraken.key`

Put your API keys in `kraken.key`

`mv example.config.json` `config.json`

Edit `config.json` (See Config Options)

`python3 stack.py` or schedule with cron.

## Config Options

The `alts` section defines the selling rules for each alt.

e.x. Sell ETH for BTC. Sell all of it. Don't sell less than 0.1 ETH at a time.

```
"ETH": {
  "minBalance": 0,
  "minSell": 0.1,
  "quote": "ETH",
  "buy": "XBT"
},
```

e.x. Sell STORJ for BTC. Keep at least 50 USD worth of STORJ at all times. Don't sell less than 10 USD worth at a time.

```
"STORJ": {
  "minBalance": 50,
  "minSell": 10,
  "quote": "USD",
  "buy": "XBT"
},
```

e.x. Sell XMR for BTC. Keep at least 10 USD on hand. Warning a zero minSell may incur cost prohibitive fees.

```
"XXMR": {
  "minBalance": 10,
  "minSell": 0,
  "quote": "ZUSD",
  "buy": "XXBT"
},
```

Older pairs use the X/Z format for crypto/fiat. You will need to specify those explicitly. [Find your ticker](https://support.kraken.com/hc/en-us/articles/360000920306-Ticker-pairs).
