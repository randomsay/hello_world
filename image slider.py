'''from os import remove
import random
def num_list(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print(num_list([2,3,4,5,6,7]))
print(num_list([1,2,3,3,4,5,5,6])
for i in range(0,5):
    char_list = ['a','e','i','o','u']
    random.shuffle(char_list)
    print(''.join(char_list))

def num_rem(num):
    if len(num) >3:
        num.pop(2)'''


# set do not have index and must contain only unique element
'''Array
      linear ds, contiguoug memory location, access elements randomly
       homogeneous elements that is similiar elements'''
 #2D array
'''r_num = int(input("number of rows:"))
c_num = int(input("enter the columnc:"))
se_arra = [[0 for col in range(c_num)] for row in range(r_num)]
for row in range(r_num):
    for col in range(c_num):
        se_arra[row][col]= row*col
print(se_arra)'''

'''Stack LIFO / FILO. ex -  plate, pile of clothes.commands -- push,pop,peak/top, isEmpty.'''


ss = """ hello everyone i am jyoti and welcome to my code today er are going to learn about all the necessary need to implement"""


# implementation of stack
    # using list and modules
      # push -- append
      # pop -- pop
stack = []
def push():
    if len(stack)==n:
        print("stack is full!!")
    else:
        element = input("enter the element:")
        stack.append(element)
        print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        element = input("enter the poping:")
        stack.pop
        print(stack)

n = int(input("enter the limit of stack:"))
while True:
    print("Select the functiion: 1 PUSH    2 POP    3 QUIT")
    choice = int(input("-->"))
    if choice==1:
        push()
    elif choice== 2:
        pop()
    elif choice== 3:
        break
    else:
        print("Enter the correct option")
