# Author : Saurabh Patil

def calc():
    n = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            n = n + i
    return str(n)

if __name__ == "__main__":
    print(calc())
