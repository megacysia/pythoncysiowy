import sys
import requests

def main():
    amount_of_BTC_to_buy = get_money_to_exchange()
    price_of_BTC = api_return_cost_of_bitcoin()
    actualPrice = (counting_usd(amount_of_BTC_to_buy, price_of_BTC))
    print("price: ", end="")
    print(f"${actualPrice:,.4f}")

def get_money_to_exchange():
    if len(sys.argv) == 2:
        prompt = sys.argv[1]
        try:
            return float(prompt)
        except ValueError:
            sys.exit("It's not a number!")

def api_return_cost_of_bitcoin():
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=5a1101f711ed2f9b8f48d98d58596e122f91d496d7746aeb2ebcf3d44f414211")
    BTC_data = response.json()
    data = BTC_data["data"]
    price =  float(data["priceUsd"])
    return price

def counting_usd(x, y):
    how_much_usd = x * y 
    return how_much_usd

main()