#Author: LZ
#Date: 3/20/25

# Print welcome message
print("Welcome to my Temperature Converter:\n")

#Function-Converts Fahrenheit to Celsius & Vice Versa
def convert_temperature(sName, fTemp, sUnit):
    sFahrenheit = {"f", "F"}
    sCelsius = {"c", "C"}
    if sUnit in sFahrenheit:
        if fTemp > 212:
            print("Temperature cannot be greater than 212 Fahrenheit")
        else:
            fCelsius = (5.0 / 9) * (fTemp - 32)
            print(f"Hi {sName}, The Celsius equivalent of your temperature is: {fCelsius:.1f}C")
    elif sUnit in sCelsius:
        if fTemp > 100:
            print("Temperature cannot be greater than 100 Celsius")
        else:
            fFahrenheit = (9.0 / 5.0) * fTemp + 32
            print(f"Hi {sName}, The Fahrenheit equivalent of your temperature is: {fFahrenheit:.1f}F")
    else:
        print("Make sure to only use C or F to represent Celsius or Fahrenheit")
        exit()

#Main execuction-Inputs
sName = input("What is your name?: ")
fTemp = float(input("Enter a Temperature?: "))
sUnit = input("Are you using Fahrenheit (F) or Celsius (C)?: ")

convert_temperature(sName, fTemp, sUnit)
