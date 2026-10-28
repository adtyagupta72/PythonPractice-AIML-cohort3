# print("Hello World");

# wkjdvbhjkwdvhb owjhvdb ih

# print("How are you?");  print("Hi")
# print("Line test");      print("No this will not work")

'''This line is going to print a message how are you
and it is going to be a question for the user
asking how is he?
2eofbn 0
efo ih
2o fih

function abc()
    hello

'''

# { }

# print("This is demo of print", end="***")
# print("\n \tThis", "is", "demo", "of", "print", sep=" ")

# print("House-" * 5)
# print("*"*20)

# # 2 = 3
# # A litral's value can never be changed ever!
# # True = False

# myscore = 10        ######
# myScore = 10        #Camel Case
# my_score = 10       #Snake case

# _ = 10
# print(_)

# age = 10
# print("Age: ", age)

# age = "Ten"
# print("Age: ", age)

# name = "Aditya"
# profession = "Software developer"
# experience = 10
# print("Hello, I am", name, ". I am a ", profession, " professionally. And I have around ", experience, " years experience with it!")
# x = 5
# print("x: ", x)
# print(type(x))
# x = "Hello World"
# print("x: ", x)
# print(type(x))
# x = 20.5
# print("x: ", x)
# print(type(x))
# x = 1j
# print("x: ", x)
# print(type(x))
# x = ["apple", "banana", "cherry"]
# print("x: ", x)
# print(type(x))
# x = ("apple", "banana", "cherry")
# print("x: ", x)
# print(type(x))
# x = range(6)
# print("x: ", x)
# print(type(x))
# x = {"name" : "John", "age" : 36}
# print("x: ", x)
# print(type(x))
# x = {"apple", "banana", "cherry"}
# print("x: ", x)
# print(type(x))
# x = frozenset({"apple", "banana", "cherry"})
# print("x: ", x)
# print(type(x))
# x = True
# print("x: ", x)
# print(type(x))
# x = b"Hello"
# print("x: ", x)
# print(type(x))
# x = bytearray(5)
# print("x: ", x)
# print(type(x))
# x = memoryview(bytes(5))
# print("x: ", x)
# print(type(x))
# x = None
# print("x: ", x)
# print(type(x))

# x = 10
# y = 18

# z = x + y
# print(z)
# print(x + y)

# z = x - y
# print(z)
# print(x - y)

# z = y - x
# print(z)
# print(y - x)

# z = x * y
# print(z)
# print(x * y)

# z = x / y
# print(z)
# print(x / y)

# z = y / x
# # print(z)
# print(y / x)
# print(y // x)

# 10.49    - 10
# 10.55    - 11
# 10.10    - 10
# 10.89    - 11

# print( 5 % 2 )      #1
# print(27 % 20)      #7

# print( 2 ** 2 )       #4
# print( 3 ** 5 )


# print(1 + 3 - 5 / 7 * 3 * (2/3))
'''
1 + 3 - 5 / 7 * 3 * (2/3)
1 + 3 - 5 / 7 * 3 * 0.66
1 + 3 - 1.41372
1 + 1.59
2.59

1 + 3 - 5 / 7 * 2.001
1 + 3 - 5 / 14.007
1 + 3 - 0.35
'''

# x = 10
# print(x)
# x += 2      # x = x + 2
# print(x)

# a = 10
# b = 15

# print("a == b: ",  a == b)
# print("a < b: ", a < b)
# print("a > b: ", a > b)

# print("a <= b: ",  a <= b )
# print("a >= b", a >= b )

'''
A           B              A and B
True        True            True
True        False           False
False       False           False
False       True            False

A           B              A or B
True        True            True
True        False           True
False       False           False
False       True            True

A           not A
True         False
False        True
'''
# a = 10
# b = 12
# c = 14
# print( a<b and b>c )
# print( a<b or b>c )

# print(a is 10)
# print(a is 12)

# print(a is not 10)
# print(a is not 12)

'''

2 - 0000 0010
A       B       A & B
1       1         1
1       0         0
0       0         0
0       1         0
            
A       B       A | B
1       1         1
1       0         1
0       0         0
0       1         1

A   ~A
1    0
0    1

A       B       A ^ B
1       1         0
1       0         1
0       1         1
0       0         0

<< - Left shift operator
>> - Right shift operator

55 - 110111
55 << 1 => (110111 <- 101110)
1 5 0 4 1 3 1 2 1 1 0 0
32 + 0 + 8 + 4 + 2 + 0 = 46

55 >> 1 (110111 -> 011011) 1 + 2 + 8 + 16 => 27

55 << 2 (110111 <- 011100)

110111
'''

