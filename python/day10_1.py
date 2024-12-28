from day10_art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    if(n2 == 0):
        return print("Number cannot be divided by zero.")
    return n1/n2

operators = {"+" : add,
             "-" : sub,
             "*" : mul,
             "/" : div,
             }
def calculator():
    print(logo)
    num1 = float(input("Enter the first num: "))


    for symbols in operators:
        print(symbols)

    further_calculation = True
    while(further_calculation):
        operation_symbol = input("Enter the operation :")

        num2 = float(input("Enter the next num: "))

        function = operators[operation_symbol]
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        decision = input(f"Type 'y' to contiue calculating with {answer},or type 'n' to start new cal.: ")
        if(decision == 'n'):
            further_calculation = False
            calculator()    