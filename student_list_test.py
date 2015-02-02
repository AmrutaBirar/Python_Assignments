# This program creates five student objects and
# stores them in a list.

import student

#Global constants for menu choices
LOOK_UP = 1
ADD_NEW = 2
EDIT_GPA = 3
EDIT_GRADE = 4
PRINT = 5
QUIT = 6

def main():
     
     #students = make_list()
     choice = 0
     # Display the data in the list.
     #print('Here is the data you entered:')
     #display_list(students)
     while choice != QUIT:
         choice = get_choice()
         #processing the choice
         if choice == LOOK_UP:
             look_up(students)
         elif choice == ADD_NEW:
             add_new(students)
         elif choice == EDIT_GPA:
             edit_gpa(students)
         elif choice == EDIT_GRADE:
             edit_grade(students)
         elif choice == PRINT:
             display_list(students)


# The make_list function gets data from the user
# for five students. The function returns a list
# of student objects containing the data.

def make_list():
     # Create an empty list.
     student_list = []

     # Add five student objects to the list.
     print('Enter data for five students.')
     for count in range(1, 3):
         # Get the student data.
         print('Student number ' + str(count) + ':')
         name = input('Enter the Name: ')
         s_id = input('Enter the Student ID: ')
         gpa = float(input('Enter the GPA: '))
         exgrade = input('Enter the expected grade : ')
         time = input('Full time - F or Part time - P ?')
         print()
         # Create a new student object in memory and
         # assign it to the student_instance variable.
         student_instance = student.Student(name,s_id,gpa,exgrade,time)
         # Add the object to the list.
         student_list.append(student_instance)

     # Return the list.
     return student_list
    
def get_choice():
    print("\n You can select any of the following operation you want to perform on Student Data")
    print("1.Look up and print the student GPA")
    print("2. Add a new student to the class")
    print("3. Change the GPA of a student")
    print("4. Change the expected grade of a student")
    print("5. Print the data of all the students in a tabular format")
    print("6. Quit the program")
    choice = int(input("Enter your choice :: "))
    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
         choice = int(input('Enter a valid choice: '))
    return choice

def look_up(student_instance):
    search = input("Enter the name of the student  whose grade you want to know : ")
    print(student_instance)
    try:
        if search in student_instance:
            print(search,"student Present in the list,Grade - ")
        else:
            print(search,"student not found !")
            
    except ValueError:
        print("Error - Student not found in the list")

# The display_list function accepts a list containing
# student objects as an argument and displays the
# data stored in each object.

def display_list(student_list):
     print("\tName  \tStudentID  \tGPA  \t  Expected Grade  \tStatus")
     print("====================================================================")
     for item in student_list:
         print("\t",item.get_name(),"\t",item.get_student_id(),"\t\t",item.get_gpa(),"\t\t",item.get_exgrade(),"\t",item.get_time())
         
# Call the main function.
main()
