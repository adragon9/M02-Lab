# Alexander L
# M02-Lab, main.py
# This will get a list of students and then return who is on the Dean's List and who is on the Honor Roll a

if __name__ == '__main__':
    # Variable initialization
    student_last_name = [""]
    student_first_name = [""]
    student_GPA = []
    student_id = []
    dean_list = []
    honor_roll = []
    every_other_student = []
    iterator = 0
    # Input loop
    while student_last_name[iterator - 1].upper() != "ZZZ":
        if iterator == 0:
            student_last_name[iterator] = input("Enter student's last name (enter: 'ZZZ' to quit): ")
        else:
            student_last_name.append(input("Enter student's last name (enter: 'ZZZ' to quit): "))

        # Terminate loop early
        if student_last_name[iterator].upper() == "ZZZ":
            break

        if iterator == 0:
            student_first_name[iterator] = input("Enter student's first name: ")
        else:
            student_first_name.append(input("Enter student's first name: "))

        student_GPA.append(float(input("Enter student's GPA: ")))
        student_id.append(iterator)
        iterator += 1

    print(student_GPA)
    
    for i in range(len(student_last_name) - 1):
        print(i)
        if student_GPA[i] >= 3.5 :
            dean_list.append(format("id: " + str(student_id[i]) + " " + student_last_name[i]+ ", " + student_first_name[i] + " GPA: " + str(student_GPA[i]) + " Student is on the Dean's List!"))
        elif student_GPA[i] >= 3.25 and student_GPA[i] < 3.5:
            honor_roll.append(format("id: " + str(student_id[i]) + " " + student_last_name[i] + ", " + student_first_name[i] + " GPA: " + str(student_GPA[i]) + " Student is on the Honor Roll!"))
        else:
            every_other_student.append(format("id: " + str(student_id[i]) + " " + student_last_name[i] + ", " + student_first_name[i] + " GPA: " + str(student_GPA[i]) + " Student exists"))

    # Out put's the results
    print("--- Dean's List ---")
    for i in range(len(dean_list)):
        print(dean_list[i])

    print("--- Honor Roll ---")
    for i in range(len(honor_roll)):
        print(honor_roll[i])

    print("--- Existing Students ---")
    for i in range(len(every_other_student)):
        print(every_other_student[i])