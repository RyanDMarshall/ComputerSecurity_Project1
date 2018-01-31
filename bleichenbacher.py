#!/usr/bin/python2.7

from roots import *
import hashlib
import sys
# Gets message from command line of the form "from_account+to_account_amount"
# e.g. "eecs183+ryanmars+1.23"
# Verify that command line input is of this form and that this is the "message"

message = sys.argv[1]
# Splits message into three strings appropriately
from_acc, to_acc, amt = message.split('+')

# Beginning of signature, as given in spec (Check this)
sig_begin = "0001FF003031300d060960864801650304020105000420"

# Middle of signature (Sha-256 digest of message)
m = hashlib.sha256()
m.update(message)
sig_mid = m.hexdigest()

# Signature-leftover bits
sig = sig_begin + sig_mid

sig += '0'*402

sig_num = int(sig, 16)
(sig_cube_root, is_cube) = integer_nthroot(sig_num, 3)

if (is_cube):
	print integer_to_base64(sig_cube_root)
else:
	print integer_to_base64(sig_cube_root+1)
