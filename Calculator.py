'''
Calculator App:
---------------
Welcome to Calculator app:
Please choose an option below:
1. Addition
2. Subtract
3. Multiplication
4. Division
5. Average
6. Exit

> 1
Operation Choosen: Addition
Please enter number (-1 to stop):10
Please enter number (-1 to stop):133
Please enter number (-1 to stop):54
Please enter number (-1 to stop):-1
Sum of all values is: 197

Please choose an option below:
1. Addition
2. Subtract
3. Multiplication
4. Division
5. Average
6. Exit

>2
---------------
Figure out static and dynamic messages / operations
    Define all necessary funcitons
1. Define the flow
2. Brute force -> Taking Best case, just implement the whole program
3. Add Validations
4. Add effeciency to the program 
'''

print("Welcome to Calculator app:")
def printMenu():
  print("---------------------------------------")
  print("Please choose an option below:")
  print("1. Addition")
  print("2. Subtract")
  print("3. Multiplication")
  print("4. Division")
  print("5. Average")
  print("6. Exit")
  print("---------------------------------------")

def addition():
  print("Operation Choosen: Addition")
  sum = 0
  while True:
    number = input("Please enter number (-1 to stop):")
    try:
      if int(number) == -1:
        break
      sum += int(number)
    except:
      print("Please enter a number only!")
      continue
    
  print("============================")
  print("Sum of all number is:", sum)
  print("============================")
  print()

def subtraction():
  print("Operation Choosen: Subtraction")
  subtractionNum = 0
  count = 0
  while count <2:
    number = input("Please enter number (-1 to stop):")
    try:
      if int(number) == -1:
        break
      if count == 0:
        subtractionNum += int(number)
      elif count == 1:
        subtractionNum -= int(number)
      count += 1
    except:
      print("Please enter a number only!")
      continue
    
  print("============================")
  print("Subtraction of both numbers is:", subtractionNum)
  print("============================")
  print()

def multiplication():
  print("Operation Choosen: Multiplication")
  sum = 0
  while True:
    number = input("Please enter number (-1 to stop):")
    try:
      if int(number) == -1:
        break
      if sum == 0:
        sum += int(number)
      else:
        sum *= int(number)
    except:
      print("Please enter a number only!")
      continue
    
  print("============================")
  print("Multiplication of all number is:", sum)
  print("============================")
  print()

def division():
  print("Operation Choosen: Division")
  division = 0
  count = 0
  while count <2:
    number = input("Please enter number (-1 to stop):")
    try:
      if int(number) == -1:
        break
      if count == 0:
        division += int(number)
      elif count == 1:
        division /= int(number)
      count += 1
    except:
      print("Please enter a number only!")
      continue
    
  print("============================")
  print("Division of both numbers is:", division)
  print("============================")
  print()

def average():
  print("Operation Choosen: Average")
  sum = 0
  count = 0
  while True:
    number = input("Please enter number (-1 to stop):")
    try:
      if int(number) == -1:
        break
      sum += int(number)
      count += 1
    except:
      print("Please enter a number only!")
      continue
    
  print("============================")
  print("Average of all number is:", sum/count)
  print("============================")
  print()

while True:
  printMenu()
  chosenOption = input("")
  try:
    if int(chosenOption) == 1:
      addition()
    elif int(chosenOption) == 2:
      subtraction()
    elif int(chosenOption) == 3:
      multiplication()
    elif int(chosenOption) == 4:
      division()
    elif int(chosenOption) == 5:
      average()
    elif int(chosenOption) == 6:
      break
    elif int(chosenOption) > 6 or int(chosenOption) < 1:
      print("Invalida input, please choose options from menu only!")
      
  except:
    print("Please enter options from the menu only!")


'''

1st number
2nd number
count     0   1
while count < 2:

12  => count += 1
asdjvb
rgkn
erolkn
knwr
klnwr
4 => count += 1
'''