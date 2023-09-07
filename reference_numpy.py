import numpy as np

print(f'np.arange(10) reutrn {np.arange(10)}')
print(f'np.arange(1,10) reutrn {np.arange(1,10)}')
print(f'np.arange(1,10,1) reutrn {np.arange(0,10,2)}')
print(f'np.arange(10,-10,-1) reutrn {np.arange(10,-10,-1)}')
print(f'np.arange(-10,10,-1) reutrn {np.arange(-10,10,-1)}')
print(f'np.arange(-10,10,2.5) reutrn {np.arange(-10,10,2.5)}')

arr = np.array([1,2,3,4,5])
print(f'\ntype(arr)    return {type(arr)}')
print(f'np.size(arr) return {np.size(arr)}')
print(f'arr.ndim     return {arr.ndim}') # n dimension
print(f'arr.dtype    return {arr.dtype}') # type of value

arr = np.arange(10)**2
print(f'\narr = {arr}')
print(f'arr + arr return {arr + arr}')
print(f'arr + 1   return {arr + 1}')

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,2,3,4,5])
print(f'\nnp.multiply(arr1, arr2) return {np.multiply(arr1, arr2)}')
print(f'arr1.dot(arr2)          return {arr1.dot(arr2)}')

arr_int = np.arange(1,6)
arr_floats = np.arange(1.1,1.6,0.1)
print(f'\narr_int              =    {arr_int}')
print(f'arr_floats           =      {arr_floats}')
print(f'arr_int + arr_floats return {arr_int + arr_floats}')
# print(f'{}')
print(f'np.hypot(arr_int, arr_floats) return {np.hypot(arr_int, arr_floats)}')
print(f'np.greater(arr_int, arr_floats) return {np.greater(arr_int, arr_floats)}') # comparison
print(f'np.ceil(arr_floats) return {np.ceil(arr_floats)}') # get uppder of a number
print(f'arr_floats.sum() return {arr_floats.sum()}')
print(f'arr_floats.mean() return {arr_floats.mean()}')
print(f'arr_floats.std() return {arr_floats.std()}')
print(f'arr_floats.var() return {arr_floats.var()}')
print(f'arr_floats.max() return {arr_floats.max()}')
print(f'arr_floats.min() return {arr_floats.min()}')

dimensions_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'\ndimensions_array = {dimensions_array[0:len(dimensions_array)]}')
print(f'dimensions_array.ndim return {dimensions_array.ndim}')
print(f'first row = {dimensions_array[0]}')
print(f'second row = {dimensions_array[1]}')
print(f'third row  ={dimensions_array[2]}')
print(f'first column = {dimensions_array[0:len(dimensions_array),0]}')
print(f'second column = {dimensions_array[0:len(dimensions_array),1]}')
print(f'third column = {dimensions_array[0:len(dimensions_array),2]}')
print(f'type(dimensions_array)    return {type(dimensions_array)}')
print(f'np.size(dimensions_array) return {np.size(dimensions_array)}')
print(f'dimensions_array.shape    return {dimensions_array.shape}') # shape 
print(f'dimensions_array.ndim     return {dimensions_array.ndim}') # n dimension
print(f'dimensions_array.dtype    return {dimensions_array.dtype}') # type of value
print(f'dimensions_array + [1,1,1] return {dimensions_array + [1,1,1]}')

# create arrays using zeros
array = np.zeros(shape=(3,2),dtype=float)
print(f'\narray = {array}')
print(f'np.reshape(array, (2,3)) return {np.reshape(array, (2,3))}')
