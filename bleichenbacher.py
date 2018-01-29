from roots import *
import hashlib
import sys
message = sys.argv[1]

from_acc, to_acc, amt = message.split('+')

sig_begin = "0001FF003031300d060960864801650304020105000420"

m = hashlib.sha256()
m.update(message)
sig_mid = m.hexdigest()

sig = sig_begin + sig_mid
#202 bytes remaining on the right side
sig_bytes = len(sig)*8
leftover = 202

for i in range(0, leftover):
	(num, perf) = integer_nthroot(sig_bytes+i,3)
	if perf:
		break

sig += integer_to_base64(leftover)
print sig

# Key obtained from https://
key = ("-----BEGIN PUBLIC KEY-----"
"MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA6zf/W1NAwrs6gRr94ULW"
"8DcApVRkuZHInGVL6HhUFRTsbuTWWWLHWFJQATfAeySb3uPvbmAEAp9Lfrow5zLL"
"c4So2xse8EDvb8lWdTC4WP4LtYmWqiGHc6qJnKUMHx8mxHrElvHAOVVAJzvmCuGv"
"Sb2rxFLEEFxgw0CNUJ6CCSqN6Vc3176sqVC3a7vqyB+VojcVIQYVRpMjsxks+daU"
"N0PCdF22kVL6mDg+MmsMnLqS10F1sU+W+BCivRU+0dZgrX89jKam7V4g8neVYsi4"
"qJsXjJizIHsHF2WUPLNETTMU2+sNfpuVMeUaKR34wE6vP2XeFWpRH8piUKtcqsqZ"
"dQIBAw=="
"-----END PUBLIC KEY-----")

# Results of openssl rsa -in p3key.pub -pubin -text -noout
"""Public-Key: (2048 bit)
Modulus:
    00:eb:37:ff:5b:53:40:c2:bb:3a:81:1a:fd:e1:42:
    d6:f0:37:00:a5:54:64:b9:91:c8:9c:65:4b:e8:78:
    54:15:14:ec:6e:e4:d6:59:62:c7:58:52:50:01:37:
    c0:7b:24:9b:de:e3:ef:6e:60:04:02:9f:4b:7e:ba:
    30:e7:32:cb:73:84:a8:db:1b:1e:f0:40:ef:6f:c9:
    56:75:30:b8:58:fe:0b:b5:89:96:aa:21:87:73:aa:
    89:9c:a5:0c:1f:1f:26:c4:7a:c4:96:f1:c0:39:55:
    40:27:3b:e6:0a:e1:af:49:bd:ab:c4:52:c4:10:5c:
    60:c3:40:8d:50:9e:82:09:2a:8d:e9:57:37:d7:be:
    ac:a9:50:b7:6b:bb:ea:c8:1f:95:a2:37:15:21:06:
    15:46:93:23:b3:19:2c:f9:d6:94:37:43:c2:74:5d:
    b6:91:52:fa:98:38:3e:32:6b:0c:9c:ba:92:d7:41:
    75:b1:4f:96:f8:10:a2:bd:15:3e:d1:d6:60:ad:7f:
    3d:8c:a6:a6:ed:5e:20:f2:77:95:62:c8:b8:a8:9b:
    17:8c:98:b3:20:7b:07:17:65:94:3c:b3:44:4d:33:
    14:db:eb:0d:7e:9b:95:31:e5:1a:29:1d:f8:c0:4e:
    af:3f:65:de:15:6a:51:1f:ca:62:50:ab:5c:aa:ca:
    99:75
Exponent: 3 (0x3)"""

# Your code to forge a signature goes here.

#print integer_to_base64(forged_signature)

