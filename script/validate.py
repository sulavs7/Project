import json

def email_validate(emails):
    if ("@gmail.com") not in emails:
            raise ValueError("Enter valid email")

def phone_validate(phone):
    if (len(phone)>10):
            raise ValueError("Phone Number cannot be greater than 10 digit")

def roll_validate(roll):
    try:
        with open("Data files/data.json", "r") as file:
                json_content = json.load(file)

        for items in json_content:
            if items["roll no"]==roll:
                raise ValueError("Roll Number is not unique.Please confirm your Roll number")
    except FileNotFoundError:
        json_content=[]
    except json.JSONDecodeError:
        json_content=[]

def teacher_id_validate(id):
    with open("Data files/teacher_data.json", "r") as file:
            json_content = json.load(file)
    for items in json_content:
        if items["teacher id"]==id:
            raise ValueError("Roll Number is not unique.Please confirm your Roll number")