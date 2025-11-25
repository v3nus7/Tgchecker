"""
Example usage of the Telegram Number Checker module.

This script demonstrates how to use the TelegramChecker class
to check phone numbers on Telegram.
"""

from telegram_checker import TelegramChecker, check_telegram_number, check_telegram_numbers, TelegramCheckerError


def main():
    # Method 1: Create an instance with API key in constructor
    print("=== Method 1: Constructor Initialization ===")
    checker = TelegramChecker(api_key="your_api_key_here")
    
    # Check if configured
    print(f"Checker status: {checker}")
    print(f"Is configured: {checker.is_configured()}")
    
    # Method 2: Create instance first, then set API key
    print("\n=== Method 2: Set API Key Later ===")
    checker2 = TelegramChecker()
    print(f"Before setting key: {checker2}")
    
    checker2.set_api_key("your_api_key_here")
    print(f"After setting key: {checker2}")
    
    # Method 3: Check number using the instance
    print("\n=== Checking a Phone Number ===")
    try:
        # Replace with a real phone number for testing
        result = checker.check_number("+1234567890")
        print(f"Result: {result}")
        
        # Handle the response
        if result.get("success"):
            print("✓ Number check successful!")
            print(f"  Status: {result.get('status')}")
            print(f"  Details: {result.get('data')}")
        else:
            print("✗ Number check failed")
            print(f"  Error: {result.get('message')}")
            
    except TelegramCheckerError as e:
        print(f"Error: {e}")
    
    # Method 4: Using convenience function
    print("\n=== Method 4: Convenience Function ===")
    try:
        result = check_telegram_number("+1234567890", "your_api_key_here")
        print(f"Result: {result}")
    except TelegramCheckerError as e:
        print(f"Error: {e}")
    
    # Method 5: Check multiple numbers at once (batch)
    print("\n=== Method 5: Batch Check (Multiple Numbers) ===")
    try:
        phone_list = ["+1234567890", "+0987654321", "+1122334455"]
        results = checker.check_numbers(phone_list)
        
        for result in results:
            phone = result.get("phone")
            if result.get("error"):
                print(f"  {phone}: Error - {result.get('error')}")
            elif result.get("success"):
                print(f"  {phone}: Success - {result}")
            else:
                print(f"  {phone}: {result}")
                
    except TelegramCheckerError as e:
        print(f"Error: {e}")
    
    # Method 6: Batch check with convenience function
    print("\n=== Method 6: Batch Check Convenience Function ===")
    try:
        results = check_telegram_numbers(["+1234567890", "+0987654321"], "your_api_key_here")
        print(f"Results: {results}")
    except TelegramCheckerError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
