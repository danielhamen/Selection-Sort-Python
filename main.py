def selection_sort(arr: list) -> list:
    """
    Performs a selection sort in Python
    """

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(selection_sort(numbers))
