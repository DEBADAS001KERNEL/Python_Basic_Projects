def linear_search(arr, target):
    """
    Performs a linear search for a target value in an array.

    Parameters:
    arr (list): The list of elements to search through.
    target (int/float/str): The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
if __name__ == "__main__":
    data = [3, 5, 2, 8, 7, 1]
    target_value = 8

    result = linear_search(data, target_value)

    if result != -1:
        print(f"Value {target_value} found at index {result}.")
    else:
        print(f"Value {target_value} not found in the list.")
