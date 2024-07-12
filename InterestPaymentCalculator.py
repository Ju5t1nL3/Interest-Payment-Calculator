"""
Amortization calculator that calculates the monthly payment for taking out a loan given the
loan amount, loan term, and interest rate
"""

def start_calc():
    """
    Asks questions about the loan to calculate the monthly payment
    """
    loan_amt = float(input("Enter the loan amount: "))

    accepted_units = ["months", "years"]
    next_step = False

    while not next_step:
        term_units = input("Would you like to input your loan term in months or years? ").lower()
        if term_units in accepted_units:
            next_step = True
            if term_units == "years":
                loan_term = int(input("Enter the loan term (in years): ")) * 12
            else:
                loan_term = int(input("Enter the loan term (in months): "))
        else:
            print("Please enter an accepted answer")

    interest = float(input("Enter the annual interest rate: "))

    calc_interest =  lambda a,b,c: a*(b/1200)/(1-((1+(b/1200))**(-c)))

    monthly_payment = calc_interest(loan_amt,interest,loan_term)

    return round(monthly_payment,2)

#starts program
print(start_calc())