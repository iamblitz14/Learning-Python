import json
import urllib.request

def fetch_live_rates():
    """Fetches the latest USD to PHP exchange rate dynamically."""
    url = "https://er-api.com"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return data["conversion_rates"]["PHP"]
    except Exception as e:
        print(f"\n[Warning] Could not fetch live rates ({e}). Using offline backup rate.")
    
    return 62.73

def currency_converter():
    print("Connecting to API to fetch live rates...")
    usd_to_php_rate = fetch_live_rates()
    
    print("\n=== Welcome to the Live PHP <-> USD Currency Converter ===")
    print(f"Current Live Rate: 1 USD = {usd_to_php_rate:.4f} PHP")
    
    # This loop keeps the program running until the user decides to exit
    while True:
        print("\n---------------------------------------------------------")
        print("1. Convert Philippine Peso (PHP) to US Dollar (USD)")
        print("2. Convert US Dollar (USD) to Philippine Peso (PHP)")
        print("3. Exit Program")
        print("---------------------------------------------------------")
        
        choice = input("Choose an option (1, 2, or 3): ").strip()

        # Process Option 1: PHP to USD
        if choice == '1':
            try:
                php_amount = float(input("Enter the amount in PHP: ₱"))
                if php_amount < 0:
                    print("Amount cannot be negative.")
                    continue  # Sends the user back to the main menu choices
                
                usd_amount = php_amount / usd_to_php_rate
                print(f"Result: ₱{php_amount:,.2f} PHP is equal to ${usd_amount:,.2f} USD")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Process Option 2: USD to PHP
        elif choice == '2':
            try:
                usd_amount = float(input("Enter the amount in USD: $"))
                if usd_amount < 0:
                    print("Amount cannot be negative.")
                    continue
                    
                php_amount = usd_amount * usd_to_php_rate
                print(f"Result: ${usd_amount:,.2f} USD is equal to ₱{php_amount:,.2f} PHP")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
        # Process Option 3: Exit
        elif choice == '3':
            print("\nThank you for using the Currency Converter. Goodbye!")
            break  # This breaks the while loop and closes the script nicely
            
        # Handle invalid choices
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    currency_converter()
