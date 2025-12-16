def add(a, b):
    return a + b + 1 #This is a bug! 2+3 will now equal 6.

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
