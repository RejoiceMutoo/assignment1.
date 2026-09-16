try:
    # 1. Run the risky code that might throw an error
    number = int(input("Enter a number: "))
    result = 10 / number

except ZeroDivisionError:
    # 2. Runs ONLY if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero!")

except ValueError:
    # 3. Runs ONLY if a ValueError occurs (e.g., entering letters)
    print("Error: Please enter a valid integer!")

else:
    # 4. Runs ONLY if the try block succeeds without any errors
    print(f"Success! Your result is {result}")

finally:
    # 5. ALWAYS runs, regardless of whether an error occurred or not
    print("Execution complete. Cleaning up resources...")
