# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
def bubble_sort(arr):
          n = len(arr)
          for i in range(n):
                    # Track if any swaps are made
                    swapped = False
                    for j in range(0, n-i-1):
                              # Compare the adjacent elements
                              if arr[j] > arr[j+1]:
                                        # Swap if the element found is greater
                                        arr[j], arr[j+1] = arr[j+1], arr[j]
                                        swapped = True
                    # If no swaps were made, the array is already sorted
                    if not swapped:
                              break
          return arr

# Example usage
if __name__ == "__main__":
          arr = [64, 34, 25, 12, 22, 11, 90]
          sorted_arr = bubble_sort(arr)
          print("Sorted array is:", sorted_arr)