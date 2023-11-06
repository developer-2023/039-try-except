def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

"""
# initial version
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer ")
        else:
            break
    return x
"""
"""
# Shorter version
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer ")
        else:
            return x
"""
"""
# Even shorter version
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer ")
"""
"""
# Even even shorter version
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer ")
"""
"""
# Refined version
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
"""
# Last parametrized version
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()