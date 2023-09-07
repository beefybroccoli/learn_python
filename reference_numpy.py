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
