
def q1():
  #Write Assignment code here
  bool1=True
  bool2=False
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  #Write Assignment code here
  number=eval(input("Enter an integer"))
  bool1=not number==0
  print(bool1)
def q3():
  #Write Assignment code here
  number=eval(input("Enter a number"))
  print(number > 0 and number < 10) 
def q4():
  #Write Assignment code here
  food=input("Enter a food, with the first letter being capitalized")
  drink=input("Enter a drink, with the first letter being capitalized")
  if food=='Pizza' and drink=='Pop':
    print(False)
  else:
    print(True)
def q5():
  #Write Assignment code here
  number=eval(input("Enter an integer"))
  if number%2==0:
    print(True)
  else:
    print(False)
#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
