while True:
    try:
        age=int(input("Please enter your age:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid age.")
    print(f"Your age is: age")