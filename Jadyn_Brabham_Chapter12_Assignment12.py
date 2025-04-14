# Jadyn Brabham
# Chapter 12, Assignment 12
# This program will use numpy to analyze student grades stored in the grades.csv file.

import numpy as np

# The load_data function reads the CSV file and returns only specific columns.
def load_data(filename):
    # Load only the exam score columns
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, usecols=(2, 3, 4))
    return data

# The calculate_statistics function calculates the mean, median, standard deviation,
# minimum, and maximum of each exam and of all the exams combined.
def calculate_statistics(data):
    print("For each exam:")
    for i in range(data.shape[1]):
        exam = data[:, i]
        print(f"\nExam {i + 1} Statistics:")
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Standard Deviation: {np.std(exam):.2f}")
        print(f"Minimum: {np.min(exam)}")
        print(f"Maximum: {np.max(exam)}")

    print("\nOverall Statistics (All Exams Combined)")
    all_grades = data.flatten()
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")

# The pass_fail function determines how many of the exams were failed or passed.
def pass_fail(data):
    print("\nPass/Fail Per Exam")
    for i in range(data.shape[1]):
        exam = data[:, i]
        passed = np.sum(exam >= 60)
        failed = np.sum(exam < 60)
        print(f"Exam {i + 1}: Passed = {passed}, Failed = {failed}")

    print("\nOverall Pass Percentage (All Exams Combined)")
    total_grades = data.size
    total_passes = np.sum(data >= 60)
    pass_percentage = (total_passes / total_grades) * 100
    print(f"Pass Percentage: {pass_percentage:.2f}%")

# The main function opens the grades.csv file and runs the flow of the program.
def main():
    filename = 'grades.py'
    data = load_data(filename)

    print("First Few Rows of Data")
    print(data[:5])

    calculate_statistics(data)
    pass_fail(data)

if __name__ == "__main__":
    main()