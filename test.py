from pymd5 import md5, padding

m = "Use HMAC, not hashes"
init_state =  md5(m).hexdigest()

print init_state

h = md5(state=init_state.decode("hex"), count=512)

x = "Good advice"
h.update(x)
print "Updated = ", h.hexdigest()

correct = m + padding(len(m)*8) + x
print "Original = ", md5(correct).hexdigest()