# name = input("Please enter your name: ")
# print("Hello ", name)

# x = int(input("Enter first value for sum: "))
# y = int(input("Enter second value for sum: "))
# z = x + y
# print("Sum: ",z)

# x = input("Enter first value for sum: ")
# y = input("Enter second value for sum: ")
# z = int(x) + int(y)
# print("Sum: ",z)

# input function always returns a string

# print("2 == 2: ", 2 == 2)
# print("2 == 2.: ", 2 == 2.)
# print("2 == 2.5: ", 2 == 2.5)
# print('abc' == 'abc')
# abc = 2
# print("abc" == abc)
# print(2 == abc)
# print(1 == abc)
# abc = 0
# print(1 == abc)
'''
if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
    have_lunch()

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

  '''

# age = 17
# if age >= 18:
#     print("Eligible")

# largest_number = -999999999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number

# while True:
#     print("I'm stuck inside a loop.")

# num = 1
# while num <= 5:
#     print(num)
#     num += 1 # num = num + 1

# Write a program to print even numbers from 2 to 10 using a while loop.
# num = 2
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# num = 2
# while num <= 10:
#     print(num)
#     num += 2

# Write a program to print odd numbers from 1 to 9 using a while loop.

# Write a program to print numbers from 10 down to 1.

# Write a program to calculate the sum of numbers from 1 to 10 using a while loop.

# Write a program to print the multiplication table of 5 using a while loop.

# num = 1
# while num <= 10:
#     print(num * 5)
#     num += 1
    
#Write a program to print numbers greater than 5 from 1 to 10 using a while loop.

# num = 1
# while num <= 10:
#     if num <= 5:
#         print(num)
#     num += 1

#Write a program to print numbers between 1 and 20 that are divisible by 3.

# num =1
# while num <=20:
#     if num % 3 == 0 :
#         print(num)
#     num +=1

# print(7 % 3) # 1
# print(5 % 3) # 2

# Write a program to find the factorial of 5 using a while loop.
'''
5 * 4 * 3 * 2 * 1
num = 5 | 4 | 3 | 2 | 1
sum = 1
sum = num * sum
'''
# num = 5
# sum = 1
# while num >=1:
#     sum *= num
#     num -= 1
# print(sum)
''' Dry run = running code without executing it
num(>=1)     sum     
5           1
4           5
3           20
2           60
1           120
0           120

Output: 120
'''

# num = 1
# while num <= 10:
#     print(num)
#     num+=1


# num = 10
# while num >= 1:
#     print(num)
#     num -=1

# num = 2
# if num == 3:
#     print("This is 3")
# else:
#     print("this is else")

# print("If else is done!")

#Write a program to reverse the number 76543 using a while loop.
# num = 76543
# res = 0
# while num > 0:
#     temp = num % 10
#     res = (res * 10) + temp
#     num //= 10
# print(res)

# for count in range(100):
#     pass
#     print(count)

# print(range(0, 100))

# for count in range(1, 6):
#     print(count)

# iterator
# (0, 5)
# (0, 6)
# (1, 5)
# (1, 6)

#Write a program to print even numbers from 2 to 10 using a for loop.

# for count in range(1, 11):
#     if count % 2 == 0:
#         print(count)
# Write a program to print odd numbers from 1 to 9 using a for loop.

# for count in range(1, 11):
#     if count % 2 == 1:
#         print(count)

# Write a program to print numbers from 10 down to 1 using a for loop.

# for count in range(10, -1, -2):
#     print(count)

#Write a program to calculate the sum of numbers from 1 to 10 using a for loop.

# sum = 0
# for count in range(1, 11):
#     sum += count
# print(sum)

#Write a program to print the multiplication table of 5 using a for loop.

# for count in range(1, 11):
#     print(f' 5 x {count} = {5 * count}')

# Write a program to print numbers from 1 to 20 that are divisible by 3.

#Write a program to find the factorial of 5 using a for loop.

# a = 10

# print(a == 10 and a > 9)

# if a == 10 and a > 9:
#     print("This will satisfy")

# num = 1
# print("Loop is starting now")
# print("----====-------====------")
# while num <= 10:
#     if num == 6:
#         break
#     else: 
#         print(num)
#     num += 1
# print("Loop is ended now")
# print("----====-------====------")

# num = 0
# print("Loop is starting now")
# print("----====-------====------")
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#     else: 
#         print(num)
# print("Loop is ended now")
# print("----====-------====------")

#Write a program to print numbers from 1 to 10 and stop when the number is divisible by 7.

