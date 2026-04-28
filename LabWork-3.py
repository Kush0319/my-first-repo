#Q-1 Type Casting
value = str(input("Enter number:"))
i=int(value)
f=float(value)
b=bool(value)
print("int:",i,type(i))
print("float:",f,type(f))
print("bool:",b,type(b))

#Q-2 Convert Float to int
num=float(input("Enter Number:"))
inum=int(num)
print("Float number is ",num,"with decimal.")
print("Int number is ",inum,"without decimal.")

#Q-3 bool to sring and int
b=bool(input("Enter True Or False:"))
i=int(b)
s=str(b)
print("Boolen value:",b)
print("Int value:",i)
print("String value:",s)

#Q-4 type and id
s=str("kush")
i=int(21)
f=float(21.8)
b=bool(True)
print("String:",s,"Type:",type(s),"memory address:",id(s))
print("Int:",i,"Type:",type(i),"memory address:",id(i))
print("Float:",f,"Type:",type(f),"memory address:",id(f))
print("Boolen:",b,"Type:",type(b),"memory address:",id(b))

#Q-5 Same value id
num1=8
num2=19
num3=8
print("Id of num1:",id(num1))
print("Id of num2:",id(num2))
print("Id of num3:",id(num3))