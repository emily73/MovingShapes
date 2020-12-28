import time

diamondHeight = int(input("Choose a height for your shape: "))
typeofShape = input("Would you like a \n 1. TRIANGLE \n 2. DIAMOND \n")

def diamond():
    for i in range(diamondHeight-2, -1, -1):
            print(" "*(diamondHeight-i), "*"*(i*2+1))

def triangle():
    for i in range(diamondHeight-2, -1, 1):
        print(" "*(diamondHeight-i), "*"*(i*2+1))
try:
    if typeofShape == '1' or typeofShape == '2':
        while True:
            for i in range(diamondHeight):
                print(" "*(diamondHeight-i), "*"*(i*2+1))
            if typeofShape == '1':
                triangle()
            elif typeofShape == '2':
                diamond()
            time.sleep(0.1)
    else:
        print("Invalid choice!!")
        exit()

except KeyboardInterrupt:
    exit()
