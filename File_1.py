# Introduction to Python - class 2 - H. Demaie
#
# Topics :
#   1 - conditions
#   2 - loops
#   3 - functions
#
# Ref: Python_introduction_course.pdf

# **************************************
## 1 - Conditions
# **************************************

# vs matlab ?
#   if/elseif/else/end
#   switch/case/otherwise/end

print('-- if 1')

val = 1

if val == 0:
    print('A')
elif val == 1: # else if
    print('B')
else:
    print('C')
    print('D')

# mind the colon at the end of the line to introduce a multiline block
# tests can includes and / or / != / not
# indentations are key in Python bc they define the blocks (vs end in matlab)

print('-- if 2')
val = 1

if val == 0:
    print('A')

    print('B')

# ternary if statement (p76)
test = 10 if val == 1 else 0

if val == 1:
    test = 10
else:
    test = 0

if 1:
    print("Toto")
else:
    print("Titi")


# explanations p68 / exercice p77

# **************************************
## 2 - Loops
# **************************************

# vs matlab ?
#   for/break/continue/end
#   while/break/continue/end

print('-- for')

for ind in range(10):
    print(ind)
print("--")

for ind in range(100):
    if ind % 2: # odd
        continue
        # print("toto")
    else: # even
        print(ind)
    if ind == 10:
        break
    print("Step")

for ind in range(10):
    print(ind % 2)

for ind in range(100):
    print(ind)
    if ind == 10:
        break

print("Step")

print('-- while')

cnt = 30

while cnt > 0:
    print(cnt)
    if cnt == 20:
        break
    cnt = cnt - 1
else:
    print("Else block")
    # not executed if loop stops on break
    # try to replace 20 by 40

# explanations p80/86/87

# **************************************
## 3 - Functions
# **************************************

# vs matlab ?
#   function out = fun(input)

print('-- function')

def sayhi():
    print('Hi')

for ind in range(10):
    sayhi()

def greet(name):
    res = "Hi " + str(name)
    print(res)
    return res

greet("Heathcliff")
res = greet("Toto")
print(res)

def add(v1, v2):
    res = str(v1) + str(v2)
    return int(res)

result = add(1, 1)
print(result)

def otherfunction(a = 0, b = 0): # 0 & 0 are the default values for a & b
    res1 = a+b
    res2 = a-b
    return (res1, res2)

[c, d] = otherfunction(5, 2)
print(c)
print(d)

c, d = otherfunction()
print(c)
print(d)

# global variable: possible but don't use it! (p102)

# Warning: a function can modify input parameters depending on their types
#     will be discussed in the next class

# explanations p91 / exercices p124





