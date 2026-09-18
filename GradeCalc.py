homework = int(input("What was your score on Homework? "))
if homework > 100:
    print("The maximum score is 100!")
    homework = 100
elif homework < 0:
    print("The minimum score is 0!")   
    homework = 0 
lab = int(input("What was your score on Lab? "))
if lab > 100:
    print("The maximum score is 100!")
    lab = 100
elif lab < 0:
    print("The minimum score is 0!")   
    lab = 0 
quiz = int(input("What was your score on Quiz? "))
if quiz > 100:
    print("The maximum score is 100!")
    quiz = 100
elif quiz < 0:
    print("The minimum score is 0!")    
    quiz = 0
project_1 = int(input("What was your score on Project 1? "))
if project_1 > 100:
    print("The maximum score is 100!")
    project_1 = 100
elif project_1 < 0:
    print("The minimum score is 0!") 
    project_1 = 0
project_2 = int(input("What was your score on Project 2? "))
if project_2 > 100:
    print("The maximum score is 100!")
    project_2 = 100
elif project_2 < 0:
    print("The minimum score is 0!") 
    project_2 = 0
midterm_exam_1 = int(input("What was your score on Midterm Exam 1? "))
if midterm_exam_1 > 100:
    print("The maximum score is 100!")
    midterm_exam_1 = 100
elif midterm_exam_1 < 0:
    print("The minimum score is 0!") 
    midterm_exam_1 = 0
midterm_exam_2 = int(input("What was your score on Midterm Exam 2? "))
if midterm_exam_2 > 100:
    print("The maximum score is 100!")
    midterm_exam_2 = 100
elif midterm_exam_2 < 0:
    print("The minimum score is 0!") 
    midterm_exam_2 = 0 
final_exam = int(input("What was your score on Final Exam? "))
if final_exam > 100:
    print("The maximum score is 100!")
    final_exam = 100
elif final_exam < 0:
    print("The minimum score is 0!") 
    final_exam = 0 
weighted_grade_1 = (homework * 0.05 + lab * 0.03 + quiz * 0.03 + project_1 * 0.14 + project_2 * 0.20 + midterm_exam_1 * 0.13 + midterm_exam_2 * 0.17 + final_exam * 0.25)
weighted_grade_2 = (homework * 0.05 + lab * 0.03 + quiz * 0.03 + project_1 * 0.25 + project_2 * 0.30 + midterm_exam_1 * 0.06 + midterm_exam_2 * 0.11 + final_exam * 0.17)
print(f"In grade weighting system 1 your score is: {int(weighted_grade_1)}")
print(f"In grade weighting system 2 your score is: {int(weighted_grade_2)}")
if weighted_grade_1 > weighted_grade_2:
    final_grade = weighted_grade_1
else:
    final_grade = weighted_grade_2    
print(f"Your final grade is: {int(final_grade)}")