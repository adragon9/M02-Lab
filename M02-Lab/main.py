# Alexander L
# M02-Lab, main.py
# This will get a list of students and then return who is on the Dean's List and who is on the Honor Roll

if __name__ == '__main__':
    student_LName = ""

    while student_LName.upper() != "ZZZ":
        student_LName = input("Enter Student's Last Name: ")
        
        if student_LName.upper() == "ZZZ":
            break
        
        student_FName = input("Enter Student's First Name: ")
        student_GPA = float(input("Enter Student's GPA: "))

        if student_GPA >= 3.5:
            print(student_LName + ", " + student_FName + " is on the Dean's List!")
        elif 3.25 <= student_GPA < 3.5:
            print(student_LName + ", " + student_FName + " is on the Honor Roll!")
        else:
            print(student_LName + ", " + student_FName + " has room for improvement!")