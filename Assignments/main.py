# Recursive function to perform bubble sort
def bubble_sort(arr, n):
    if n == 1:
        return arr  # Base case: if there's only one element, it's sorted

    # Perform a single pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements if needed

    # Recursive call to sort the remaining elements
    return bubble_sort(arr, n - 1)

# Main function
def main():
    arr = list(map(int, input("Enter the array elements separated by commas: ").split(',')))
    n = len(arr)  # Calculate the length of the array
    result = bubble_sort(arr, n)
    print("Sorted array:", result)

# Calling the main function
if __name__ == "__main__":
    main()