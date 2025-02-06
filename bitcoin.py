import sys
import requests
import json


# Ask for cmd arg no. of bitcoins(n) # convet arg to float
def get_bitcoin():
    try:
        if len(sys.argv) >= 2:
            bitcoin = float(sys.argv[1])
            return bitcoin
        else:
            len(sys.argv) == 1
            sys.exit("Missing command line argument")

    except ValueError:
        sys.exit("Command line argument must be a number")


# Ask API for Json obj
def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        rate = data["bpi"]["USD"]["rate_float"]
        return rate

    except requests.exceptions.RequestException:
        sys.exit("Error: Cannot connect to API")


# Calculate current cost of n bitcoins
def Calculate_Price(bitcoin, rate):
    price = bitcoin * rate
    return price


# output current cost of n bitcoins
def main():

    bitcoin = get_bitcoin()
    price = get_bitcoin_price()
    Current_price = Calculate_Price(bitcoin, price)
    print(f"${Current_price:,.2f}")


if __name__ == "__main__":
    main()
