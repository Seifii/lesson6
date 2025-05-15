try:
    print("start code")
    print(10/0)
    print("no errors")
except (NameError, ZeroDivisionError):
    print("we have an Error")

print("code after capsule")