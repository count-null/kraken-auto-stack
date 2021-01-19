# Kraken Exchange Auto Stack Sats

Too many shitcoins in your kraken balance? Trade them for BTC! 

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

Edit `config.json` to your liking.

`python3 stack.py` or schedule with cron.

## Config Options

### alts 

This is a list of rules for each alt eligible to trade. Here are some examples:
```
{
  "name": "ETH",
  "minBalance": 0.5,
  "quote": "ETH",
  "buy": "XBT"
},
```
Sell ETH for XBT. Keep a minimum of 0.5 ETH

```
{
  "name": "STORJ",
  "minBalance": 50,
  "quote": "USD",
  "buy": "XBT"
},
```
Sell STORJ for XBT. Keep a minimum balance of 50 USD worth of STORJ

```
{
  "name": "XXMR",
  "minBalance": 10,
  "quote": "ZUSD",
  "buy": "XXBT"
},
```
Older pairs use the X, Z format for crypto and fiat. You will need to specity those.
This setting will sell XMR for XBT while keeping a minimul balance of 10 USD worth of XMR

### fees
