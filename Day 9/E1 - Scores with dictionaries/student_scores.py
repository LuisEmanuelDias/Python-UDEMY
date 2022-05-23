student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
scores={
    "Outstanding":range(91,101),
    "Exceeds Expectations": range(81,91),
    "Acceptable":range(71,81),
    "Fail":range(0,71)
}
student_grades ={}
for m,n in student_scores.items():
    for k,l in scores.items():
        if (n in l):
            student_grades[m] = k 

#TODO-2: Write your code below to add the grades to student_grades.👇

# 🚨 Don't change the code below 👇
print(student_grades)
