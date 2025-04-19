# Summative Assignment 02 
# John Kayode-Abusi
 
'''
Quarter of the Year 

Write a program that asks the user for a month as a number between 1 and 12. The program should display a message indicating whether the month is in the first quarter, the second quarter, the third quarter, or the fourth quarter of the year. Following are the guidelines: 

If the user enters either 1, 2, or 3, the month is in the first quarter. 

If the user enters a number between 4 and 6, the month is in the second quarter. 

If the number is either 7, 8, or 9, the month is in the third quarter. 

If the month is between 10 and 12, the month is in the fourth quarter. 

If the number is not between 1 and 12, the program should display an error. 

'''

month = int(input('enter month on number: '))

if month <= 3:
    print('the month is in the first quarter')
elif month <= 6:
    print('the month is in the second quarter')
elif month <= 9:
    print('the month is in third quarter')
elif month <= 12:
    print('the month is in fourth quarter')
else:
    print('error this is out of range')



'''
Roulette Wheel Colors 

On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows: 

Pocket 0 is green. 

For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black. 

For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red. 

For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black. 

For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red. 

Write a program that asks the user to enter a pocket number and displays whether the pocket is green, 
red, or black. The program should display an error message if the user enters a number that is outside the range of 0 through 36. 

pocket0 = 'green'
pocket1_10_odd = 'red'
pocket1_10_even = 'black'
pocket11_18_odd = 'black'
pocket11_18_even = 'red'
pocket19_28_odd = 'red'
pocket19_28_even = 'black'
pocket29_36_even = 'red'
pocket29_36_odd = 'black'

'''

askPocket = int(input("Enter a pocket number (0-36): "))

# Check for valid input
if askPocket < 0 or askPocket > 36:
    print("Error: Invalid pocket number. Please enter a number between 0 and 36.")
elif askPocket == 0:
    print('Pocket 0 is green')
elif 1 <= askPocket <= 10:
    if askPocket % 2 == 0:
        print(f"pocket {askPocket} is black.")
    else: 
        print(f"pocket {askPocket} is red.")
elif 11 <= askPocket <= 18:
    if askPocket % 2 == 0:
        print(f"pocket {askPocket} is red.")
    else:
        print(f"pocket {askPocket} is black.")
elif 19 <= askPocket <= 28:
    if askPocket % 2 == 0:
        print(f"pocket {askPocket} is red.")
    else:
        print(f"pocket {askPocket} is black.")
elif 29 <= askPocket <= 36:
    if askPocket % 2 == 0:
        print(f"pocket {askPocket} is red.")
    else:
        print(f"pocket {askPocket} is black.")



'''
Time Calculator 

Write a program that asks the user to enter several seconds and works as follows: 

There are 60 seconds in a minute. If the user enters more than or equal to 60 seconds, the program should convert the number of seconds to minutes and seconds. 

There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds. 

There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should convert the number of seconds todays, hours, minutes, and seconds.
'''


t_seconds = int(input("Enter the number of seconds: "))

seconds_in_minute = 60
seconds_in_hour = 3600
seconds_in_day = 86400

days = t_seconds // seconds_in_day
# Calculate days, hours, minutes, and seconds
days = t_seconds // seconds_in_day
remaining_seconds = t_seconds % seconds_in_day

hours = remaining_seconds // seconds_in_hour
remaining_seconds %= seconds_in_hour

minutes = remaining_seconds // seconds_in_minute
seconds = remaining_seconds % seconds_in_minute

# Display the result based on the size of input
print("\nTime breakdown:")
if t_seconds >= seconds_in_day:
    print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
elif t_seconds >= seconds_in_hour:
    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
elif t_seconds >= seconds_in_hour:
    print(f"{minutes} minute(s), {seconds} second(s)")
else:
    print(f"{t_seconds} second(s)")


