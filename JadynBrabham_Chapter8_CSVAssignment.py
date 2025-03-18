# Jadyn Brabham
# Chapter 8, CSV Assignment
# This program is designed for an instructor to input grades of
# students for 3 exams. The program will store the data in a CSV file
# and allow the instructor to view the data in tabular format.
# The user will be prompted to input the number of students,
# their first and last names, and their grades for the exams.
# Then it saves the data to the CSV file and displays the
# contents of the file in a table.

import csv

# The write_grades() function prompts the user for the number
# of students, their first and last name, and their grades on the
# exams. Then it writes the input data to the CSV file.
def write_grades():
    # Ask the instructor for the number of students
    num_students = int(input("Enter the number of students: "))

    # Open grades.csv in write mode
    with open('grades.csv.py', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Collect data for each student and write it to the CSV file
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            try:
                exam_1 = int(input("Enter the grade for Exam 1: "))
                exam_2 = int(input("Enter the grade for Exam 2: "))
                exam_3 = int(input("Enter the grade for Exam 3: "))
            except ValueError:
                print("Please enter valid integer grades.")
                return

            # Write student data to the CSV file
            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])

    print("Grades have been written to grades.csv.py.")

# The read_grades() function opens the CSV file in read mode,
# skips the header, and displays the data in a tabular format.
def read_grades():
    # Open grades.csv in read mode
    with open('grades.csv.py', mode='r') as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Print the table header
        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<8}"
              f"{'Exam 2':<8}{'Exam 3':<8}")
        print("-" * 55)

        # Iterate through each row of the CSV file and print the data
        for row in reader:
            first_name, last_name, exam_1, exam_2, exam_3 = row
            print(f"{first_name:<15}{last_name:<15}{exam_1:<8}"
                  f"{exam_2:<8}{exam_3:<8}")

# The main function calls the write_grades() and read_grades() functions.
def main():
    # Call the function to write data to grades.csv
    write_grades()
    # Call the function to read and display the data from grades.csv
    read_grades()

if __name__ == "__main__":
    main()