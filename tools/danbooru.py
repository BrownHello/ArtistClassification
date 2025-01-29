import requests
import urllib.parse as urlParse
import json

TESTWEBSITE = r"https://testbooru.donmai.us/"
WEBSITE = r"https://danbooru.donmai.us/"
TEST = True

if TEST:
    WEBSITE = TESTWEBSITE

class auth:
    
    def __init__(self, APIKEYS: dict, username: str):
        self.APIKEYS = APIKEYS
    
    def endpointParams(self, endpoint: str):
        return self.__authParams(self.APIKEYS[endpoint], str)

    def __authParams(apikey: str, username: str) -> dict:
        return {
            "login": username,
            "api_key": apikey
            }

def url(apiStr: str):
    return urlParse.urljoin(WEBSITE, apiStr)


if __name__ == "__main__":
    req = requests.get(url("posts.json?search[id]=1"), params={})
    print(req.text)