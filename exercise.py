numbers = [3,  8,  1,  6,  4,  9,  7,  2,  5]

# Step  1: Sort the list in ascending order
numbers.sort()

# Step  2: Iterate through the list
for i in range(0, len(numbers),  2):
    # Step  3 &  4: Swap even and odd numbers
    if numbers[i] %  2 ==  0:
        for j in range(i+1, len(numbers)):
            if numbers[j] %  2 !=  0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                break
    else:
        for j in range(i+1, len(numbers)):
            if numbers[j] %  2 ==  0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                break

print(numbers)