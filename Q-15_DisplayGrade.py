percentage= int(input("Enter you percentage: "))
if(percentage>85):
    print(percentage, "A+")
elif(percentage<=85 and percentage>65):
    print(percentage, "A")
elif(percentage<=65 and percentage>45):
    print(percentage, "B")
elif(percentage<=45 and percentage>25):
    print(percentage, "C")
else:
    print(percentage, "D")
    