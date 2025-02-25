totalHours=float(input("Amount of worked hours"))
regularHours=float(input("How many hours until overtime?"))
otHours=totalHours-regularHours
regularRate=float(input("What is your hourly rate?"))
otRate=regularRate*1.5
regularPay=regularHours*regularRate
otPay=otHours*otRate
totalPay=regularPay+otPay

print("Total hours", "\t\t", "{0:,.0f}".format(totalHours), "\n"
      "Regular hours", "\t\t", "{0:,.0f}".format(regularHours), "\n"
      "OT hours", "\t\t", "{0:,.0f}".format(otHours), "\n"
      "Regular rate", "\t\t", "{0:,.0f}".format(regularRate), "\n"
      "OT rate", "\t\t", "{0:,.2f}".format(otRate), "\n"
      "Total Regular Pay", "\t", "{0:,.2f}".format(regularPay),"\n"
      "Total OT Pay", "\t\t", otPay, "\n"
      "Total Pay", "\t\t", totalPay)