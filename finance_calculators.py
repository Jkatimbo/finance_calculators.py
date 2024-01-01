#finance_calculators.py 
#program allows a user to access two different financial calculators, an inves calculator and a home loan repayment calculator.

#function to import python math 
import math 

#initial output statements 
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#user input for their choice
user_choice = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

# Check if the user entered a valid choice
if user_choice not in ['investment', 'bond']:
    print("Invalid input. Please enter 'investment' or 'bond'.")
else:
    # User selected 'investment'
    if user_choice == 'investment':
        # Ask the user for input
        principal_amount = float(input("Enter the amount of money you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
        years = int(input("Enter the number of years you plan on investing: "))
        interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

        # Calculate the total amount based on the interest type
        if interest_type == 'simple':
            total_amount = principal_amount * (1 + interest_rate * years)
        elif interest_type == 'compound':
            total_amount = principal_amount * math.pow((1 + interest_rate), years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            total_amount = None

        # Display the result
        if total_amount is not None:
            print(f"The total amount after {years} years with {interest_rate * 100}% {interest_type} interest is: {total_amount:.2f}")

    # User selected 'bond'
    else:
        # Ask the user for input
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate: ")) / 100
        months = int(input("Enter the number of months for bond repayment: "))

        # Calculate the monthly repayment amount
        monthly_interest_rate = annual_interest_rate / 12
        repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

        # Display the result
        print(f"The monthly repayment amount for the bond is: {repayment:.2f}")
