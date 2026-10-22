import sys
import requests

if len(sys.argv) > 1:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f38a41349005de8af8abf480f1c0fe1e609c666a0177c7f29d40b03a994affda")
    response_json = response.json()
    price = float(response_json["data"]["priceUsd"])
    cost = amount * price
    print(f"${cost:,.4f}")
except requests.RequestException:
    sys.exit("Request failed")