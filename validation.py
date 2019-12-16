#!/usr/bin/env python3
        

def get_float(prompt, lowvalue, highvalue):
    value = float(input(prompt))
    while value <= lowvalue or value >= highvalue:
        print("Entry must be greater than", lowvalue, "and less than", highvalue, ". please try again.") 
        value = float(input(prompt))

    return value 

def get_int(prompt, low, high):
    years = int(input(prompt))
    while years <= low or years >= high:
        print("Entry must be greater than", low, "and less than", high, ". please try again.")
        years = int(input(prompt))
    return years



def main():
    choice = "y"
    while choice.lower() == "y":
            # get input from the user
        get_float("Enter monthly investment:\t", 0, 1000)       
       
        get_int("Enter number of years:\t", 0, 50)

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()