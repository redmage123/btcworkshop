#!/usr/bin/env python
import json
import urllib2
import sys

# This simple example shows how to get the latest price in a given currency to bitcoin

exchange_data = {}

# Get the exchange data

while (1):
    curr = raw_input("Please enter the currency you want to compare to bitcoin: ")
    response= urllib2.urlopen("https://blockchain.info/ticker")
    exchange_data = json.loads(response.read())
    try:
        print "Price from the last 15 minutes: %.2f" % exchange_data[curr]["15m"]
    except KeyError:
        if (curr.upper() == "X"):
            sys.exit()
        print "Invalid currency type"




