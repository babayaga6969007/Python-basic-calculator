def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b   

print("Choose a Selection: 1.Add, 2.Subtract 3. Multiply 4. Divide")
select=int(input("Enter the number doing operation from 1, 2, 3, 4")) 
a=int(input("Enter first number"))   
b=int(input("Enter second number"))    
if select==1:
    print(a,"+", b, "=", add(a, b))
elif select==2:
    print(a, "-", b, "=", sub(a, b))
elif select==3:
    print(a, "*", b, "=", mul(a, b))
elif select==4:
    print(a, "/", b, "=",div(a, b))
else: 
    print("Invalid Input")   









