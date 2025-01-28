import requests
import urllib.parse as urlParse
import json

TESTWEBSITE = r"https://testbooru.donmai.us/"
WEBSITE = r"https://danbooru.donmai.us/"
TEST = False

if TEST:
    WEBSITE = TESTWEBSITE

def authenticate(apikey: str, username: str) -> dict:
    return {
        "login": username,
        "api_key": apikey
        }

def url(apiStr: str):
    return urlParse.urljoin(WEBSITE, apiStr)


if __name__ == "__main__":
    req = requests.get(url("posts.json?search[id]=1"), params={})
    print(req.text)