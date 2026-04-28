#Q-1 use of sep & end
print("Hellow", sep="my" )
print("Friend", end=" and ")
print("Family")

#Q-2 create user define inputs
name=input("Enter your name:")
age=input("Enter your age:")
hobby=input("Enter your hobby:")
print("Hello",name,"! At",age,"enjoying",hobby,"sounds fun.")

#Q-3 arathmatic opration 
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
print("Addition is ",num1+num2)
print("Subtraction is",num1-num2)
print("Multiplication is ",num1*num2)
print("Division is",num1/num2)
print("Modulo is ",num1%num2)
print("Floor Division",num1//num2)
print("Exponentiation is ",num1**num2)

#Q-4 Declares Type of variabale 
name=str("Kush")
age=int("21")
percentage=float("63.73")
print(type(name),type(age),type(percentage))

#Q-5 user Hight and weight 
Hight = float(input("Enter you hight in feet:"))
Weight = float(input("Enter you weight in kg:"))
print("Your Hight is",Hight,"feet and you weight is",Weight,"kg.")

#Q-6 logical operators
i1 = input("Enter True or False:")
i2 = input("Enter True or False:")
print(i1 and i2)
print(i1 or i2)
print(not i2)

#Q-7 Assignment operators
num1=21
num1+=num1
num1-=num1
num1*=num1
num1/=num1