## Problem 3 
"""
We are given three subsets of numbers $A, B, C\subseteq \{ 0, \ldots, n\}$. Design an algorithm that runs in worst case time  $\Theta(n \log(n))$ that checks if there exists numbers $n_1, n_2$ in $A,B$, respectively and number $n_3$ in $C$ such that
$ n_1 + n_2 = n_3$. 

**Hint:** Convert the set $A = \{ n_0, n_1, \ldots, n_k\}$ into the polynomial $p_A(x):\ x^{n_0} + x^{n_1} + \cdots + x^{n_k}$. Suppose $p_A(x), p_B(x)$ are polynomials obtained from the sets $A, B$ respectively, interpret what the product  $p_A(x) \times p_B(x)$ signifies. Use this to complete an algorithm for the problem at hand that runs in $n \log(n)$ time. 
"""
from numpy import fft, multiply
from course_3_week_1_problem_2 import polynomial_multiply

# inputs sets a, b, c
# return True if there exist n1 in a, n2 in B such that n1+n2 in C
# return False otherwise
# number n which signifies the maximum number in a, b, c
# here is a useful reference to set data structure in python
# https://docs.python.org/3/tutorial/datastructures.html#sets
def check_sum_exists(a, b, c, n):
    a_coeffs = [0]*n
    b_coeffs = [0]*n 
    # convert sets a, b into polynomials as provided in the hint
    # a_coeffs and b_coeffs should contain the result
        
    # multiply them together
    # print ("a_coeffs . ", a_coeffs)
    # print ("b_coeffs . ", b_coeffs)
    c_coeffs = polynomial_multiply(a_coeffs, b_coeffs)
    # print("Co-efficients of the testcase are")
    coeffs_copy = []
    for num in c_coeffs:
        if(abs(num-0) < abs(num-1)):
            coeffs_copy.append(0)
        elif(abs(num-1) < abs(num-2)):
            coeffs_copy.append(1)
        else:
            coeffs_copy.append(2)
    # print("coeffs_copy= ", coeffs_copy)
    # use the result to solve the problem at hand
    # your code here
    # ----------------------procedure-------------------------
    # # procedure code, run time is theta(n * n)
    # for index in a:
    #     a_coeffs[index] = 1
    # for index in b:
    #     b_coeffs[index] = 1
    # a_multiply_b = polynomial_multiply(a_coeffs,b_coeffs)
    # # print(f'a_coeffs = {a_coeffs}')
    # # print(f'b_coeffs = {b_coeffs}')
    # # print(f'a_multiply_b = {a_multiply_b}')
    # # print(f'len of a_multiply_b = {len(a_multiply_b)}')
    # # print(f'c = {c}')
    # for element in c:
    #     if a_multiply_b[element] > 0:
    #         return True
    # return False
    # ---------------------recursive-----------------------------
    
    if len(a) == 1 :
        for index in a:
            a_coeffs[index] = 1
        for index in b:
            b_coeffs[index] = 1
        a_multiply_b = polynomial_multiply(a_coeffs,b_coeffs)
        # print(f'a_coeffs = {a_coeffs}')
        # print(f'b_coeffs = {b_coeffs}')
        # print(f'a_multiply_b = {a_multiply_b}')
        # print(f'len of a_multiply_b = {len(a_multiply_b)}')
        # print(f'c = {c}')
        for element in c:
            if a_multiply_b[element] > 0:
                return True
        return False
    else:
        mid = len(a)//2
        return check_sum_exists(list(a)[0:mid], list(b)[0:mid], c, n) or check_sum_exists(list(a)[mid:], list(b)[mid:], c, n) or check_sum_exists(list(a)[0:mid], list(b)[mid:], c, n) or check_sum_exists(list(a)[mid:], list(b)[0:mid], c, n)

# print('-- Test 1 --')
# a = set([1, 2, 10, 11])
# b = set([2, 5, 8, 10])
# c = set([1, 2, 5,  8])
# print(f'check_sum_exists(a, b, c, 12) return {check_sum_exists(a, b, c, 12)}')
# assert not check_sum_exists(a, b, c, 12), f'Failed Test 1: your code returned true when the expected answer is false'

print('-- Test 2 --')
a = set([1, 2, 10, 11])
b = set([2, 5, 8, 10])
c = set([1, 2, 5,  8, 11])
print(f'check_sum_exists(a, b, c, 12) return {check_sum_exists(a, b, c, 12)}')
assert check_sum_exists(a, b, c, 12), f'Failed Test 2: your code returns false but note that 1 in a + 10 in b = 11 in c '

print('-- Test 3 --')
a={1, 4, 5, 7, 11, 13, 14, 15, 17, 19, 22, 23, 24, 28, 34, 35, 37, 39, 42, 44}
b={0, 1, 4, 9, 10, 11, 12, 15, 18, 20, 25, 31, 34, 36, 38, 40, 43, 44, 47, 49}
c={3, 4, 5, 7, 8, 10, 19, 20, 21, 24, 31, 35, 36, 37, 38, 39, 42, 44, 46, 49}
print(f'check_sum_exists(a, b, c, 50) return {check_sum_exists(a, b, c, 50)}')
assert check_sum_exists(a, b, c, 50), f'Failed Test 3: your code returns False whereas the correct answer is true eg., 4 + 0 = 4'

print('-- Test 4 --')
a={98, 2, 99, 40, 77, 79, 87, 88, 89, 27}
b={64, 66, 35, 69, 70, 40, 76, 45, 12, 60}
c={36, 70, 10, 44, 15, 16, 83, 20, 84, 55}
assert not check_sum_exists(a, b, c, 100), f'Failed Test 4: your code returns True whereas the correct answer is False'

print('All Tests Passed (15 points)!')
