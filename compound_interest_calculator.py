# Compound Interest Calculator
savings_amount = float(input("Enter your savings amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
number_of_years = int(input("Enter the number of years you plan to save: "))

interest_rate = annual_interest_rate / 100
current_amount = savings_amount

for year in range(1, number_of_years + 1):
    current_amount = current_amount * (1 + interest_rate)
    print("Year", year, "Amount:", round(current_amount, 2))

    if current_amount >= 2 * savings_amount:
        print("Congratulations! Your savings have doubled in year", year)
        break

