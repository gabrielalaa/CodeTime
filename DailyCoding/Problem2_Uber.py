# Return a new array such that at index i is the product of all nr except the one at i
def uber(arr):
    # Create the new array
    new_array = []
    # Iterate through the list
    for index in range(len(arr)):
        # Calculate the array without including the element at position index
        product = 1
        for element in arr:
            if arr.index(element) == index:
                continue
            product *= element
        new_array.append(product)
    return new_array

given_array = [1, 2, 3, 4, 5] # => [120, 60, 40, 30, 24]
given_array2 = [3, 2, 1]
print(uber(given_array))
print(uber(given_array2))
