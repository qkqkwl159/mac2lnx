# -*- coding: utf-8 -*-


#Creating a Function 

def Hello_function():
    print("Hello from the Function")
    

#Calling a function    
Hello_function()    

print("---------------------")

#Creating a function with arguments

def MyName_Function(User_name):
    print(User_name + " is a cool Person")
    
    
 #Calling the function 
MyName_Function("Kim")  
MyName_Function("Lee")   
MyName_Function("Park")   
 

print("---------------------")


#Creating a Function 
   
def cal(x):
    return x*100/10

#Invoke the function 
print(cal(2))
print(cal(2+5))
