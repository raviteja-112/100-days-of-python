hours = int(input("Enter the hours :"))
minutes = int(input("Enter the minutes :"))
seconds = int(input("Enter the seconds :"))
if 0<=hours<24 and 0<=minutes<59 and 0<= seconds<59:
    if hours>12:
        hours = hours - 12
        print(f"The time is {hours}:{minutes}:{seconds} PM in 12 hour clock format is :")
    else:
        print(f"The time is {hours}:{minutes}:{seconds} AM in 12 hour clock format is :")         
else:
    print("INVALID INPUT")
    #type f for writing in string in print function
    #refer line 7 and 9
