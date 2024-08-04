# Function to count the digits in a number
def count_digits(number):
    return len(str(number))

# Main function
if __name__ == "__main__":
    try:
        # Take input from the user
        user_input = input("Enter a number: ")
        
        # Convert the input to an integer
        number = int(user_input)
        
        # Get the count of digits
        digit_count = count_digits(number)
        
        # Print the count of digits
        print(f"The number of digits in {number} is: {digit_count}")
    except ValueError:
        print("Please enter a valid number.")
