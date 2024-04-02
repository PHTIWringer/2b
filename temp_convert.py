# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# Date: 04/02/2024
# Description: Asks the user for a Celsius temperature and converts it to Fahrenheit

print("Please enter a Celsius temperature")
celsius_num = float(input())

celsius_to_fahrenheit = ((9 / 5) * celsius_num + 32)

print("The equivalent Fahrenheit temperature is:")
print(celsius_to_fahrenheit)
