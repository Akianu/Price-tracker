import requests

# Function to fetch the current price of Lava Network (LAVA)
def get_lava_price(currency="usd"):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids=lava-network&vs_currencies={currency}'
    response = requests.get(url)
    data = response.json()
    
    # Return the price of Lava Network in the specified currency (default is USD)
    if 'lava-network' in data:
        return data['lava-network'][currency]
    else:
        print("Error: Unable to fetch data for Lava Network.")
        return None

# Function to calculate portfolio value
def calculate_portfolio_value(holdings):
    total_value = 0
    for crypto, amount in holdings.items():
        if crypto == "lava-network":
            price = get_lava_price()
            if price is not None:
                value = price * amount
                total_value += value
                print(f"Lava Network (LAVA): {amount} coins = ${value:.2f}")
        else:
            print(f"Error: Unsupported cryptocurrency {crypto}")
            return None
    return total_value

# Main function
def main():
    # Example portfolio (just Lava Network in this case)
    portfolio = {
        "lava-network": 1000,  # 1000 LAVA
    }

    print("Calculating your crypto portfolio value...\n")
    total_value = calculate_portfolio_value(portfolio)
    
    if total_value is not None:
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == '__main__':
    main()
