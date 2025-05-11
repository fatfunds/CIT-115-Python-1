# Author: LZ
# Date: 04/13/2025

# === INPUT FUNCTIONS ===
def get_positive_float(sPrompt):
    # Prompt for a positive float (or 0 for goal) with validation.
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue < 0:
                print("Error: Value cannot be negative.")
            else:
                return fValue
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_positive_nonzero_float(sPrompt):
    # Prompt for a positive non-zero float with validation.
    while True:
        try:
            fValue = float(input(sPrompt))
            if fValue <= 0:
                print("Error: Value must be greater than 0.")
            else:
                return fValue
        except ValueError:
            print("Error: Please enter a numeric value.")

def get_positive_nonzero_int(sPrompt):
    # Prompt for a positive non-zero integer with validation.
    while True:
        try:
            iValue = int(input(sPrompt))
            if iValue <= 0:
                print("Error: Value must be greater than 0.")
            else:
                return iValue
        except ValueError:
            print("Error: Please enter a whole number.")

# === MAIN PROGRAM FUNCTION ===
def main():
    # USER INPUT SECTION
    fDeposit = get_positive_nonzero_float("Enter the initial deposit amount: $")
    fInterestRatePercent = get_positive_nonzero_float("Enter the annual interest rate percentage (e.g., 5 for 5%): ")
    iNumMonths = get_positive_nonzero_int("Enter the number of months to calculate: ")
    fGoal = get_positive_float("Enter your savings goal amount (can be 0): $")

    # CALCULATE MONTHLY INTEREST RATE
    fMonthlyRate = (fInterestRatePercent / 100) / 12

    # CALCULATE COMPOUND INTEREST MONTH BY MONTH
    print("\nMonthly Compounded Balance:\n")
    fBalance = fDeposit  # Reset to original deposit
    for iMonth in range(1, iNumMonths + 1):
        fInterest = fBalance * fMonthlyRate
        fBalance += fInterest
        print(f"Month {iMonth}: ${fBalance:,.2f}")

    # CALCULATE HOW MANY MONTHS TO REACH GOAL
    if fGoal == 0 or fBalance >= fGoal:
        print("\nNo savings goal to reach or already reached during the term.")
    else:
        fBalance = fDeposit  # Reset again
        iMonthCount = 0
        while fBalance < fGoal:
            fBalance += fBalance * fMonthlyRate
            iMonthCount += 1
        print(f"\nIt will take {iMonthCount:,} months to reach your goal of ${fGoal:,.2f}.")

main()
