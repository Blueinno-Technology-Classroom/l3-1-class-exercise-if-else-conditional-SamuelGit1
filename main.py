##################################################
'''
Q1:
a: True
b: False
c: True 
d: False 
e: True 
f: False 
g: True 
h: True 
i: True
'''

##################################################
'''
Q2:
a: y > 0
b: z != 0
c: y > z
d: z > 0
e: (x - y < z - y and x > 0 and z > 0) or (x - y > z - y and x < 0 and z < 0)
f: z % 2 == 1
g: x % 2 == 0
h: y % z == 0
i: 10 > y > 0
j: -x == z
k: (x % 2 == 0 and y % 2 == 1) or (y % 2 == 0 and x % 2 == 1) 
'''

##################################################
'''
Q3:
'''
'''
when the number is even and not divisible by 3
'''
number = int(input('Give me a number: '))

if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
    else:
        print("Even number.")

##################################################
