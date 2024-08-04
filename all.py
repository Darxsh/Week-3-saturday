# Function to generate the list of integers from 1 to N
def generate_sequence(N):
    return list(range(1, N + 1))

# Main function
if __name__ == "__main__":
    try:
        # Take input from the user
        user_input = input("Enter an integer N: ")
        
        # Convert the input to an integer
        N = int(user_input)
        
        # Generate the sequence
        sequence = generate_sequence(N)
        
        # Print the sequence
        print(f"The sequence from 1 to {N} is: {sequence}")
    except ValueError:
        print("Please enter a valid integer.")
