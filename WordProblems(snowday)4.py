precentOne=float(input("Percentage Number "))
wholeOne=float(input("Whole Number "))
decimalOne=precentOne/100
valueOne=decimalOne*wholeOne

precentTwo=float(input("Percentage Number 2nd Time "))
wholeTwo=float(input("Whole Number 2nd Time "))
decimalTwo=precentTwo/100
valueTwo=decimalTwo*wholeTwo

precentThree=float(input("Whole Number 3rd Time"))
wholeThree=float(input("Whole Number 3rd Time"))
decimalThree=precentThree/100
valueThree=decimalThree*wholeThree

print("10 % of 70 is ", "{0:,.1f}".format(valueOne),"\n"
      "20 % of 25 is ", "{0:,.1f}".format(valueTwo),"\n"
      "5 % of 60 is ", "{0:,.1f}".format(valueThree))