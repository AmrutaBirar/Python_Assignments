# Local Drivers License Exam Program
# Lab 8 - Amruta Birar

def main():
     correct_count = 0
     incorrect_count = 0
     incorrect_ans_list = []
     
     
     correct_ans_list = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
     print("\n Correct Answer list:",correct_ans_list)
     try:
             ans_file = open('user_ans.txt','r')
             user_ans = ans_file.readlines()
             ans_file.close()
             
             #Strip '\n' from each element 
             index = 0
             while index < len(user_ans):
                  user_ans[index] = user_ans[index].rstrip('\n')
                  index += 1
             print("\n Your answer list:",user_ans) 
             
             i = 0 
             while i < len(user_ans) :
                  if correct_ans_list[i] == user_ans[i] :
                       correct_count += 1
                       i += 1
                  else:
                       incorrect_count += 1
                       incorrect_ans_list.append(i+1) 
                       i += 1
             
             status(incorrect_count)
             print("\n Total number of corretly answered questions :",correct_count)
             print("\n Total number of incorrect answered questions :",incorrect_count)
             print('\n Incorrect question numbers :',incorrect_ans_list)
     except ValueError as err:
             print("Error:",err)
     except IOError as err:
             print("Error:",err)
     except NameError as err:
             print("Error:",err)
     except:
             print("Error occured")

def status(incorrect_count):
     if incorrect_count > 5:
          print("\n Result == Sorry you failed Driver License Exam,good luck next time!")
     else:
          print("\n Result == You passed the exam,Congratulations - Drive Safe !!")
     

main()
