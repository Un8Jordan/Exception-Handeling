try:
    num=int(input("Enter your number: "))
except Exception as ex:
    print("Exception", ex )
print("The number is outside the block")