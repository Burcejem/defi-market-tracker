import requests

# Insert your CoinMarketCap API key instead of the text inside the quotes
API_KEY = 'YOUR_API_KEY_HERE'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

parameters = {
    'start': '1',
    'limit': '50', # Number of tokens to fetch
    'convert': 'USD',
    'tag': 'defi'  # Filter exclusively by the DeFi category
}

def get_defi_data():
    try:
        response = requests.get(URL, headers=headers, params=parameters)
        data = response.json()
        
        if response.status_code == 200:
            print("Fetching top DeFi tokens data...\n")
            for item in data['data']:
                name = item['name']
                symbol = item['symbol']
                price = item['quote']['USD']['price']
                volume = item['quote']['USD']['volume_24h']
                
                print(f"{name} ({symbol})")
                print(f"Price: ${price:,.4f}")
                print(f"24h Volume: ${volume:,.2f}")
                print("-" * 30)
        else:
            print(f"API Error: {data['status']['error_message']}")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    get_defi_data()