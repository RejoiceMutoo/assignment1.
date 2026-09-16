favorite_fruits = ['apple', 'banana', 'orange', 'mango','peach']
with open("fruits.txt", 'w') as file:
     for fruit in favorite_fruits :
         file.write(fruit+ "\n")
print("Your favourite fruits are:")
with open("fruits.txt", 'r') as file:
     for line in file:
         print(line.strip())


