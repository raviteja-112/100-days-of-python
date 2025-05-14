a = {
    "chalna" : "walking",
    "khana"  : "eating",
    "pina"   : "drinking",
    "bolna " : "talking"
}
print("The hindi words in it are :",a.keys())
b = input("Enter the hindi word : \n")
print("The english meaning of it is :",a[b]) #improved version in below line
#the above line throws an error if the word is not present
print("The english meaning of it is :",a.get(b))