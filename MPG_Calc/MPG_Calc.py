
#
#Joshua Pantoja
#SEC 290 24194.B1 Spring 2020
#1/26/2020
#Programming Assignemet 2 MPG
#

print("Automobile Fuel Cost Calculator\n")

print("This program may help with deciding which car makes more sense based on your budget.You will be asked to enter the MPG, the average number of miles you expect to drive each month, and the cost per gallon for fuel.\n")

print("The program will then calculate the monthly fuel cost.\n")


car_mpg_input = input("Please enter the car's average MPG (miles per gallon): ")
car_float = float(car_mpg_input)
avg_monthly_miles_input = input("Please enter the average number of miles driven per month: ")
fuel_cost_input =(input("Please enter the cost of the fuel per gallon: $"))
cost_float = float(fuel_cost_input)

car_mpg = int(car_float)
avg_monthly_miles = int(avg_monthly_miles_input)
fuel_cost = int(cost_float)


total_gallons = avg_monthly_miles/car_float
float_gallons = float(total_gallons)
total_fuel_cost = float_gallons * cost_float
float_total_cost = float(total_fuel_cost)
print()

print("Given the price of fuel at ${:.2f}/gallon and {} miles/month traveled:\n".format(cost_float, avg_monthly_miles))

print("Gallons used each month: {:.1f}".format(float_gallons))
print("Monthly cost of fuel: ${:.2f}".format(float_total_cost))
