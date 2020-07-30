# Day 0: Hello, World.

input_string = input()
print('Hello, World. \n'+input_string)


# Day 1: Data Types

# Declare second integer, double, and String variables.
x = int(input())
y = float(input())
z = input()
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i+x)
print(d+y)
print(s+z)
# Print the sum of the double variables on a new line.


# Day 2: Operators

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
        tip=meal_cost*tip_percent*0.01
        tax=meal_cost*tax_percent*0.01
        return round(meal_cost+tip+tax)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))


# Day 3: Intro to Conditional Statements

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if(N%2==1 or (N>5 and N<21)):
        print("Weird")
    else:
        print("Not Weird")

# Day 4: Class vs. Instance

class Person:
    def __init__(self,initialAge):
        if(initialAge<0):
                self.age=0
                print("Age is not valid, setting age to 0.")
        else:
                self.age=initialAge
    def amIOld(self):
        if(self.age<13):
                print("You are young.")
        elif(self.age<18 and self.age>=13):
                print("You are a teenager.")
        else:
                print("You are old.")
    def yearPasses(self):
        self.age+=1

        
# Day 5: Loops

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print(format("{} x {} = {}").format(n,i,n*i))


# Day 6: Let's Review

for i in range(int(input())):
        s=input()
        print(s[0::2],s[1::2] )


# Day 7: Arrays

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    result=" ".join(map(str,arr[::-1]))
    print(result)


# Day 8: Dictionaries and Maps 

n=int(input())
names_numbers=[input().split() for _ in range(n)]
dictNames={k:v for k,v in names_numbers}
while True:
        try:
                name=input()
                if name in dictNames:
                        print("%s=%s"%(name,dictNames[name]))
                else:
                        print("Not found")
        except:
                 break


# Day 9: Recursion 3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
        if(n==0):
                return 1
        return n* factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# Day 10: Binary Numbers

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    counter=0
    while n:
        n&=n<<1
        counter+=1
    print(counter)


# Day 11: 2D Arrays

import math
import os
import random
import re
import sys

def maxOfHourGlass(arr):
        result=0
        sumOfHourGlass=0
        for i in range(0,4):
                for j in range(0,4):
                        sumOfHourGlass=sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1]
                        if(sumOfHourGlass>result or (i==0 and j==0)):result=sumOfHourGlass
        return result


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
print(maxOfHourGlass(arr))


# Day 12: Inheritance

class Student(Person):
    #   Class Constructor
    def __init__(self,firstName, lastName, idNumber, scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores

    def calculate(self):
        avgScore= round(sum(self.scores)/len(self.scores))
        if(90<=avgScore<=100):
                return"O"
        elif(80<=avgScore<90):
                return"E"
        elif(70<=avgScore<80):
                return"A"
        elif(55<=avgScore<70):
                return"P"
        elif(40<=avgScore<55):
                return"D"
        else:
                return"T"


# Day 13: Abstract Classes

#Write MyBook class
class MyBook():
        def __init__(self,title,author,price):
                super().__init__()
                self.price=price
        def display(self):
                print("Title: "+title)
                print("Author: "+author)
                print("Price: "+str(price))


# Day 14: Scope

class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = max(self.__elements)-min(self.__elements)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


# Day 15: Linked List