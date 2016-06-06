#!/usr/bin/env python

import hashlib

md = hashlib.sha256("The quick brown fox jumped over the lazy dog")
print md.hexdigest()
