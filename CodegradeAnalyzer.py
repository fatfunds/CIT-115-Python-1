# Grade Analyzer Program
#Author: LZ
#Date: 4/5/25


# Prompt for the person's name
sName = input("Enter the name of the student: ")

# Prompt for 4 test scores and ensure they are whole numbers (non-negative)
iTest1 = int(input("Enter the first test score: "))
iTest2 = int(input("Enter the second test score: "))
iTest3 = int(input("Enter the third test score: "))
iTest4 = int(input("Enter the fourth test score: "))

# Check if any of the test scores are less than 0
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

# Prompt to determine if the lowest grade should be dropped
drop_lowest = input(f"{sName}, Do you want to drop the lowest grade? (Y/N): ")

# Validate the Drop Lowest input (must be Y or N)
if drop_lowest not in ['Y', 'N']:
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Calculate the average based on whether the lowest grade is dropped or not
if drop_lowest == 'Y':
    # Find the lowest grade WITHOUT using min() or lists... :)
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        avg_score = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        avg_score = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        avg_score = (iTest1 + iTest2 + iTest4) / 3
    else:
        avg_score = (iTest1 + iTest2 + iTest3) / 3
else:
    # Average all 4 test scores
    avg_score = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Determine the grade based on the average score
if avg_score >= 97.0:
    sGrade = "A+"
elif avg_score >= 94.0:
    sGrade = "A"
elif avg_score >= 90.0:
    sGrade = "A-"
elif avg_score >= 87.0:
    sGrade = "B+"
elif avg_score >= 84.0:
    sGrade = "B"
elif avg_score >= 80.0:
    sGrade = "B-"
elif avg_score >= 77.0:
    sGrade = "C+"
elif avg_score >= 74.0:
    sGrade = "C"
elif avg_score >= 70.0:
    sGrade = "C-"
elif avg_score >= 67.0:
    sGrade = "D+"
elif avg_score >= 64.0:
    sGrade = "D"
elif avg_score >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

# Output the results
print(f"\nStudent Name: {sName}")
print(f"Calculated Average: {avg_score:.1f}")
print(f"Letter Grade: {sGrade}")
