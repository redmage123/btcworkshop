#!/usr/bin/env python
import hashlib

md = hashlib.md5("The quick brown fox jumps over the lazy dog")
print md.hexdigest()
md = hashlib.md5("The quick brown fox jumps over the lazy dog.")
print md.hexdigest()
md = hashlib.md5("1")
print md.hexdigest()
md = hashlib.md5("2")
