import json
import myfile
import validate
class Student:

    def display_abstracted(self):
        """this function displays abstracted data of student to student
        """
        first,last=input("Enter full name of student for student's details:").split()
        roll=input("Enter roll number of student:")
        first=first.lower()
        last=last.lower()
        result=myfile.open_in_read_mode()
        for record in result:
            if record["first name"]==first and record["last name"]==last and record["roll no"]==roll:
                print(f"Name:{record['first name'] +' '+ record['last name']}")
                print(f"Email:{record["email address"]}")
                print(f"Marks:{record["marks"]}")
                print(f"total:{record["marks"]["total"]}")
                print(f"percent:{record["marks"]["total"]/len(record["marks"])}%")
                break
            else:
                print("Invalid Name/Roll Number!!!")
                break
                
    
    def pass_fail_calculation(self):
        """this function checks pass and fail of student
        """
        try:
            first,last=input("Enter full name of student for student's details:").split()
            roll=input("enter roll number of student ")
            first=first.lower()
            last=last.lower()
            result=myfile.open_in_read_mode()
            for record in result:
                if (record["first name"].lower() == first and 
                    record["last name"].lower() == last and 
                    record["roll no"] == roll):
                    
                    failed_subjects = [subject for subject, marks in record["marks"].items() if marks < 40]
                    
                    if failed_subjects:
                        print(f"You failed in {', '.join(failed_subjects)}")
                    else:
                        print("Congratulation!!! You passed in all subjects")
                        return
                else:
                    print("Invalid Name/Roll Number!!!")
                    break
        
        except FileNotFoundError:
                print("No data file found.")

    def highest_lowest_scores(self):
        """this function displats highest or lowest of a subject
        """
        subject=input("Enter subject to check highest and lowest score:")
        try:
            json_data=myfile.open_in_read_mode()

            list1=[]
            for record in json_data:
                for key,value in (record["marks"].items()):
                    if key==subject:
                        list1.append(value)
                lowest=min(list1)
                highest=max(list1)
            print(f"Highest score in {subject} is {highest} and lowest score is {lowest}")
        except ValueError:
            print("Subject not found!!")
    
    def rank_calcualtion(self):
        """this function calculate rank and display to user 
        """
        with open("Data files/data.json", "r") as file:
            json_data = json.load(file)
        sorted_stu = sorted(json_data , key = lambda x:x["marks"]["total"] , reverse=True)
        for i, student in enumerate(sorted_stu):
            print(f"rank : {i+1}   Name:{student["first name"]} {student["last name"]}  Total:{student["marks"]["total"]}")

   
if __name__=="__main__": 
    student = Student()
    print("Enter......")
    options = int(input("1.For Displaying Student's Information\n2.For pass or fail calculation \n3.For highest and lowest in a subject\n4.rank calculation\n"))
    if options == 1:
        student.display_abstracted()
    elif options == 2:
        student.pass_fail_calculation()
    elif options == 3:
        student.highest_lowest_scores()
    elif options == 4:
        student.rank_calcualtion()
    else:
        print("Enter valid input!")