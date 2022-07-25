import os

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {
}

for x in student_scores:
    name = x
    score = student_scores[x]
    if score <= 100 and score >= 91:
        score = "Outstanding"
    elif score <=90 and score >= 81:
        score = "Exceeds Expectations"
    elif score <=80 and score >= 71:
        score = "Acceptable"
    else:
        score = "Fail"
    grade = name + score
    student_grades[name] = score  

print(student_grades)
os.system('pause')