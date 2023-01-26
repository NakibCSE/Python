def myFunc(x):
    print("Inside myFunc ",x)
    x = 10
    print("Inside myFunc after value reassign ",x)

x = 20
myFunc(x)
print(x)


# global scope test 

def myFnc(y):
    print("y = ",y)
    print("x = ",x)

x = 20
myFnc(x)


#default value as parameter of a function
print("myfnc2 function begins")
def myfnc2(y=29):
    print("y = ",y)
    
x = 20
myfnc2(x)
myfnc2()


#another function
print("myfnc3 begins")
def myfnc3(x, y=10, z=0):
    print('x = ', x, ' y = ',y , 'z = ',z)
x = 10
y = 11
z = 14
myfnc3(z,y,z)
myfnc3(x,y)
myfnc3(x)