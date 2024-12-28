# print("Welcome to the tip calculator.")
# bill = input("what was the total bill? ")
# bill_as_float = float(bill)
# tip = input("what percentage tip would you like to give? 10,12 or 15 ")
# tip_as_int = int(tip)
# final_bill = (bill_as_float + (bill_as_float*tip_as_int)/100)
# spilt = input("How many people to spilt the bill? ")
# spilt_as_integer = int(spilt)
# pay = final_bill / spilt_as_integer
# print(f"Each person should pay:{round(pay,2)}") # using this to round off the value to 2 decimal places

#better syntax

print("Welcome to the calcuator ! ")
bill = float(input("what was the total bill"))
tip = int(input("what percentage tip would you like to give?10,12,15  "))
final_bill = (bill + (bill*tip)/100)
spilt = int(input("How many people to spilt the bill? "))
pay = final_bill/spilt
pay_total = "{:.2f}".format(pay)

print(f"Each person should pay : {pay_total}")

