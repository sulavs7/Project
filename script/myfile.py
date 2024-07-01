import os
import json

def open_in_read_mode():
    """
    to open file in read mode
    """
    with open("Data files/data.json", "r") as file:
            json_content = json.load(file)
            return json_content
    
def append_student_to_json_file(dictionary):
    """
    append student to json file

    Args:
          accepts dictionary

    Returns:
        return dictionary 
    """
    try:
        with open("Data files/data.json","r") as file:
            json_content=json.load(file)
    except FileNotFoundError:
        json_content=[]
    except json.JSONDecodeError:
        json_content=[]
    json_content.append(dictionary)

    # Write updated data back to the file
    with open("Data files/data.json", "w") as file:
        json.dump(json_content,file,indent=4)
    
    return ("Data successfully written to the file.")


def append_teacher_to_json_file(dictionary):
    try:
        with open("Data files/teacher_data.json","r") as file:
            json_content=json.load(file)
    except FileNotFoundError:
        json_content=[]
    except json.JSONDecodeError:
        json_content=[]
    json_content.append(dictionary)

    # Write updated data back to the file
    with open("Data files/teacher_data.json", "w") as file:
        json.dump(json_content,file,indent=4)
    
    return ("Data successfully written to the file.")