#Write a program to print numbers from 1 to 10, skipping all even numbers.

# i = 0
# j = 1

# print( i and j )
# print( i & j )

# a = " "

# if a:
#     print("a = True")
# numbers = []
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# print(type(numbers))

# print(f'first element: {numbers[0]}')
# print(f'second element: {numbers[1]}')
# print(f'third element: {numbers[2]}')
# print(f'fourth element: {numbers[3]}')

# numbers[1] = 100
# print(f'second element: {numbers[1]}')
# print(numbers)

# numbers[0] = numbers[2]
# print(numbers)


'''
0x0011    0x0013  0x0015      0x0017      0x0019
[10,       20,      30,         40,         50]
 0   1   2   3   4

1, 2, 3, 4, 5

numbers[0] => 10    
    => numbers[0] => address of numbers + (index * size of elem)
                     0x0011 + (0 * 2) => 0x0011
numbers[1] => 20
    => numbers[0] => address of numbers + (index * size of elem)
                     0x0011 + (1 * 2) => 0x0013
'''

# print(len(numbers))

# myList = ["One", 2, 2.5, True, False, [1, 2, 3]]
# print(len(myList))
# print(myList)
# myList[0] = 1
# print(myList)
# print(type(myList))
# print(len(myList))

# del myList[0]
# print(len(myList))
# print(myList)

# print(myList[0])
# print(myList[3])

# del myList
# print(myList)
# print(myList[0])

# print(myList[-1])
# print(myList[-2])

#list = [5,4,3,2,1]
# print(list)
# print(f'Length of list: {len(list)}')
# list.append(6) 
# print(list)
# print(f'Length of list: {len(list)}')

# list.insert(1, 10)

# print(list)
# print(f'Length of list: {len(list)}')


# list = [5,4,3,2,1]

# for index in range(len(list)):
#     print("Element: ", list[index])

# for index in range(len(list)):
#     print(f'list[{index}] -> ', list[index])

# my_list = []

# for count in range(1, 11):
#     my_list.append(count)

# print(my_list)

# for index in range(len(my_list)):
#     my_list[index] = my_list[index] + 10

# print(my_list)

# a = 10
# b = 20

# 1 ---------
# b = a + b
# a = b - a
# b = b - a
# 2 ---------
# c = b
# b = a
# a = c
# 3 ---------
# b = a * b
# a = b // a
# b = b // a

# a, b = b, a

# print(a)
# print(b)

# list = [8, 10, 6, 2, 4]
# list = [2, 4, 8, 6, 10]

# count = 0
# swapped = True
# for index1 in range(len(list) - 1):
#     swapped = False
#     for index in range(len(list) - (index1 + 1)):
#         count += 1
#         if list[index] > list[index + 1]:
#             swapped = True
#             list[index], list[index + 1] = list[index + 1], list[index]
#     if swapped == False:
#         break

# print(list)
# print("Loop ran for: ", count, " times")

'''
1                       4
[8, 10, 6, 2, 4]
[8, 6, 10, 2, 4]
[8, 6, 2, 10, 4]
[8, 6, 2, 4, 10]

2                       4
[6, 8, 2, 4, 10]
[6, 2, 8, 4, 10]
[6, 2, 4, 8, 10]
[6, 2, 4, 8, 10]        X

3                       4
[2, 6, 4, 8, 10]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]        X
[2, 4, 6, 8, 10]        X

4                       4
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]        X
[2, 4, 6, 8, 10]        X
[2, 4, 6, 8, 10]        X

'''
# swapped = True
# count = 0
# while swapped:
#     swapped = False
#     for index in range(len(list) - 1):
#         count += 1
#         if list[index] > list[index + 1]:
#             swapped = True
#             list[index], list[index + 1] = list[index + 1], list[index]
# print(count)

# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:4]
# print(new_list)

# new_list = my_list[0:]
# print(new_list)

# list = []
# for index in range(0, 500):
#     list.append(index+1)

# # 175-450
# myNewList = list[174: 450]
# print(myNewList)

# my_list = [10, 8, 6, 4, 2]
# my_list1 = my_list[:]
# print("21 in my_list: ", 21 in my_list)
# print("2 in my_list: ", 2 in my_list)

# print(my_list1)
# my_list1[2] = 18
# print("21 in my_list1: ", 21 in my_list1)
# print("2 in my_list1: ", 2 in my_list1)
# print("18 in my_list1: ", 18 in my_list1)

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")
# print(row)
# print(len(row))

# row = ["WHITE_PAWN1" for i in range(8)] # List comprehension
# print(row)
# print(len(row))

# squares = [x ** 2 for x in range(10)]
# print(squares)

# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# # twos = [2 ** i for i in range(8)]
# # print(twos)

# odds = [x for x in squares if x % 2 != 0]
# print(odds)

# for element in squares:
#     print(element)

# list = [1,2, 3, 4, 5]
# list1 = [6, 7, 8, 9, 10]
# list2 = list.extend(list1)
# print("list: ", list)
# print("list1: ", list1)
# print("list2: ", list2)

# list = [[1, 2, 3], [1, 2, 3]]
# list1 = [
#             [1, 2], 
#             [1, 2, 3], 
#             [1, 2, 3, 4]
#         ]
# list = [[1, 2, 3], [1, 2, 3]]
# list2 = [
#             [1, 2, 0, 0], 
#             [1, 2, 3, 0], 
#             [1, 2, 3, 4]
#         ]
# list2 => 3, 4
# list2[0][0] => 1
# list2[0][1] => 2
# list[row][column]

# list2[0][0]
# A[0]

# list2[1][2]
'''
Student table
row ---
Column
|
|
roll number         Name        Address
11                  Abhishek    Bhopal
12                  Adtya       Indore
13                  Mayur       Silicon city
'''

# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# # print(board)

# board[0][0] = "ROOKS"
# board[0][7] = "ROOKS"
# board[7][0] = "ROOKS"
# board[7][7] = "ROOKS"

# # print(board)

# board[0][1] = "KNIGHT"
# board[0][6] = "KNIGHT"
# board[7][1] = "KNIGHT"
# board[7][6] = "KNIGHT"

# print(board)


# temps = [[h for h in range(24)] for d in range(31)]
# temps[row][col]
# print(temps)

# sum = 0
# for i in range(len(temps)):
#     sum += temps[i][11]
# average = sum / len(temps)
# print("Average: ", average)

# greater = -999999999
# for row in range(len(temps)):
#     for col in range(24):
#         if greater < temps[row][col]:
#             greater = temps[row][col]
# print("greater: ", greater)
# print([1, 2, 3])

'''
[
    [0, 0, 0, 0, 0, 0, 0, ....24]
    [0, 0, 0, 0, 0, 0, 0, ....24]
    [0, 0, 0, 0, 0, 0, 0, ....24]
    [0, 0, 0, 0, 0, 0, 0, ....24]
]
[
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
'''


# def message():
#     print("Enter a value: ")

# print("Starting now")
# message()
# print("Completed now")

# print("Enter a value: ")
# message()
# a = int(input())
# # print("Enter a value: ")
# message()
# b = int(input())
# # print("Enter a value: ")
# message()
# c = int(input())

# def greet(name):        #Parameterised function
#     print("Hello", name)

# name = input("Enter your name :")
# greet(name)     #Arugumented function invocation

# def greetWithDetails(firstName, rollNo):
#     print("Hello RollNumber", rollNo, " ", firstName)

# name = input("Enter your name :")
# roll = int(input("Enter your rollNumber :"))
# greetWithDetails(name, roll)
# greetWithDetails(roll, name)

# def message(number, what):
#     print("Enter", what, "number", number)

# def message(number, what, xyz):
#     print("Enter", what, "number", number)
    
# message("telephone", 11)
# message("price", 5)
# message("number", "number")

# message(number1 = 11, what = "telephone")
# message(number = 11, what = "telephone", xyz = "xyz")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# adding(1, 2, 3)
# adding(c = 1, b = 2, a = 3)
# adding(3, c = 1, b = 2)
# adding(a = 3, 1, c = 2)

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")

# happy_new_year(False)

# def greet():
#     print(1)
#     print(2)
#     print(3)
#     return
#     print(4)

# greet()

# def sum(a, b):
#     return a + b

# result = sum(11, 32)
# print(result)

# def sum(a, b, c, d, e):
#     return [a + 5, b + 5, c + 5, d + 5, e + 5]

# result = sum(11, 32, 55, 90, 1)
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])
# print(result[4])

# print(None + 2)
# value = None
# if value is None:
#     print("Sorry, you don't carry any value")
# print(type(None))
# print(type(value))

# def hello(check):
#     if check is True:
#         return

# result = hello(False)
# print(result)       #False

# result = hello(True)
# print(result)       #True
'''
hello(False) => 
    check -> False  => None

hello(True) =>
    check -> True   => None
'''

# def strange_function(n):
#     if(n % 2 == 0):
#         return True
# print(strange_function(2)) #=> True
# print(strange_function(1)) #=> None

