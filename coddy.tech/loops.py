#for loops
def forl():
    n = int(input())
    for i in range (3, n+1):
    #This will start at 3, until reaching to the desired number
    #For example, 24. It will end at 24
        print(f"Hello Cody, {i}")
def whilel():
    i = float(input())
    while i >= 3.5:
        i = i / 2
    print(i)
def breakl():
    for i in range(10):
        if i == 6:
            break
        print(i)
        #it will not print anything after 5.
def continuel():
    for i in range(1, 21):
        #if i % 2 == 1:
        if i % 2 != 0:
            #both codes do the exact same thing, and will skip the number 1.
            continue
        print(i)

def factorial():
    n = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
def alternative_fact():
    n = int(input())
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(result)

def rangef():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    for i in range(n1, n2, n3):
        print(i)

def nested():
    rows = int(input())
    cols = int(input())
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            row_str += "*"
        print(row_str)

def dynamic():
    count = int(input())
    total = 0
    for _ in range(count):
        #The original input (in count) is the amount the following code will be played
        #example 4 input, the following code will ask for 4 numbers. Each time a number is entered it add total. Then it will update the code.
        num = int(input())
        total += num
    print(total)
dynamic()
