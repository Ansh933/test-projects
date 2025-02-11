
#Defining a function
def triangle():
    base = float(input("Enter your base: "))
    height = float(input("Enter the height: "))
    print("The Area is:")
    print(0.5 * base *height)
def rect():
    L = int(input("Enter the length of the rectangle: "))
    B = int(input("Enter the Breadth of the rectangle: "))
    print("The area is: ")
    print(L*B)
    print("The Perimeter is")
    print(L+B + L+B)

choice = input("Enter the type of shape that you want to find area of(rectangle or triangle):")
choice = choice.lower()
if choice == "triangle" :
    triangle()
elif choice == "rectangle":
    rect()
else:
    print("u can only choose rectangle or triangle")