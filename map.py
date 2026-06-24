data = [10, 20, 30, 40]
for i in range(1, len(data) - 1):  # Starts at 1, stops before the last
    print(data[i-1], data[i], data[i+1])  # Looks at neighbors