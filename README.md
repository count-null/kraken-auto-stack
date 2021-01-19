# Kraken Exchange Auto Stack Sats

Too many shitcoins in your Kraken account? Trade them for BTC!

## Features 

 - List the alt tickers you want to sell
 - Set a min balance to keep for each alt

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

e.x. Sell ETH for BTC. Sell all of it.
```
"ETH": {
  "minBalance": 0,
  "quote": "ETH",
  "buy": "XBT"
},
```
 
e.x. Sell STORJ for BTC. Keep at least 50 USD worth of STORJ at all times.
```
"STORJ": {
  "minBalance": 50,
  "quote": "USD",
  "buy": "XBT"
},
```
e.x. Sell XMR for BTC. Keep at least 10 USD on hand. 
```
"XXMR": {
  "minBalance": 10,
  "quote": "ZUSD",
  "buy": "XXBT"
},
```
Older pairs use the X/Z format for crypto/fiat. You will need to specity those explicitly. [Find your ticker](https://support.kraken.com/hc/en-us/articles/360000920306-Ticker-pairs).

