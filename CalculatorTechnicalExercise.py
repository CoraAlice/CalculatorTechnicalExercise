import time

#All the required conversion factors in a particular order
conversionFactors = [0.157473, 6.35029, 1e9, 1e-9, 2.54, 0.393701, 86400, 1.15741e-5]
originalUnits = ["kilos", "stones", "gigabytes", "bytes", "inches", "centimetres", "days", "seconds"]
newUnits = ["stones", "kilos", "bytes", "gigabytes", "centimetres", "inches", "seconds", "days"]

def division(numbers, times):
    #Divides any quantity of numbers and prints the result
    #Numbers is an array of the numbers that are to be divided,
    #where the first number is the number to be divided from
    #Times represents the quantity of numbers to be divided
    result = numbers[0]
    for i in range(1,times):
        result = result / numbers[i]
    for i in range(0, (times - 1)):
        print(str(numbers[i]) + " /")
    print(str(numbers[times - 1]) + " = " + str(result))
        

def multiplication(numbers, times):
    #Multiplies any quantity of numbers and prints the result
    #Numbers is an array of the numbers that are to be multiplied
    #Times represents the quantity of numbers to be multiplied
    result = 1
    for i in range(0, times):
        result = result * numbers[i]
    for i in range(0, (times - 1)):
        print(str(numbers[i]) + " x")
    print(str(numbers[times - 1]) + " = " + str(result))

def subtraction(numbers, times):
    #Subtracts any quantity of numbers and prints the result
    #Numbers is an array of the numbers that are to be subtracted,
    #where the first number is the number to be subtracted from
    #Times represents the quantity of numbers to be subtracted
    result = numbers[0]
    for i in range(1, times):
        result -= numbers[i]
    for i in range(0, (times - 1)):
        print(str(numbers[i]) + " -")
    print(str(numbers[times - 1]) + " = " + str(result))

def addition(numbers, times):
    #Sums any quantity of numbers together and prints the result
    #Numbers is an array of the numbers that are to be summed
    #Times represents the quantity of numbers to be summed
    result = 0
    for i in range(0, times):
       result += numbers[i]
    for i in range(0, (times - 1)):
        print(str(numbers[i]) + " +")
    print(str(numbers[times - 1]) + " = " + str(result))
    
while True:
    time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    while True:
        #The user will be prompted to select "add", "subtract", "divide", or "multiply"
        #If they enter something else, they will be prompted again
        print("What would you like to do?")
        time.sleep(0.5)
        print("> Add")
        print("> Subtract")
        print("> Multiply")
        print("> Divide")
        print("> Convert")
        print("(type your answer)")
        operation = input("> ")

        if operation.lower() == "add":
            break
        elif operation.lower() == "subtract":
            break
        elif operation.lower() == "multiply":
            break
        elif operation.lower() == "divide":
            break
        elif operation.lower() == "convert":
            break
        else:
            print("Please enter an option from the list above.")
            time.sleep(0.5)

    if operation.lower() == "convert":
        #Code for unit conversions
        #The user is propmted to choose which units to convert between
        print("What conversion would you like to perform?")
        time.sleep(0.3)
        print("> 1: Kilos to Stone")
        print("> 2: Stone to Kilos")
        print("> 3: Gigabytes to Bytes")
        print("> 4: Bytes to Gigabytes")
        print("> 5: Inches to Centimetres")
        print("> 6: Centimetres to Inches")
        print("> 7: Days to Seconds")
        print("> 8: Seconds to Days")
        time.sleep(0.3)
        print("(Enter the number corresponding to the option you would like.)")
        #The user can only select one of the above options
        while True:
            try:
                option = int(input("> "))
                if option > 0 and option < 9:
                    break
                else:
                    print("Please enter a number between 1 and 8.")
            except:
                print("Please enter a number between 1 and 8.")

        print("Enter the quantity you would like to convert.")
        amount = float(input("> "))
        
        convertedAmount = amount * conversionFactors[option - 1]
        print(str(amount) + " " + originalUnits[option - 1] + " = " + str(convertedAmount) + " " + newUnits[option - 1])
        
    else:
        #Code for arithmetic operations
        #The user is prompted to enter the quantity of numbers to perfom the operation on
        #If they do not enter an integer, they are prompted again        
        print("How many numbers would you like to "+ operation.lower()+"?")
        while True:
            try:
                quantity = int(input("> "))
                break
            except:
                print("Please enter a whole number.")

        #The user is prompted to enter their numbers
        if operation.lower() == "subtract" or operation.lower() == "divide":
            print("Ensure the first number you enter is the number you want to " + operation + " from.")
            time.sleep(0.5)
    
        #The user enters their numbers and they are added to the array "userNumbers"
        userNumbers = []
        x = quantity
        while x > 0:
            print("Enter the next number:")
            try:
                number = float(input("> "))
                userNumbers.append(number)
                x -= 1
            except:
                print("Please enter a number.")


        #The operation is performed
        if operation.lower() == "add":
            addition(userNumbers, quantity)
        elif operation.lower() == "subtract":
            subtraction(userNumbers, quantity)
        elif operation.lower() == "multiply":
            multiplication(userNumbers, quantity)
        elif operation.lower() == "divide":
            division(userNumbers, quantity)
    
