import requests

def get(l, w, url="http://localhost:8765/fish"):
    params = {
        'length': l,
        'weight': w,
    }

    response = requests.get(url, params=params)
    #j = response.json()
    r = response.text
    return r
