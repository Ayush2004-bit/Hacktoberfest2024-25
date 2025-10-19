# Find first occurrence of an element in a list

def first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index of first occurrence
    return -1  # If element not found

# Example usage
arr = [10, 20, 30, 20, 40, 50]
x = int(input("Enter the element to find: "))

index = first_occurrence(arr, x)

if index != -1:
    print(f"First occurrence of {x} is at index {index}")
else:
    print(f"{x} not found in the list")
