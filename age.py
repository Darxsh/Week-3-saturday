# Function to filter ages that are 18 or older
def filter_adult_ages(ages):
    return [age for age in ages if age >= 18]

# Main function
if __name__ == "__main__":
    try:
        # Take input from the user as a comma-separated string
        user_input = input("Enter the ages separated by commas: ")
        
        # Convert the input string to a list of integers
        ages = list(map(int, user_input.split(',')))
        
        # Filter the ages
        adult_ages = filter_adult_ages(ages)
        
        # Print the filtered ages
        print(f"The ages of persons 18 or older are: {adult_ages}")
    except ValueError:
        print("Please enter valid ages as integers separated by commas.")
