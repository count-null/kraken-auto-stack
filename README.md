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

`python3 stack.py`
