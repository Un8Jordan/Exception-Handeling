try:
    num1=int(input("Please enter your value: "))
    num2=int(input("Please enter your value: "))
    result= num1/num2
    print("The result is: ",result)
except ZeroDivisionError:
    print("You cannot divide by Zero!")
except ValueError:
    print("Please enter a numerical value!")
except Exception as ex:
    print("Exception: ",ex)    

except:
    print("An unexpected error occured!!")

finally:
    print("I will execute this code no matter what!") 6       