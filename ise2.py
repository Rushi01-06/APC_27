def check_number(num):
    """Check and print whether the number is positive/negative/zero and even/odd."""
    
 
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"
    
  
    if num == 0:
        parity = "Neither even nor odd"
    elif num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
    
    print(f"The number {num} is {sign} and {parity}.")

try:
   
    user_input = input("Enter an integer: ").strip()

    number = int(user_input)

    check_number(number)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
