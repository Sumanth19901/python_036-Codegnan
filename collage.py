# 1. Repeat an action EXACTLY 5 times
for i in range(5):
    print("Hello")  # Prints "Hello" 5 times

# 2. Loop through list items using their INDEX
fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print(f" {fruits[index]}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# 3. Generate only EVEN numbers
for even in range(0, 11, 2):
    print(even)  # Prints 0, 2, 4, 6, 8, 10

# 4. COUNTDOWN (Negative step)
for countdown in range(5, 0, -1):
    print(countdown)  # Prints 5, 4, 3, 2, 1
print("Blast off!")