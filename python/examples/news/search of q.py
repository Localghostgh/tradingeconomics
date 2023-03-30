import requests

url = "https://brains.tradingeconomics.com/v2/search/wb,fred,comtrade"
params = {
    "q": "nigeria",
    "pp": "50",
    "p": "0",
    "_": "1557934352427",
    "stance": "2"
}

response = requests.get(url, params=params)
data = response.json()

print(data)
