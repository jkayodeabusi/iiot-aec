# print("Hello Introduction to programming")

# print('programming')
# print('is')
# print('fun')

# print(12, 13)
# print('john'  +  'kayode')

# print('Hello')
# print('intofuction to')
# print('programming 2025')
# print('Hello' '\n' 'Introduction to' '\n' 'programming 2025')

# print(12 + 13)
# print(((12+3)*3)/4)
# name = ('Hello John')
# value = 12 
# print(name, value)

# a = 3
# b = 4
# c = 5
# print(a*b/c)

# room1_temp = 28.8
# # room 2
# room2_temp = 29.8
# #camel case variable name
# myName = 'John'
# room1_temp, room2_temp, myName = 16.5, 25.8, 'John'
# print('room 1 temperature is', room1_temp)
# print('room 2 temperature is', room2_temp)
# print('my name is', myName)

# # another seg
# variable1 = 35
# variable2 = 45.69
# variable = 'chaplainIIoT'
# print(variable1, variable2, variable)

# #using function
# variable1 = int(35)
# variable2 = float(45.69)
# variable3 = str(12)
# print('this values are', variable1, variable2, variable3)

# # practice for tofays class - 3rd march 2025
# variable1 = 47.89
# variable2 = 'Montreal'
# variable3 = 147
# variable4 = variable1 + variable3
# print(variable1, variable2, variable3, variable4)

# # using the input function
# valueOne = float(input('enter value one'))
# valueTwo = float(input('enter value two'))
# multiResult = valueOne * valueTwo
# print('the result is', multiResult)

# #class work
# Write a Python program that:
# 1. Takes the user's yearly income as input.
# 2. Calculates the federal & provincial income tax based on 2024 Canadian tax brackets.
# 3. Applies basic personal amount deduction.
# 4. Outputs the total tax owed and net income.
# For this program, consider the Federal income tax is flat 13% and Quebec income tax is flat 22%. In
# addition, the basic personal amount deduction for everyone is 10,924. Please consider the person’s
# income before tax is 35K CAD or more.
# Also, consider that after the deduction of the basic personal amount from the yearly income,
# Federal and Quebec taxes will be applied on the rest of the income. After deduction of the taxes
# from your income, please print the tax you owed and your net income in hand

# # calcilate taxes and netpay
# yearlyIncome = float(input('enter your total income'))
# personalAmtDeduction = float(10.924)
# federalTaxRate = 13/100
# quebecTaxRate =22/100
# taxableIncome = yearlyIncome - personalAmtDeduction
# federalIcomeTax = taxableIncome * federalTaxRate
# quebecIncomeTax = taxableIncome * quebecTaxRate
# netpay = yearlyIncome - (federalIcomeTax + quebecIncomeTax)
# print(federalIcomeTax + quebecIncomeTax)
# print(netpay)

# # Get user input for yearly income
# yearlyIncome = float(input("Enter your total income: "))

# # Personal amount deduction
# personalAmtDeduction = 10.924  # Fixed amount

# # Federal & Quebec tax rates
# federalTaxRate = 13 / 100
# quebecTaxRate = 22 / 100

# # Calculate taxable income (income after deduction)
# taxableIncome = yearlyIncome - personalAmtDeduction

# # Calculate federal and Quebec income taxes
# federalIncomeTax = taxableIncome * federalTaxRate
# quebecIncomeTax = taxableIncome * quebecTaxRate

# # Calculate net pay after tax deductions
# netpay = yearlyIncome - (federalIncomeTax + quebecIncomeTax)

# # Print tax amounts and net pay
# print("Total Tax Deducted:", federalIncomeTax + quebecIncomeTax)
# print("Net Pay After Taxes:", netpay)


# Sales Prediction Program

# # enter the projected amount of total sales
# projected_sales = float(input("Enter the projected total sales amount: $"))
# # Calculate the profit as 23% of total sales
# profit = projected_sales * 0.23
# # Display the profit
# print(f"The estimated profit is: ${profit:.2f}")

# ----------------------------------------------

# # Pounds to Kilograms Converter

# # enter the mass in pounds
# pounds = float(input("Enter the mass of the object in pounds: "))
# # Convert to kilograms
# kilograms = pounds * 0.454
# # Display the result
# print(f"The mass of the object in kilograms is: {kilograms:.3f} kg")

