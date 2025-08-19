num1 = int(input("A:"))
num2 = int(input("B:"))
num3 = int(input("C:"))
if(num1 < num2 and num1 < num3):
    print(num1,"is minimum") 
elif(num2<num1 and num2<num3):
    print(num2,"is minimum")
else:
    print(num3,"is minimum")