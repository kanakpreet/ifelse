#an automatic car giving directions for help , reverse, start
a='y'
while a=='y':
  automation = input("enter the colour")
  if automation=="green":
    print ("the car goes in reverse ")
    if automation =="green":
      print("the car is already in reverse ")
    else:
      break
  elif automation == 'red':
    print ("the car starts")
  elif automation == "yellow":
    print ("the car stops ")
  else:
    print("help directions")
  a=input("want to continue yes=y, no=n")
