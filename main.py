import os 
import json
import sys

if __name__=="__main__":
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_dir,"script"))

from script import *

def main():
    print("Welcome to Student and Teacher Management System!")

    while True:
        print("\nEnter your choice:")
        print("1. Student Operations")
        print("2. Teacher Operations")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                student_operations()
            elif choice == 2:
                teacher_operations()
            elif choice == 3:
                print("Exiting Program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def student_operations():
    student = Student()

    while True:
        print("\nStudent Operations:")
        print("1. Display Student Information")
        print("2. Pass/Fail Calculation")
        print("3. Highest and Lowest Scores in a Subject")
        print("4. Display Rank")
        print("5. Back to Main Menu")

        try:
            option = int(input("Enter option: "))

            if option == 1:
                student.display_abstracted()
            elif option == 2:
                student.pass_fail_calculation()
            elif option == 3:
                student.highest_lowest_scores()
            elif option == 4:
                student.rank_calcualtion()
            elif option == 5:
                break
            else:
                print("Invalid option. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def teacher_operations():

    teacher = Teacher()
    if not teacher.teacher_authentication():
        print("Name or ID of teacher doesn't match.")
        exit()
    while True:
        print("\nTeacher Operations:")
        print("1. Add Student Data")
        print("2. Display All Students")
        print("3. Search Student Details")
        print("4. Delete Student Details")
        print("5. Add Teacher Data")
        print("6. Display All Teacher's Data ")
        print("7. Search Teacher Details")
        print("8. Delete Teacher Details")
        print("9. Back to Main Menu")

        try:
            option = int(input("Enter option: "))

            if option == 1:
                teacher.data_input()
            elif option == 2:
                teacher.display_all()
            elif option == 3:
                teacher.detail_of_student()
            elif option == 4:
                teacher.delete_items()
            elif option == 5:
                teacher.teacher_info()
            elif option == 6:
                teacher.display_all_teacher()
            elif option == 7:
                teacher.display_detail_of_one_teacher()
            elif option == 8:
                teacher.delete_teacher_record()
            elif option == 9:
                break
            else:
                print("Invalid option. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


