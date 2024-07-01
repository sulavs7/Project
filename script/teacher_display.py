import validate
import os
import json
import myfile
def add_teacher_data_to_json_file():
    """this function adds teacher data to json file
    """
    print("Enter the details of Teacher to store:")
    first,last = input("Full Name:").split()

    teacher_id = input("Enter teacher ID:")
    validate.teacher_id_validate(teacher_id)

    email = input("Email:")
    validate.email_validate(email)

    phone = input("Phone Number:")
    validate.phone_validate(phone)

    address = input("Address:")
    teacher_info={
        "first name":first,
        "last name": last,
        "teacher id": teacher_id,
        "email address": email,
        "phone number": phone,
        "Address": address

    }
    os.makedirs("Data files", exist_ok=True)
        # Append new data
    result=myfile.append_teacher_to_json_file(teacher_info)
    print(result)

def display_all_teacher_data():
    """this function displays teacher data 
    """
    try:
        with open("Data files/teacher_data.json", "r") as file:
            json_data = json.load(file)
        for record in json_data:
            
            print(f"\nName:{record['first name'] +' '+ record['last name']}")
            print(f"Roll Number:{record["teacher id"]}")
            print(f"Email:{record["email address"]}")
            print(f"Phone Number:{record["phone number"]}")
            print(f"Address:{record["Address"]}")
            
    except FileNotFoundError:
        print("No data file found.")
    except json.JSONDecodeError:                    #for missing commas and brackets in json file 
        print("Data file is empty or corrupted.")


def detail_of_teacher():
    """displays teacher's data
    """
    opt=int(input("Enter\n 1.To search by name of teacher\n 2.To search by teacher id:\n"))

    if opt==1:
        first,last=input("Enter full name::").split()
        first=first.lower()
        last=last.lower()
        
        with open("Data files/teacher_data.json", "r") as file:
            json_data = json.load(file)

        for record in json_data:
            if record["first name"]==first and record[("last name")]==last:
                print(f"Name:{record['first name'] +' '+ record['last name']}")
                print(f"Teacher ID:{record["teacher id"]}")
                print(f"Email:{record["email address"]}")
                print(f"Phone Number:{record["phone number"]}")
                print(f"Address:{record["Address"]}")
                print("\n")
    else:
        t_id=input("Enter teacher's id for details:")
        with open("Data files/teacher_data.json", "r") as file:
            record= json.load(file)
        for record in result:
            if record["teacher id"]==t_id:
                print(f"Name:{record['first name'] +' '+ record['last name']}")
                print(f"Email:{record["email address"]}")
                print(f"Phone Number:{record["phone number"]}")
                print(f"Address:{record["Address"]}")
                print("\n")
def delete_items():
    """delete teacher record
    """
    first,last=(input("enter teacher's name to delete their record:")).split()
    t_id=input("Enter teacher ID:")
    with open("Data files/teacher_data.json", "r") as file:
            json_data = json.load(file)
    list1=[]
    for record in json_data:
        dict1={}
        if record["first name"]==first and record["last name"]==last and record["teacher id"]==t_id:
            continue
        for key,value in record.items():
            dict1[key]=value
        list1.append(dict1)
    with open("Data files/teacher_data.json","w") as file:
        json.dump(list1,file,indent=4)
    print("Data Deleted Succesfully!!")
