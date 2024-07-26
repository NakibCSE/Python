#Version 01
def myfnc(x):
    print("Inside myfnc", x)
    x = 10
    print("Inside myfnc", x)

x = 20
myfnc(x)
print(x) 

#Version 02
def myfnc(y):
    print("y = ", y)
    print("x = ", x)

x = 20
myfnc(x)

#Version 03
def myfnc(y):
    print("y = ", y)
    print("x = ", x)

x = 20
myfnc(x)
#print("y = ", y)   #Will generate error as y (variable inside a function) not accessible outside the function

#Version 04
# function with default parameter
def myfnc(y = 10):
    print("y = ", y)

x = 20
myfnc(x)
myfnc() 


#Version 05
#Order of mixing parameter (actual and default)
#def myfnc(x, y = 10, z):                # will generate error as it is not allowed to have normal parameter after dafault parameter
 #   print("x = ", x, "y = ", y, "z = ",z)

x = 5
y = 6
z = 7

#myfnc(x,y,z)


#Version 06
#Order of mixing parameter (actual and default)  error fixed version 
def myfnc(x , y = 10, z = 0):
    print("x = ",x, "y = ", y, "z = ", z)
 
x = 5
y = 6
z = 7
myfnc(x,y,z)
myfnc(x,y)
myfnc(x)


#Version 07
#Calling function with definate parameter indication
def myfnc(x, z, y = 10):
    print("x = ",x, "y = ",y, "z = ", z)

myfnc(x = 1, y =2, z = 5)
a = 5
b = 6
myfnc(x = a, z = b)
a = 1
b = 2
c = 3
myfnc(y=a, z = b, x = c)