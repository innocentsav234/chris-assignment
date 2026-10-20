overall_score = int(300)
number_of_subject = int(3)

student_name = input("Enter your name: ")
student_age = input("enter your age: ")
math_score = int(input("enter your score: "))
english_score = int(input("enter your score:"))
computer_score =int(input("enter your score:"))
total_score = math_score + english_score + computer_score
print(total_score) 
average_score = total_score / number_of_subject
print(average_score)
percentage_score = total_score/ overall_score * 100
print(percentage_score)
pass_mark = 10
if pass_mark >= math_score:
   print("math_score: failed")
else:
   print("math_score: passed") 
if pass_mark >= english_score:
   print("english_score: failed")
else: 
   print("english_score: passed") 
if  pass_mark >= computer_score:
    print("computer_score: failed")
else:
   print("computer_score: passed")
