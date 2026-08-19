print("Calculator")

try :

    number = int(input("Enter your number.  "))

except ValueError :

    print("Please enter a valid number.")

    exit()


result = number

while (True) :

    print("Enter what you want to do.  ")

    print("/ , * , + , - or exit  ")

    tmp = input()

    if tmp not in ( "/" , "*" , "+" , "-" , "exit") :

        print('Wrong input')

        exit()

    if ( tmp == "exit" ) :

        print( "result : ", result )

        break

    print("Enter your next number.  ")

    try :
        num_tmp = int(input())

    except ValueError :

        print("Please enter a valid number.")
        
        exit()

    if ( tmp == "/") :

        if ( num_tmp == 0 ):

            print("Not defined")

            print("Reason : Deviding by zero.")

            exit()

        result = result / num_tmp

    elif ( tmp == "*") :

        result = result * num_tmp

    elif ( tmp == "+") :

        result = result + num_tmp

    else :

        result = result - num_tmp
