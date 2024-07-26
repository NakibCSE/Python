def testFnc(li):
    li[0] = 10

my_list = [1,23,4,3,2,2]
print("My list before function call: ", my_list)
testFnc(my_list)
print("My list after function call: ", my_list)