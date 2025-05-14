def ctof(numc):
    numf = (9/5)*numc+32
    return numf
numc = float(input('enter your body temperature (input in clesius):'))
print("The farhenhiet temperature of your body is :",ctof(numc))