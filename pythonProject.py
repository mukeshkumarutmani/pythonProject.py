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

marks=[34,56,78,99,89]
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
if the average is None:
    print(f"{average:.2f}")
else:
    print(f"Student '{student_name}' not found in the dictionary.")

    print(8113509743655314852)
    print(8113509747655314852)

# make program for adding numbers
def sum(number):
    add=0
    for i in range(number+1):
        add+=i
    return add
num=int(input("input your number "))
sum(num)
print(sum(num))

odd number sum
x=int(input())
sum=0
for i in range(x+1):
    if i%2!=0:
        sum+=i
print(sum)


even number sum
x=int(input())
sum=0
for i in range(x+1):
    if i%2==0:
        sum+=i
print(sum)

x=int(input())
sum=0
for i in range(x+1):
    if i%x==0:
        sum+=i
       
print(sum)

# what do we want
# we want to evalute the algorithm
# we want to evaulte scalbility
# we want to evalute in term of input size 
# best case, Wrost case, Average case

Order of growth
factorial calculate  

def fac(num):
    answer=1
    while num>1:
        answer*=num
        num-=1
    return answer
    # print(answer)

x=int(input("input Number"))
fac(x)
print(fac(x))

it doest not depend on the length of array
list=[3,4,5,6,7,76,847,99,8437,6476,234,34,45,56,34,45,56]
print(list[3])

# logrithm code will get more money
# order of growth
# constant, linear, qudratic, logorithmic, nlogn, exponetial
# fabonaci

list=[3,4,6,7,8,9]
# list=int(list)
sum=0
for i in list:
    sum+=i
print(sum)

list=[1,2,3,4,5]
product=1
for i in list:
    product=i*product
print(product)      #Time complexcity of this program will be o(n)

# quadratic ---> order of growth
time complexcity will be n**2
import time
start=time.time()
list=[1,2,3,4,5]
for i in list:
    for j in list:
        print("(",i,",",j,")")
print(time.time()-start)

def intTostr(i):
    digits='0123456789'
    if i==0:
        return'0'
    result=''
    while i>0:
        result= digits[i%10]+result
        i=i//10
    return result
    # print(intTostr(i))
# num=int(input('Number'))
print(intTostr(99))
    
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
x=5
print(x+x)

a="6"
print(int(a)+6)
print(a+"6")

print function
print('Chanderyan III')
print("Elon Musk")


# use for to find size of data type
import sys
print(sys.maxsize)
print(sys.int_info)

# name=input("enter your name")
# print(name)

# c=100
# f=c*9/5+32
# print(float(f))

# temp_c=float(input("enter your temp "))
# f=temp_c*9/5+32
# print(str(f))

# a=float(input("input number one "))
# b=float(input("input number two "))
# c=a**b
# print(c)

# a=78 
# print((a))
# try:
     
#     hour_worked=float(input('input your worked hour '))
#     rate_work=float(input('input rate of the work '))
# # if hour_worked==str:
# #     print("Error, please enter numberic input")
#     if hour_worked<40:
#         gross_payy=hour_worked*rate_work
#     else:
#         regular_pay=40*rate_work
#         over_timehour=hour_worked-40
#         over_timepay=over_timehour*(rate_work*1.5)
#         gross_payy=regular_pay+over_timepay
#     print('Total gross pay will be '+ str(gross_payy))

# except ValueError:
#        print("Error, please enter numbers input")
    
# try:
#     print("Enter the score between 0.0 and 1.0: ")
#     score=float(input())
#     if score>=0.9 and score<=1:
#         print('A')
#     elif score>=0.8 and score<0.9:
#         print('B')
#     elif score>=0.7 and score<0.8:
#         print('C')
#     elif score>=0.6 and score<0.7:
#         print('D')
#     elif score>0 and score<0.6:
#         print('F')
#     else:

#        """ print('Bad Score')
# except ValueError:
#     print('error, please input correct numeric') """

# print('Starting countdown')
# count=10
# while count>=1:
#     print(count)
#     count-=1
# print('liftoff!')

# print('countdown start')
# for a in range(10,0,-1):
#     print(a)
# print('liftoff')

# def my_func(b):
#     return sum(b)
# p_number=[2,3,4,5,6,7,8]
# result=my_func(p_number)
# print(result)

# def func(numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     return total
# num=[3,4,5,6,7]
# result=func(num)
# print(result)

# def my_function(numbers):
#     total_length=len(numbers)
#     sum=0
#     for number in numbers:
#         sum+=number

#     average=sum/total_length
#     return average

# num=[4,5,6,7,8,9]
# result=my_function(num)
# print(result)


# def my_function(num):
#     largest_number=num[0]
#     for number in num:
#         if number>largest_number:
#             largest_number=number
#     return largest_number

# list=(input('Input your list'))
# number_string=list.split(' ')
# numbers=[int(num) for num in number_string]
# result=my_function(numbers)
# print(result)

# def my_function(num):
#     smallest_num=num[0]
#     for number in num:
#         if smallest_num>number:
#             smallest_num=number
        
#     return smallest_num

# list=[340,405,504,607,793,304,900,878]
# result=my_function(list)
# print(result)

# msge=input(' type a string ')
# count=0
# for letter in msge:
#     count=count+1
# print('the length in string is '+str(count))

# mssge=input('type a mssge')
# str_length=len(mssge)
# print(str_length)

# str_var='X-DSPAM-confidence:0.8487654323'
# # print(str_var)
# colo_pos=str_var.find('6')
# # # print(colo_pos)

# # num_slice=str_var[colo_pos+1:]
# # print(num_slice)

# slice_str=str_var[colo_pos+1:]
# print(slice_str)
# float_num=float(slice_str)
# print(type(float_num))
# print(float_num)

# a=7
# print(type(a))
# text = "Hello, World"
# substring = text[0:5]
# print(text)
# print(substring)


# text='the quick brown fox jump over the lazy dog'
# slice_of=text[0:10]
# print(slice_of)

# slice_of_2=text[-10:]
# print(slice_of_2)

# replace_str=text.replace('the', 'a')
# print(replace_str)


# text=input('Write a text ')
# split_text=text.split()
# print(split_text)

# word_count=0
# for wd in split_text:
#     word_count=word_count+1

# print(word_count)



# length_words=len(split_text)
# print(length_words)


# list=[3,1,18,4,11,10,6,20,76,98,9,23,34,45]
# even_list=[]

# for num in list:
#     if num%2!=0:
#         even_list.append(num)
# print(even_list)


# by using list comprehension method

# list=[23,34,45,56,67,98,65,77,88]
# out_list=[i for i in list if i%2 != 0]

# print(out_list)


# list=[1,2,3,45,6,7,8,9]
# num=1
# for i in list:
#     num=i*num
# print(num)


# num_list=[3,1,18,4,11,10,20]

# sum=0
# for i in num_list:
#     sum+=i
# print('The sum of all number',sum)


# len_list=len(num_list)
# print('length of number is '+ str(len_list))

# largest_num=num_list[0]
# for i in num_list:
#     if i > largest_num:
#         largest_num=i
# print("Largest number",largest_num)

# smallest_numer=num_list[0]
# for i in num_list:
#     if i<smallest_numer:
#         smallest_numer=i
# print("Smallest number",smallest_numer)


# char_list=['y','e','l','l','o','w']
# join_list=''.join(char_list)
# print(join_list)

# str_list=['the','quick','brown','fox']
# join_str=''.join(str_list)
# print(join_str)


# list1=[3,1,18,4]
# list2=[11,10,6,20]
# new_list=list1+list2
# print(new_list)
# sort_list=sorted(new_list)
# print(sort_list)
