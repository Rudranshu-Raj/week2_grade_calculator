def calculate_grade(marks):
    """Calculate grade and return an encouraging message."""

    if marks >= 90:
        return "A", "Excellent work! Keep up the outstanding performance!"
    elif marks >= 80:
        return "B", "Great job! Keep working hard and aim even higher!"
    elif marks >= 70:
        return "C", "Good effort! A little more practice can improve your score."
    elif marks >= 60:
        return "D", "You passed! Keep practicing and you can do even better."
    else:
        return "F", "Don't give up! Learn from your mistakes and keep trying."


def get_valid_marks():
    """Get valid marks between 0 and 100."""

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input. Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():

    # Get student name
    name = input("Enter student name: ").strip()

    # Get valid marks
    marks = get_valid_marks()

    # Calculate grade
    grade, message = calculate_grade(marks)

    # Display result
    
    print(f"Student Name : {name}")
    print(f"Marks        : {marks:g}/100")
    print(f"Grade        : {grade}")
    print(f"Message      : {message}")


main()
