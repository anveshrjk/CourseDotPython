import numpy as np

# creates a 1D array
arr1 = np.array([1,2,3,4,5])
# reverses it
print(arr1[ : :-1])

# similarly creates a string object and reverses it
str1 = "inte"
print(str1[ : :-1])

# create array initialize with zero
arr2 = np.zeros((3,4))
print(arr2)

# transpose of an array
arr3 = np.array([[1, 2, 3],
                 [4,5,6],
                 [7,8,9]])
print(arr3.transpose())
print(arr3 + arr3)
print(arr3 @ arr3)
print(arr3 ** 2)