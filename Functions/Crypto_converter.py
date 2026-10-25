"""
Module Name: Cryptocurrency Converter
Description: Converts amounts between Bitcoin, Ethereum, Dogecoin, and Litecoin using USD reference prices.
Author: Kollier

Note: The exchange rates are reference prices and must be updated regularly.
They are not live prices and do not include exchange fees.
"""

def convert_currency(amount, source_currency, target_currency, exchange_rates):
    if amount <= 0:
        raise ValueError("The amount must be greater than zero.")

    if source_currency not in exchange_rates:
        raise ValueError("The source currency is not supported.")

    if target_currency not in exchange_rates:
        raise ValueError("The target currency is not supported.")

    amount_in_usd = amount * exchange_rates[source_currency]
    converted_amount = amount_in_usd / exchange_rates[target_currency]

    return converted_amount

def display_exchange_rates(exchange_rates):
    print("\nCryptocurrency reference prices (USD):")

    for currency, price in exchange_rates.items():
        print(f"{currency}: ${price:,.8f}")

if __name__ == "__main__":
    # Approximate reference prices checked on October 25, 2026.
    # Prices can vary by exchange and market conditions.
    exchange_rates = {
        "BTC": 80713.10,  # Bitcoin
        "ETH": 2333.91,   # Ethereum
        "DOGE": 0.07743,  # Dogecoin
        "LTC": 56.98      # Litecoin
    }

    supported_currencies = ", ".join(exchange_rates.keys())

    display_exchange_rates(exchange_rates)

    try:
        amount = float(input("\nEnter the amount to convert: "))
        source_currency = input(
            f"Enter the source currency ({supported_currencies}): "
        ).strip().upper()

        target_currency = input(
            f"Enter the target currency ({supported_currencies}): "
        ).strip().upper()

        result = convert_currency(
            amount,
            source_currency,
            target_currency,
            exchange_rates
        )

        print(
            f"\n{amount:.8f} {source_currency} is equivalent to "
            f"{result:.8f} {target_currency}"
        )

    except ValueError as error:
        print(f"Error: {error}")