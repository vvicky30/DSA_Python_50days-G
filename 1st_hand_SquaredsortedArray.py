def sorted_squared(array):
    for i in range(len(array)):   # running loop to range equals to the length of array 
        array[i] = array[i]**2  # squaring 
    array= sorted(array)  # sorting array in ascending order as well
    print(array)
    return array

#checking with some test-cases.
sorted_squared([8,4,2,6]) # passing array
sorted_squared([-1,-3,-8,4,2,6]) # passing array with some -ves
sorted_squared([-1,-3,-8,-8, 4,2,6,6]) # passing array with some same subsequant values
