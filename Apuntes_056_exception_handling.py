# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# 1 / 0 # ZeroDivisionError
# 1 + "1" # TypeError
# int("pizza") # ValueError


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by 0, IDIOT!")
except ValueError:
    print("Enter only numbers, please!")
except Exception: # Existe pero es mejor tratar con cada problema específico
    print("Something went wrong!") 
finally: # Se ejecuta siempre, aunque no haya un error
    print("Do some cleanup here")