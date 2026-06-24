original = [1, 2, 3]
duplicate = original.copy()
duplicate.append(4)
print(original)   # [1, 2, 3]  (unchanged)
print(duplicate)  # [1, 2, 3, 4]
