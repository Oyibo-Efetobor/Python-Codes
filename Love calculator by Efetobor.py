import time
print(("Welcome to the love calculator! "))
print()
name1 = input("enter your first name and your last name: ")
print()
name2 = input("enter your crush's/ lover's first name and last name: ")
newname1 = name1.lower()
newname2 = name2.lower()
newname1_counta = newname1.count("t")
newname1_countb = newname1.count("r")
newname1_countc = newname1.count("u")
newname1_countd = newname1.count("e")
newname_total = int(newname1_counta) + int(newname1_countb) + int(newname1_countc) + int(newname1_countd)


newname2_counta = newname2.count("t")
newname2_countb = newname2.count("r")
newname2_countc = newname2.count("u")
newname2_countd = newname2.count("e")
newname2_total = int(newname2_counta) + int(newname2_countb) + int(newname2_countc) + int(newname2_countd)

true_total = (newname_total) + (newname2_total)

ename1_counta = newname1.count("l")
ename1_countb = newname1.count("o")
ename1_countc = newname1.count("v")
ename1_countd = newname1.count("e")
ename_total = int(ename1_counta) + int(ename1_countb) + int(ename1_countc) + int(ename1_countd)

ename2_counta = newname2.count("l")
ename2_countb = newname2.count("o")
ename2_countc = newname2.count("v")
ename2_countd = newname2.count("e")
ename2_total = int(ename2_counta) + int(ename2_countb) + int(ename2_countc) + int(ename2_countd)

love_total = (ename_total) + (ename2_total)

compatible_total = str(true_total) + str(love_total)

compatible_total2 = int(compatible_total)
print()
time.sleep(1)
print("COMPATIBILITY LOADING")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print()
if compatible_total2 < 10 or compatible_total2 == 100:
    print(f"your score is {compatible_total2} % you go together like coke or mentos")
if compatible_total2 > 39 and compatible_total2 < 51:
    print(f"your love score is {compatible_total2} % , you are alright together.")
if compatible_total2 > 100:
    print("you're madly in love, over 100% ")
else:
    print(f"your love score is {compatible_total2} %")
