# Basic marks percentage calculation in python 
phy= int(input("enter your physics marks:"))
chem = int(input("enter your chemistry marks:"))
maths = int(input("enter your maths marks:"))

if phy<33:
  if chem<33:
    if maths<33:
      print("fail in all subject")
    else:
      print("fail in phy and chem")
  else:
    if maths<33:
      print("fail in phy and maths")
    else:
      print("supli in phy")
else:
  if chem<33:
    if maths<33:
      print("fail in chem and maths ")
    else:
      print("suppli in chem")
  else:
    if maths<33:
      print("suppli in maths")
    else:
        total = phy+chem+maths
        per = total // 3
        if per>=90 and per<=100:
          print("student score 'A' Grade")
        elif per>=80 and per<90:
          print("student score 'B'Grade")
        elif per>=60 and per<80:
          print("student score 'C'Grade")
        elif per>=33 and per<60:
          print("student score 'D' Grade")
        else:
          print("student fail")
        
      
