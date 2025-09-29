import requests

data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
rates = data['rates']
print(">>> Available currencies: ", list(rates.keys())[:10])

while True:
    try:
        amount = float(input(">>> Enter the amount: "))
        frm_crr = input(">>> From (USD, EUR, RUB): ").upper()
        to_crr = input(">>> To (EUR, USD, RUB): ").upper()

        if frm_crr not in rates:
            print(f">>> ERROR: Currency '{frm_crr}' not found\n")
            continue

        if to_crr not in rates:
            print(f">>> ERROR: Currency '{to_crr}' not found\n")
            continue
        
        if frm_crr == "USD":
            res = amount * rates[to_crr]
        else:
            usd_amount = amount / rates[frm_crr]
            res = usd_amount * rates[to_crr]
        
        print(f'>>> {amount} {frm_crr} = {res:.2f} {to_crr}\n')
        
        
        again = input(">>> Convert again? (y/n): ").lower()
        if again != 'y':
            break

    except ValueError:
        print(">>> ERROR: Enter a valid number\n")
    except Exception as e:
        print(f">>> ERROR: Something went wrong - {e}\n")