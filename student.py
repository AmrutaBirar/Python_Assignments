
#The Student class holds information about student
class Student:
            def __init__(self,name,student_id,gpa,exgrade,time):
                    self.name = name
                    self.__student_id = student_id
                    self.__gpa = gpa
                    self.__exgrade = exgrade
                    self.__time = time

            #set method below sets the value to data attributes
            def set_name(self,name):
               self.name = name
            def set_student_id(self,student_id):
               self.__student_id = student_id
            def set_gpa(self,gpa):
               self.__gpa = gpa
            def set_exgrade(self,exgrade):
               self.__exgrade = exgrade
            def set_time(self,time):
               self.__time = time

            #get method below gets the value of the data attribute
            def get_name(self):
               return self.name
            def get_student_id(self):
               return self.__student_id
            def get_gpa(self):
               return self.__gpa
            def get_exgrade(self):
               return self.__exgrade
            def get_time(self):
               return self.__time

            # The _ _str_ _ method returns the object's state
            # as a string.
            '''def __str__(self):
               return "Name: " + self.name + \
                             "\nStudent ID: " + self.__student_id + \
                             "\nGPA: " + self.__gpa + \
                             "\nExpected Grade: " + self.__exgrade + \
                             "\nStatus: " + self.__time 
            '''
            def write_to_file(self):
                     student_file = open('student.txt','a')
                     student_file.write(str(self.name) + "\n")
                     student_file.write(str(self.__student_id) + "\n")
                     student_file.write(str(self.__gpa) + "\n")
                     student_file.write(str(self.__exgrade) + "\n")
                     student_file.write(str(self.__time) + "\n")
                     student_file.close()
                     print("Student data written into the student.txt file.")

            def add_new(self):
                print("Please enter the following data for adding a new student to the class")
                self.name = input("Enter student name")
                self.__student_id = input('Enter the Student ID: ')
                self.__gpa = float(input('Enter the GPA: '))
                self.__exgrade = input('Enter the expected grade : ')
                self.__time = input('Full time - F or Part time - P ?')
                print()
                student_file = open('student.txt','a')
                student_file.write(str(self.name) + "\n")
                student_file.write(str(self.__student_id) + "\n")
                student_file.write(str(self.__gpa) + "\n")
                student_file.write(str(self.__exgrade) + "\n")
                student_file.write(str(self.__time) + "\n")
                student_file.close()
                print("Student data written into the student.txt file.")
                
            def edit_gpa(self):
                found = False
                s_id = input("Enter student ID for editing GPA of student")
                student_file = open('student.txt','r')
                name = student_file.readline()
  
                for line in student_file:
                    name = name.rstrip('\n')
                    student_id = student_file.readline()
                    student_id = student_id.rstrip('\n')

                    student_gpa = student_file.readline()
                    student_gpa = student_gpa.rstrip('\n')
                    student_gpa = float(student_gpa)
                    if s_id == student_id:
                        newgpa = float(input("Enter the new gpa:"))
                        student_gpa = newgpa
                        print("Updated succsefully")
                    else:
                        print("No such student id exist!")
                            
                            
            def print_table(self):
               student_file = open('student.txt','r')
               name = student_file.readline()
               print("\tName  \tStudentID  \tGPA  \t  Expected Grade  \tStatus")
               print("====================================================================")
            
               
               for line in student_file :
                      #read the id feild
                      name = name.rstrip('\n')

                      student_id = student_file.readline()
                      student_id = student_id.rstrip('\n')

                      student_gpa = student_file.readline()
                      student_gpa = student_gpa.rstrip('\n')

                      student_exgrade = student_file.readline()
                      student_exgrade = student_exgrade.rstrip('\n')

                      student_time = student_file.readline()
                      student_time = student_time.rstrip('\n')

                      #print(student_id)
                      print("\t",name,"\t",student_id,"\t",student_gpa,"\t",student_exgrade,"\t",student_time)
                      name = student_file.readline()
               student_file.close()
            
