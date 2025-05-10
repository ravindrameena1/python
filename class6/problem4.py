# coditions multiple if statements 
a = int(input("Enter your age: ",))
b= input("Enter your name: ")
if(a%2):
    print("Even ",)


    
if(a>=18):
    print("You're above the age of consent ",)
    print("Hello",(b))
elif(a<0):
    print("invaild age")

elif(a==0):
    print("age cannot be 0")

else:
    print("You're less then 18 ",)
    print("Sorry ")