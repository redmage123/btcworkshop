#!/usr/bin/env python

#from bitcoin import *
from pybitcointools import *
import hashlib

privateKey = sha256('i love bitcoins a lot')
print "This is the private key created:  " ,privateKey

publicKey = privtopub(privateKey)

print "This is the public key created:  ",publicKey

addr = pubtoaddr(publicKey)
 
print "This is the bitcoin wallet address created from the public key: ",addr


print "This is the wallet's history",history(addr)

addr = "1C8iAFLrkCZpE5fVG97dMbGzTyRumBVo5Q"
print "This is the wallet's history",history(addr)
