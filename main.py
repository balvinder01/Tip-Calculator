#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# code below this line 👇
print("welcome to tip calculator")
bill=float(input("what is the total bill?\n"))
tip=int(input("what percentage tip would you like to give? 10,12,15?\n"))
people=int(input("how many people you want to split the bill?\n"))
tip_as_percent= tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"each person should pay{final_amount}")
