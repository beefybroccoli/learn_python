"""
First implement polynomial multiplication using FFT. For convenience, please use the numpy package in python which implements functions
`numpy.fft.fft` and `numpy.fft.ifft`. The advantages include efficient computation of FFT for sizes of inputs that are not powers of two.

We studied polynomial multiplication using FFT in class. Recall the algorithm given two polynomials $a(x) = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1} $ and $b(x) = b_0 + b_1 x + \cdots + b_{m-1} x^{m-1}$.

- Pad the coefficients of $a, b$ with zero coefficients to make up two polynomials of degree $m + n - 2$ (expected size of the result).
- Compute FFTs of $[a_0, \ldots, a_{n-1}, 0 , \ldots, 0 ]$ and 
$[b_0, \ldots, b_{n-1}, 0, \ldots, 0 ]$. 
  - Let $[A_0, \ldots, A_{m+n-2}]$ and $[B_0, \ldots, B_{m+n-2}]$ be the resulting FFT sequences.
- Multiply the FFT sequences: $[ A_0 \times B_0, \ldots, A_{m+n-2} \times B_{m+n-2}]$.
- Compute the inverse FFT to obtain the polynomial $c(x) = a(x) b(x)$.

"""

from numpy.fft import fft, ifft
from numpy import real, imag, multiply

def polynomial_multiply(a_coeff_list, b_coeff_list):
    # Return the coefficient list of the multiplication 
    # of the two polynomials 
    # Returned list must be a list of floating point numbers.
    # Please convert list from complex to reals by using the real function in numpy.
    # your code here
    # -----------------------------------------------------
    # - Pad the coefficients of $a, b$ with zero coefficients to make up two polynomials of degree $m + n - 2$ (expected size of the result).
    new_length = len(a_coeff_list) + len(b_coeff_list) - 1
    # print(f'new_length = {new_length}')
    padded_a_coeff_list = a_coeff_list + [0]*(new_length-len(a_coeff_list))
    padded_b_coeff_list = b_coeff_list + [0]*(new_length-len(b_coeff_list))
    # print(f'padded_a_coeff_list = {padded_a_coeff_list}')
    # print(f'padded_b_coeff_list = {padded_b_coeff_list}')

    # - Compute FFTs of $[a_0, \ldots, a_{n-1}, 0 , \ldots, 0 ]$ and $[b_0, \ldots, b_{n-1}, 0, \ldots, 0 ]$. 
    fft_padded_a_coeff_list = fft(padded_a_coeff_list)
    fft_padded_b_coeff_list = fft(padded_b_coeff_list)

    # - Multiply the FFT sequences: $[ A_0 \times B_0, \ldots, A_{m+n-2} \times B_{m+n-2}]
    result_multiply = multiply(fft_padded_a_coeff_list, fft_padded_b_coeff_list)
    # print(f'len(result_multiply) = {len(result_multiply)}')
    result_multiply_list = result_multiply.tolist()
    # print(f'len(result_multiply_list) = {len(result_multiply_list)}')

    # - Compute the inverse FFT to obtain the polynomial $c(x) = a(x) b(x)$.
    inverse_result_multiply_list = real(ifft(result_multiply_list))

    return list(map(lambda x : round(x), inverse_result_multiply_list))

def check_poly(lst1, lst2):
    print(f'Your code found: {lst1}')
    print(f'Expected:        {lst2}')
    assert(len(lst1) == len(lst2)), 'Lists have different lengths'
    for (k,j) in zip(lst1, lst2):
        assert abs(k-j)<= 1E-05, 'Polynomials do not match'
    # print('Passed!')
# print('-------') 

# print('Test # 1')
# # multiply (1 + x - x^3) with (2 - x + x^2)
a = [1, 1, 0, -1]
b = [2, -1, 1]
c = polynomial_multiply(a,b)
assert(len(c) == 6)
# print(f'c={c}')
check_poly(c, [2,1,0,-1,1,-1])
# print('-------')


# print('Test # 2')
# multiply 1 - x + x^2 + 2 x^3 + 3 x^5 with 
#            -x^2 + x^4 + x^6
a = [1, -1, 1, 2, 0, 3]
b = [0, 0, -1, 0, 1, 0, 1]
c = polynomial_multiply(a,b)
assert(len(c) == 12)
# print(f'c={c}')
check_poly(c, [0, 0, -1, 1, 0, -3, 2, -2, 1, 5, 0, 3])
# print('-------')

# print('Test # 3')
# multiply 1 - 2x^3 + x^7 - 11 x^11
# with     2 - x^4 - x^6 + x^8
a = [1, 0, 0, -2, 0, 0, 0, 1, 0, 0, 0, -11]
b = [2, 0, 0, 0, -1, 0, -1, 0, 1]
c = polynomial_multiply(a, b)
assert(len(c) == 20)
# print(f'c={c}')
check_poly(c, [2, 0, 0, -4, -1, 0, -1, 4, 1, 2, 0, -25, 0, -1, 0, 12, 0, 11, 0, -11])
print('All tests passed (10 points!)')