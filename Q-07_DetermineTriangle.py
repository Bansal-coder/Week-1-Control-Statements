angle1 = int(input("enter first angle:"))
angle2 = int(input("enter second angle:"))
angle3= int(input("enter third angle:"))
if(angle1==90 or angle2==90 or angle3 == 90):
    print("Right angle")
elif(angle1>90 or angle2>90 or angle3>90):
    print("Obtuse angle")
else:
    print("acute angle")
