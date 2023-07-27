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



