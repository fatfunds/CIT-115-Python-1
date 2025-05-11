# Author: LZ
# Date: 5/7/25
# Program: BDJ Real Estate Sales Analyzer
# Description: This program collects property sales values and displays summary statistics
#              including min, max, total, average, median, and commission.

# Function to get a validated, positive float input from the user
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Sales value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Function to manually compute the median from a sorted list
def getMedian(sales_list):
    count = len(sales_list)
    mid = count // 2
    if count % 2 == 1:
        return sales_list[mid]  # Odd: middle element
    else:
        return (sales_list[mid - 1] + sales_list[mid]) / 2  # Even: avg of two middle

# Main function that handles the full program logic
def main():
    print("=== BDJ Real Estate Sales Analyzer ===")
    sales = []

    # Repeated input loop
    while True:
        sale = getFloatInput("Enter property sales value: ")
        sales.append(sale)

        # Ask user if they want to enter another
        while True:
            again = input("Enter another value Y or N: ").strip().lower()
            if again in ["y", "n"]:
                break
            print("Invalid input. Please enter Y or N.")
        if again == "n":
            break

    # Sort the sales values from lowest to highest
    sales.sort()

    # Output each entry formatted as currency
    print("\n--- Sorted Sales Entries ---")
    for i, amount in enumerate(sales, start=1):
        print(f"Sale {i}: ${amount:,.2f}")

    # Calculate all summary values
    total = sum(sales)
    minimum = sales[0]
    maximum = sales[-1]
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    # Display summary results
    print("\n--- Sales Summary ---")
    print(f"Minimum Sale:    ${minimum:,.2f}")
    print(f"Maximum Sale:    ${maximum:,.2f}")
    print(f"Total Sales:     ${total:,.2f}")
    print(f"Average Sale:    ${average:,.2f}")
    print(f"Median Sale:     ${median:,.2f}")
    print(f"Commission (3%): ${commission:,.2f}")

# Run the program
main()
