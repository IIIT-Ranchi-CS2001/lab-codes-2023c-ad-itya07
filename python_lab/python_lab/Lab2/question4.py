# Function to determine grade point and remark based on marks
def get_grade_point_and_remark(marks):
    if marks >= 90:
        return 10, "Excellent"
    elif marks >= 80:
        return 9, "Very Good"
    elif marks >= 70:
        return 8, "Good"
    elif marks >= 60:
        return 7, "Average"
    elif marks >= 50:
        return 6, "Below Average"
    elif marks >= 40:
        return 5, "Pass"
    else:
        return 0, "Fail"

# Main function to input student details and display them
def main():
    # Input student details at runtime
    name = input("Enter the student's name: ")
    roll_number = input("Enter the student's roll number: ")
    marks = float(input("Enter the marks secured in Mathematics (out of 100): "))
    grade_point, remark = get_grade_point_and_remark(marks)
    
    
    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Marks: {marks}")
    print(f"Grade Point: {grade_point}")
    print(f"Remark: {remark}")


if __name__ == "__main__":
    main()
