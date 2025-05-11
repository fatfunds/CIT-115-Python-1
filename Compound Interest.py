#Author: LZ
#Date 2/18/2025

#Constants
fPV= float(input("Enter the Starting Principal: "))
fR= float(input("Enter your annual interest rate: ")) / 100
fT= int(input("How many times per year is the interest compounded: "))
fM= float(input("For how many years will the account earn interest: "))



#Calculations
fFV = fPV * (1 + fR / fM) ** (fM * fT)


#Outprint: f-string print
print(f"Your Future value after 2 years is: ${fFV:<10,.2f}")
