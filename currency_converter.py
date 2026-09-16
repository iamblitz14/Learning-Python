def currency_converter():
    # Current approximate exchange rate (September 2026)
    # 1 USD = 57.00 PHP
    usd_to_php_rate = 57.00

    print("=== Welcome to the PHP <-> USD Currency Converter ===")
    print("1. Convert Philippine Peso (PHP) to US Dollar (USD)")
    print("2. Convert US Dollar (USD) to Philippine Peso (PHP)")
    
    # Ask the user to pick an option
    choice = input("Choose an option (1 or 2): ").strip()

    # Process Option 1: PHP to USD
    if choice == '1':
        try:
            php_amount = float(input("Enter the amount in PHP: ₱"))
            if php_amount < 0:
                print("Amount cannot be negative.")
                return
            
            usd_amount = php_amount / usd_to_php_rate
            print(f"₱{php_amount:,.2f} PHP is equal to ${usd_amount:,.2f} USD")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Process Option 2: USD to PHP
    elif choice == '2':
        try:
            usd_amount = float(input("Enter the amount in USD: $"))
            if usd_amount < 0:
                print("Amount cannot be negative.")
                return
                
            php_amount = usd_amount * usd_to_php_rate
            print(f"${usd_amount:,.2f} USD is equal to ₱{php_amount:,.2f} PHP")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    # Handle invalid choices
    else:
        print("Invalid choice. Please restart the program and select 1 or 2.")

# Run the program
if __name__ == "__main__":
    currency_converter()
