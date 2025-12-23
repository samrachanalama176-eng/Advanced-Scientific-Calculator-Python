# Creating Enhanced Calculator with advanced features
import math
def add(x, y):
    return x + y        #returns sum
def subtract(x,y):
    return x - y        #returns difference
def multiply(x,y):
    return x * y        #returns product
def divide(x,y):
    if y == 0: 
        return "Error! Division by zero." 
    return x / y        #returns quotient
def power(x,y):
    return x ** y       #returns x raised to the power y
def modulus(x,y):
    return x % y        #returns remainder
def sqrt(x):
    if x < 0:
        return "Error! Square root of negative number."
    return math.sqrt(x) #returns square root
def sine(x):
    return math.sin(math.radians(x)) #returns sine of angle in degrees
def cosine(x):
    return math.cos(math.radians(x)) #returns cosine of angle in degrees
def tangent(x):
    return math.tan(math.radians(x)) #returns tangent of angle in degrees
def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base) #returns logarithm of x to given base
def show_menu():
    print("\n=== Enhanced Scientific Calculator ===")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power") 
    print("6. Modulus")
    print("7. Square Root")
    print("8. Sin") 
    print("9. Cos")
    print("10. Tan") 
    print("11. Log (base 10)")
    print("q. Quit") 
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").lower()
        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break
        try:
            if choice in ('1','2','3','4','5','6'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '5':
                    print("Result:", power(num1, num2))
                elif choice == '6':
                    if num2 == 0:
                        print("Error! Modulus by zero.")
                    else:
                        print("Result:", modulus(num1, num2))
            elif choice == '7':
                num = float(input("Enter number: "))
                print("Result:", sqrt(num))
            elif choice in ('8','9','10'):
                angle = float(input("Enter angle in degrees: "))
                if choice == '8':
                    print("Result:", sine(angle))
                elif choice == '9':
                    print("Result:", cosine(angle))
                else:
                    print("Result:", tangent(angle))
            elif choice == '11':
                num = float(input("Enter number: "))
                print("Result:", logarithm(num))
            else:
                print("Invalid choice! Please select again.")
        except ValueError:
            print("Error! Please enter valid numeric input.")


if __name__ == '__main__':
    main()
    