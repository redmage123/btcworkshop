#!/usr/bin/env python
import hashlib

data = "The quick brown fox jumps over the lazy dog"
md = hashlib.new('ripemd160',data)
print md.hexdigest()
