import httplib, urlparse, sys

url = sys.argv[1]

print "url = ", url

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedURL.query)
print conn.getresponse().read()