# import math  # to use math.pi

# # Ask the user to enter the radius
# radius = float(input("Enter the radius of the circle: "))

# # Calculate area and circumference
# area = math.pi * radius ** 2
# circumference = 2 * math.pi * radius

# # Display the results
# print(f"Area of the circle: {area:.2f}")
# print(f"Circumference of the circle: {circumference:.2f}")


'''''
you are asked to develop a mini calculator program, where you will take two values as input from the user.
Values should eligible for decimal points.math
After taking the inputs ask for the user's choice, (take another value as input 1 for multilication) for division. 
perfom the operation inside the print  (formatted) function and print the result with at most 3 decimal points.pow
1. ask for value 1 and hold in variable 1;
2. ask value 2 and hold it in variable 2;
3. ask for user's choice and hold it in variable choice;
4. if (condition): if choice is 1 do multiplication;
5. if (condition): if choice is 2, do division

v1 = float(input ('enter value1'))
v2 = float(input('enter value2'))
uc = float(input('your choice'))
if uc == v1: 
    print(v1 * v2)
if uc == v2:
    print(v1 / v2)

''''''
# -----------------------------------------------------
temp = input('enter today temp')
if temp <-5:
    print('outside is very cold, wear jacket')
    else:

# ----------------------------------------
''
Let us consider you are working in a IoT company. 

The manager asked you to develop a program that will decide whether you should start the humidifier or not based on some pre-defined conditions:
 
0. ask the user to insert the room temperature, room humidity
 
1. if the room temperature goes lower than 8 degree centrigrade

do step 2, else step 3
 
2. If condition 1 statisfies, then you will check whether room humidity is less than 70. If yes, will start the humidifier, else start the heater
 
3. If condition 1 is not satisfied, ask the user to enter the temperature set in the monitor (a new temp variable). If it is greater than 20, ask the user to change it to 15; otherwise, tell the user to keep patience.


roomTemp = ('enter room temp')
roomHumid = ('enter room humid')
monitorTem = ('enter temp on the monitor')

if roomTemp < 8:
    if roomHumid < 70:
        print('start the humidfier')
        else('start the heater')
if roomTemp <! 8:  print(monitorTem)

'''
# ------------------------------------
'''
try:
    room_temp = float(input("Enter room temperature (°C): "))
    room_humidity = float(input("Enter room humidity (%): "))

    if room_temp < 8:
        if room_humidity < 70:
            print("Starting the humidifier.")
        else:
            print("Starting the heater.")
    else:
        monitor_temp = float(input("Enter temperature set on the monitor (°C): "))
        if monitor_temp > 20:
            print("Please change the monitor temperature to 15°C.")
        else:
            print("Please be patient.")

except ValueError:
    print("Invalid input. Please enter numeric values.")


'''

''''
temp = float(input('enter the outside temp'))

if temp < -5:
    print('outside is very cold, wear inter coat')
elif temp < 10:
    print('outside is cold, wear jacket')
elif temp >= 10:
    print('outside is warm, wear reqular cloth')
else:
    print('the input is wrong')
    
'''



# complex boolen

# pin = '123456'
# askPin = input('Enter your pin number')
# currTime = int(input('Enter the ccurrent hour'))

# if askPin == pin:
#     if currTime >= 8 and currTime <= 12:
#         print('You can access the phone')
#     else:
#         print('You can not access the phone')
# else:
#     print('Your pin is incorrect. You cannot access the phone')

# # more optimzed code




# grading system

# case1

score = int(input('Enter score'))

if score >= 90:
    print('Your grade is A')
elif score >= 80:
    print('Your grade is B')
elif score >= 70:
    print('Your grade is C')
elif score >= 60:
    print('Your grade is D')
else:
    print('Your grade is F')



# case2

# score = int(input('Enter score'))

# if score >= 90:
#     print('Your grade is A')
# elif score >= 80 and score < 90:
#     print('Your grade is B')
# elif score >= 70 and score < 80:
#     print('Your grade is C')
# elif score >= 60 and score < 70:
#     print('Your grade is D')
# else:
#     print('Your grade is F')




