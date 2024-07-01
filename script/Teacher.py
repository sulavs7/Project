import json
import os
import myfile
import validate
import teacher_display
class Teacher:
    def __init__(self):
        self.first = None
        self.last = None
        self.phone = None
        self.email = None
        self.address = None
        self.marks = None
    def teacher_authentication(self):
        try:
             with open("Data files/teacher_data.json","r") as file:
                json_data=json.load(file)
        except FileNotFoundError:
            json_data=[]
            print("\nNo teacher data found. Please add teacher data.")
            teacher_display.add_teacher_data_to_json_file()
        except json.JSONDecodeError:
            json_data=[]
            print("\nNo teacher data found. Please add teacher data.")
            teacher_display.add_teacher_data_to_json_file()
        print("______TEACHER LOGIN________")
        t_first,t_last = input("Enter name: ").split()
        teacher_id = input("Enter your teacher ID: ")

        with open("Data files/teacher_data.json","r") as file:
                json_data=json.load(file)
        for record in json_data:
            if record["teacher id"]==teacher_id and record["first name"]==t_first and record['last name']==t_last:
                return True

    def teacher_info(self):
        teacher_display.add_teacher_data_to_json_file()
    def display_all_teacher(self):
        teacher_display.display_all_teacher_data()
    def display_detail_of_one_teacher(self):
        teacher_display.detail_of_teacher()
    def delete_teacher_record(self):
        teacher_display.delete_items()
    

    
    def add_marks(self):
        python=int(input("Enter marks of python:"))
        c=int(input("Enter marks in c:"))
        java=int(input("Enter marks in java:"))
        php=int(input("Enter marks in php:"))
        total=python+c+java+php
        marks_info={
            "python":python,
            "c":c,
            "java":java,
            "php":php
        }
        marks_info["total"]=total
        return marks_info
    def data_input(self):
        print("Enter the data of student to store:")
        self.first, self.last = input("Full Name:").split()

        self.roll = input("Roll Number:")
        validate.roll_validate(self.roll)

        self.email = input("Email:")
        validate.email_validate(self.email)

        self.phone = input("Phone Number:")
        validate.phone_validate(self.phone)

        self.address = input("Address:")
        marks_info=self.add_marks()

        student_info = {
            "first name": (self.first).lower(),
            "last name": (self.last).lower(),
            "roll no": self.roll,
            "email address": self.email,
            "phone number": self.phone,
            "Address": (self.address).lower()
        }
        student_info["marks"]=marks_info  #append marks to the dictionary
        # Ensure the directory exists
        os.makedirs("Data files", exist_ok=True)

        # Append new data
        result=myfile.append_student_to_json_file(student_info)
        print(result)
    
    def display_all(self):
        try:
            json_data=myfile.open_in_read_mode()
            for record in json_data:
                print(f"\nName:{record['first name'] +' '+ record['last name']}")
                print(f"Roll Number:{record["roll no"]}")
                print(f"Email:{record["email address"]}")
                print(f"Phone Number:{record["phone number"]}")
                print(f"Address:{record["Address"]}")
                print(f"Marks:{record["marks"]}\n")

                
        except FileNotFoundError:
            print("No data file found.")
        except json.JSONDecodeError:                    #for missing commas and brackets in json file 
            print("Data file is empty or corrupted.")
    
       
    def detail_of_student(self):
        opt=int(input("Enter\n 1.To search by name of student\n 2.To search by roll number:\n"))

        if opt==1:
            first,last=input("Enter full name of student:").split()
            first=first.lower()
            last=last.lower()
            json_data=myfile.open_in_read_mode()
            for record in json_data:
                if record["first name"]==first and record[("last name")]==last:
                    print(f"\nName:{record['first name'] +' '+ record['last name']}")
                    print(f"Roll Number:{record["roll no"]}")
                    print(f"Email:{record["email address"]}")
                    print(f"Phone Number:{record["phone number"]}")
                    print(f"Address:{record["Address"]}")
                    print(f"Marks:{record["marks"]}")
                    print(f"total:{record["marks"]["total"]}")
                    print(f"percent:{record["marks"]["total"]/len(record["marks"])}%\n")

        else:
            Roll=input("Enter the roll number of student for details:")
            result=myfile.open_in_read_mode()
            for record in result:
                if record["roll no"]==Roll:
                    print(f"\nName:{record['first name'] +' '+ record['last name']}")
                    print(f"Roll Number:{record["roll no"]}")
                    print(f"Email:{record["email address"]}")
                    print(f"Phone Number:{record["phone number"]}")
                    print(f"Address:{record["Address"]}")
                    print(f"Marks:{record["marks"]}")
                    print(f"total:{record["marks"]["total"]}")
                    print(f"percent:{record["marks"]["total"]/len(record["marks"])}%\n")
                    

    def delete_items(self):
        first,last=(input("enter student's name to delete their record:")).split()
        roll=input("Enter Roll number:")
        json_data=myfile.open_in_read_mode()
        list1=[]
        for record in json_data:
            dict1={}
            if record["first name"]==first and record["last name"]==last and record["roll no"]==roll:
                continue
            for key,value in record.items():
                dict1[key]=value
            list1.append(dict1)
        with open("Data files\data.json","w") as file:
            json.dump(list1,file,indent=4)
        print("Data removed succesfully!!")

        

if __name__=="__main__": 
    teach=Teacher()
    if not teach.teacher_authentication():
        print("Name or ID of teacher doesn't match.")
        exit()
    print("Enter......")
    options = int(input("1.For student Data Input\n2.For Displaying student Data\n3.For Search Student\n4.For deleting record of student\n5.for teacher data input\n6.for displaying teacher data\n7.for searching teacher\n8.for deleting teacher's data\n"))
    if options == 1:
        teach.data_input()
    elif options == 2:
        teach.display_all()
    elif options == 3:
        teach.detail_of_student()
    elif options==4:
        teach.delete_items()
    elif options==5:
        teach.teacher_info()
    elif options==6:
        teach.display_all_teacher()
    elif options==7:
        teach.display_detail_of_one_teacher()
    elif options==8:
        teach.delete_teacher_record()
    else:

        print("Enter valid input!")
