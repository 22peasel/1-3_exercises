#!/usr/bin/env python3
import validation        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    if i % 120 == 0:
            print("Year = ", i // 120 , "Future Value =" , round(future_value, 2))
    return future_value

# def get_float(prompt, lowvalue, highvalue):
#     value = float(input(prompt))
#     while value <= lowvalue or value >= highvalue:
#         print("Entry must be greater than", lowvalue, "and less than", highvalue, ". please try again.") 
#         value = float(input(prompt))

#     return value 

# def get_int(prompt, low, high):
#     years = int(input(prompt))
#     while years <= low or years >= high:
#         print("Entry must be greater than", low, "and less than", high, ". please try again.")
#         years = int(input(prompt))
#     return years



def main():
    choice = "y"
    while choice.lower() == "y":
            # get input from the user
        monthly_investment = validation.get_float("Enter monthly investment:\t", 0, 1000)       
        yearly_interest_rate = validation.get_float("Enter yearly interest rate:\t", 0, 16)
        year = validation.get_int("Enter number of years:\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, year)
    
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()