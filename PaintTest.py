##Author: LZ
##Date: 4/25/25

# Function to get a positive, non-zero float input
def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt + ": "))
            if fValue <= 0:
                print("Error: Value must be positive and greater than zero.")
            else:
                return fValue
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Function to calculate total gallons needed
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    iGallons = int(fSquareFeet / fFeetPerGallon)
    if (fSquareFeet % fFeetPerGallon) != 0:
        iGallons += 1
    return iGallons

# Function to calculate labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

# Function to calculate labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

# Function to calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

# Function to determine sales tax rate based on state -- uses .upper() for all CAPS input. I hope this is allowed, if not I can make my own while loop to check for proper Capitalization!
def getSalesTax(sState):
    sState = sState.upper()
    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0

# Function to show cost estimate on screen and write to file
def showCostEstimate(sLastName, iTotalGallons, fTotalLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost):
    sFileName = sLastName + "_PaintJobOutput.txt"

    sOutput = (
        f"\n------ Paint Job Estimate ------\n"
        f"Gallons of paint: {iTotalGallons}\n"
        f"Hours of labor: {fTotalLaborHours:.1f}\n"
        f"Paint charges: ${fPaintCost:.2f}\n"
        f"Labor charges: ${fLaborCost:.2f}\n"
        f"Tax: ${fTaxAmount:.2f}\n"
        f"Total cost: ${fTotalCost:.2f}\n"
        f"--------------------------------\n"
    )

    print(sOutput)

    with open(sFileName, "w") as file:
        file.write(sOutput)

    print(f"File: {sFileName} was created.")

# Main program logic
def main():
    # Get input values
    fSquareFeet = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fFeetPerGallon = getFloatInput("Enter feet per gallon")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon")
    fLaborChargePerHour = getFloatInput("Labor charge per hour")

    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")

    # Perform calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fTotalLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)

    fSubtotal = fPaintCost + fLaborCost
    fTaxAmount = fSubtotal * fSalesTaxRate
    fTotalCost = fSubtotal + fTaxAmount

    # Show cost estimate and save to file
    showCostEstimate(sLastName, iTotalGallons, fTotalLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost)

# Call main function
if __name__ == "__main__":
    main()
