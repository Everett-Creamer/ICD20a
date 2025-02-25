math=float(input("What is your math grade? "))
programming=float(input("What is your programming grade? "))
science=float(input("What is your science grade? "))
english=float(input("What is your english grade? "))
average = (math + programming + science + english) /4


print("Math" "\t\t", "{0:,.0f}".format(math), "%","\n"
      "Programming" "\t", "{0:,.0f}".format(programming), "%", "\n"
      "Science" "\t\t", "{0:,.0f}".format(science), "%","\n"
      "English" "\t\t", "{0:,.0f}".format(english), "%","\n"
      "Average" "\t\t", "{0:,.0f}".format(average),"%")
