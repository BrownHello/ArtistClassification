from .APIKeys import APIKEYS, USERNAME
from tools import auth, WEBSITE

import requests, urllib.parse as urlparse, json


myAuth = auth(APIKEYS=APIKEYS, username=USERNAME)

req = requests.get(urlparse.urljoin(WEBSITE, '/post.json'), params=auth.endpointParams('/post'))

js = json.dumps(req.text)

print(js)
