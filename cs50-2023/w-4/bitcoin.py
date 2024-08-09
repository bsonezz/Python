import sys, requests

try:
    if len(sys.argv) == 2:
        n = float(sys.argv[1])
    elif len(sys.argv) < 2:
        sys.exit("Missing command-line argument ")

except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = response["bpi"]["USD"]["rate_float"]
    amount = rate * n
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass
