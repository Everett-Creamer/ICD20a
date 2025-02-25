originalCost=float(input("What is the cost of the item? "))
taxRate=float(input("What is the tax rate? For Example 0.14. "))
taxRate_1=taxRate+1
finalCost=originalCost*taxRate_1
taxAmount=originalCost*taxRate
rateOfTax=taxRate*100

print(" Original Cost", "\t$", "{0:,.2f}".format(originalCost),"\n",
      "Final Cost", "\t$", "{0:,.2f}".format(finalCost), "\n",
      "Amount of Tax", "\t$", "{0:,.2f}".format(taxAmount), "\n",
      "Rate of Tax", "\t", "{0:,.0f}".format(rateOfTax), "%")