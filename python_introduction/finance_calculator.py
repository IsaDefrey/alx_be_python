#prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculate projected annual savings with 5% interest rate
annual_interest_rate = 0.05
annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * annual_interest_rate
projected_savings = annual_savings_without_interest + interest_earned

#print result
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")

