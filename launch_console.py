print("Welcome to the Launch Console!")
name = input("What is your name? ")
print(f"Hello, {name}!")
running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) List of best programming languages")
    print("4) Exit")
    choice = input("(1-4) ")
    if choice == "1":
        print("About me:")
        print("My name is Abdulmohsin. I have been programming for almost 4 years. I like to code in C.")
    elif choice == "2":
        print("My Goals:")
        print(" - Create a compiler")
        print(" - Go to MIT")
        print(" - Become an engineer")
    elif choice == "3":
        print("1. C (obviously)")
        print("2. C3 (C but different)")
        print("3. C++ (C-style)")
        print("4. Assembly (C but lower level) (intel syntax only)")
        print("5. Go")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Invalid option.")