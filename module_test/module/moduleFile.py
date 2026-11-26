# print("I like to be a module.")

print(__name__)     # Prints the name of the file when executed from other file

__counter = 0

# if __name__ == "__main__":          # when directly ran
#    print("I am the main file now!!")
# else:                               # when ran as a module
#    print("I am a module now.")

# def printNumbers():
#    for count in range(1, 11):
#       print(count)

# if __name__ == "__main__":          # when directly ran
#    printNumbers()

def suml(list):
    global __counter
    sum=0
    for elem in list:
        sum += elem
    return sum

def prodl(list):
    global __counter
    sum = 1
    for elem in list:
       sum *= elem
    return sum

if __name__ == "__main__":
    # print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    # my_list.append(2)
    print("This is the list, I am testing with:", my_list)
    print("Sum of all elements is: ", suml(my_list))
    if suml(my_list) == 15:
        print("Sum test case passed ✔")
    else:
        print("The Sum test case have been Failed X ")
    print("Product of all elements is: ", prodl(my_list))
  
    if prodl(my_list) == 120:
        print("Product test case passed ✔")
    else:
        print("The Product test case have been Failed X ")
