print ("Kumar")
age=78.78
bol=True
name="mukesh"
name="Google By"
print(bol)

first_name="Tony"
last_name=("Stark")
age=51
is_Genius=True
print(first_name)
print(last_name)
print(age)
print(is_Genius)

name=input('what is your name ')
print("Hello"+name)  

hero=input(" what is your super hero name")
print(' My superhero name is '+hero)

# typform
lastYear_Marks=input("My last year makrs is")
# typeform
# int(lastYear_Marks)
new_Marks=int(lastYear_Marks)+20
print(new_Marks)

# sum program
first = input("Enter first number")
second=input("enter second number")
sum=int(first)+ int(second)
print(sum)

String Useage
name = "Elon musk "
print(name.upper())
print(name)
print(name.lower())
print(name.find('S'))   #it return -1
print(name.find('usk'))
print(name.find('Elon'))

print(name.replace('musk','kumar'))
print(name)
print(name.replace('E', 'M'))
print('E' in name)
print('x' in name)
print('Elon' in name)

# Operators
print(6+8)
print(6*7)
print(5/10)
print(20//7)  #it will print only integer
print(6%4)
print(5**2)  #power 
i=5
i=i+7
i+=7
i-=7
i*=3
i//=18
print(i)

#operator percendence
total=7+7*4
print(total)

# camparison operator
print(3<2)
print(3>=2)
print(3==3)
print(2!=4)
print(2==6 and 3==3)
print(2==6 or 3==3)
print(not 9>8)

# condition if and else 
age=15
if age>21:
    #use of indentation also use colon  for block of code
    print("You r an adult")  
    print("You can Vote")
elif age<18 and age>3:
    print("You r in school")
else:
  print("You r a kid ")
print("Thank You")

# Mini Project Calculator
first=input('Input your 1st Number ')
operator=input('Input your operator +,-,*,/ is ')
second=input('Input your 2nd Number ')
first=int(first)
second=int(second)
if operator=='+':
    print(first+second)
elif operator=='*':
    print(first*second)
elif operator=='/':
    print(first//second)
elif operator=='-':
    print(first-second)
elif operator=='%':
    print(first%second)

else:
  print('invalid operation')


# RANGE
number =range(3,5)
print(number)

# while LOOP
i=1
while i<=5:
  print(i*' *  ')
  i=i+1

print('second')
i=5
while i>=0:
  print(i*' *  ')
  i=i-1

# for loop
for i in range(5):
    print(i*5)
 

marks=[34,56,78,99]
print(marks[-3])

marks=[34,56,78,99]
print(marks[1:3])

marks=[34,56,78,99]
for score in marks:
    print(score)

marks=[34,56,78,99]
marks.append(80)  #append mean add in list
print(marks)

marks=[34,56,78,99]
marks.insert(0,80)   #insert mean add between the list 
print(marks)

#find element exit or not in list
marks=[34,56,78,99]
marks.insert(0,80)   
print(56 in marks)

marks=[34,56,78,99]
marks.insert(0,80)   
print(156 in marks)

#find length of element
marks=[34,56,78,99,300]
marks.insert(0,80)   
print(len(marks))


# break and continue
students=['ram','sham','radhika','suneel','akash']
for student in students:
    if student=='suneel':
        break;
    print(student)

# constinue   mean skip from list

students=['ram','sham','radhika','suneel','akash']
for student in students:
    if student=='suneel':
        continue;
    print(' '+student)


# TUPLE     IMMUETABLE IT CANT BE CHANGE
marks =(95,45,23,56)
# marks[0]=90
print(marks)

marks =(95,45,23,56,78, 87,78,78)

print(marks.count(78))
print(marks.index(78))

person='ram','sham','mukesh' 
print(person)

# SET
# marks={34,45,56,65,45,87,45,45}
# print(marks[0]) #it cant be access by index in set we can iterate by looops

marks={34,45,56,65,45,87,45,45}
print(marks)

marks={34,45,56,65,45,87,45,45}
for score in marks:
    print(score)

# Dictinory  it will stored information in pairs
marks={"Kelash":78 , "KUmar": 99, "Mukesh": 100}
print(marks["Kelash"])
marks["rahul"]=87
print(marks)

marks["rahul"]=89
print(marks)

# FUNCTION  
# 1: In Built Function  2: Module Function 3: User Define Function

# Module Function

from math import * #all function of math module
import math
from math import sqrt
print(dir(math))
print(sqrt(36))

#user define function
# def function_Name(parameters):
def sum(first,second):
    print(first+second)
sum(2,6)

def sum(first,second=7):
    print(first+second)
sum(2)

def compute_average_scores(scores):
    num_students = len(scores)
    num_subjects = len(scores[0])

    average_scores = []

    for student in range(num_students):
        total_score = 0
        for subject in range(num_subjects):
            total_score += scores[student][subject]

        average_score = total_score / num_subjects
        average_scores.append(str(average_score))

    return average_scores

# Take input from the user for the number of students (N) and number of subjects (X)
N = int(input("Enter the number of students: "))
X = int(input("Enter the number of subjects: "))

# Take input from the user for the scores of each student
scores = []
for student in range(N):
    student_scores = []
    print(f"Enter scores for student {student + 1}:")
    for subject in range(X):
        score = int(input(f"Subject {subject + 1}: "))
        student_scores.append(score)
    scores.append(student_scores)

averages = compute_average_scores(scores)
print("Average Scores: " + ', '.join(averages))

def generate_coordinates(x, y, z, n):
        coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
        return coordinates
    
    # Input values
x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
result = generate_coordinates(x, y, z, n)
print(result)


def average_marks(student_dict, student_name):
    # Check if the student_name exists in the dictionary
    if student_name in student_dict:
        marks = student_dict[student_name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None

# Input the number of students and their marks and names
n = int(input())
student_dict = {}

for _ in range(n):
    name = input()
    marks = [float(x) for x in input(f"").split()]
    student_dict[name] = marks

# Input the student name for which you want to calculate the average marks
student_name = input()

# Call the function to calculate the average marks for the provided student
average = average_marks(student_dict, student_name)

# Print the average marks with 2 decimal places
if average is not None:
    print(f"{average:.2f}")
else:
    print(f"Student '{student_name}' not found in the dictionary.")