# def strange_list_fun(n):
#     strange_list = []
#     for i in range(0, n):
#         strange_list.insert(0, i)
#     return strange_list
# print(strange_list_fun(5)) #=> 4 / 0, 1, 2, 3, 4 / 0 / [4, 3, 2, 1, 0]

'''
list = [1, 2, 3]
list.insert(0, 4) => 4, 1, 2, 3
[1, 2, 3] => [4, => 1, 2, 3]
'''

# def scope_test():
#     x = 123
# scope_test()
# # print(x)
# # Global Vs Local

# def my_function():
#     print("Do I know that variable?", var)
# var = 1
# my_function()
# print(var)

# var = 2
# def mult_by_var(x):
#     return x * var
# print(mult_by_var(7))

# var = 7
# def mult(x):
#     var = 5     # Shadow variable of the global var variable
#     return x * var
# print(mult(7))


# def my_function():
#     var = 2
#     print("Do I know that variable?", var)
# var = 1
# my_function()
# print(var)

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?", var)

# var = 1
# my_function()
# print(var)

'''
var     2       1
'''

# var = 2
# print(var)
# def return_var():
#     global var
#     var = 5
#     return var
# print(return_var())
# print(var)

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)
# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)   #Copy of 2
#     print("Print #2:", my_list_2)
#     #my_list_1 = [0, 1]    # New list created locally
#     my_list_1.append(5)
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
#     del my_list_1[0]
#     print("Print #5:", my_list_1)
#     print("Print #6:", my_list_2)

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #7:", my_list_2)

'''
Print #1:   [2, 3]      
Print #2:   [2, 3]
Print #3:   [3]         [2, 3]
Print #4:   [2, 3]
Print #5:   [2, 3]

'''

# tuple_1 = (1, 2, 4, 8)
# print("tuple_1: ", tuple_1)
# print("Type of tuple_1: ", type(tuple_1))
# tuple_2 = 1., .5, .25, .125
# print("tuple_2: ", tuple_2)
# print("Type of tuple_2: ", type(tuple_2))
# tuple_3 = 1, 2, 3, 4, 5
# print("tuple_3: ", tuple_3)
# print("Type of tuple_3: ", type(tuple_3))

# tuple_4 = ()
# print("tuple_4: ", tuple_4)
# print("Type of tuple_4: ", type(tuple_4))
# tuple_5 = 1,
# print("tuple_5: ", tuple_5)
# print("Type of tuple_5: ", type(tuple_5))
# tuple_6 = "hello",
# print("tuple_6: ", tuple_6)
# print("Type of tuple_6: ", type(tuple_6))

# my_tuple = (1, 10, 100, 1000)
# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10
# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[2])
# print("Length of Tuple is: ", len(my_tuple))

# my_tuple1 = (10000, 100000)
# my_tuple2 = my_tuple + my_tuple1
# print(my_tuple2)
# print("Length of my_tuple2: ", len(my_tuple2))

# my_tuple2 => 12
# my_tuple2 = my_tuple2 + (12,)
# print(my_tuple2)
# print("Length of my_tuple2: ", len(my_tuple2))

# my_tuple2[0] = (13,)

# list = [1, 2]
# print(list * 5)

# my_tuple = (1, 10, 100, 1000)
# print(my_tuple * 3)

# check = 100 in my_tuple
# print(check)

# check = 200 in my_tuple
# print(check)

# check = 100 not in my_tuple
# print(check)

# check = 200 not in my_tuple
# print(check)

# list = [1, 2, 3, 4, 5]

# for index in range(0, len(list)):
#     print(list[index])
# print("-------------------")
# for elem in list:
#     print(elem)
# print("-------------------")
# tuple = (1, 2, 3, 4, 5)
# print("-------------------")
# for index in range(0, len(tuple)):
#     print(tuple[index])
# print("-------------------")
# for elem in tuple:
#     print(elem)

# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
# my_list = [2, 4, 6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type(tup))

# var = 123

# t1 = (1, )

# t2 = (2, )

# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)

# 1, 2, 3, 123
# 2, 3, 123, 1

# dict = { 
#     "a": "AA",
#     "a": "A",
#     "b": "B"
# }

# print(dict)
# print(len(dict))
# print(type(dict))

phone_numbers = {
    'boss': 5551234567, 
    'Suzy': 22657854310
}

empty_dictionary = {}

print(phone_numbers['boss'])
print(phone_numbers['Suzy'])
# print(phone_numbers['Suzy12'])

dictionary = {
                "cat": "chat", 
                "dog": "chien", 
                "horse": "cheval"
            }
words = dictionary.keys()

# words = ['cat', 'lion', 'horse', "dog"]
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print(words)
print(dictionary.keys())