import numpy as np
import pandas as pd
from datetime import date

print("hello world")
s1 = pd.Series(np.arange(0,5))
print(f's1 = {s1}')
print(f'type(s1) return {type(s1)}')
print("")

s2 = pd.Series(np.arange(0,5), index=['a','b','c','d','e'])
print(f's2 = {s2}')
s2.index = ['A','B','C','D','E']
print(f's2 = {s2}')
print("")

s3 = pd.Series(5)
print(f's3 = {s3}')
print("")

s4 = pd.Series([1,2,3,4,5])
print(f's4 = {s4}')
print(f's4.index = {s4.index}')
print('')

birthdays = {
    'Aaron': date(2001, 10, 10),
    'Brian': date(2002, 6, 6),
    'Christine': date(2003, 2, 2),
    'Di': date(2004, 9, 9),
}
s5 = pd.Series(birthdays)
print(f's5 = {s5}')
print(f's5.index = {s5.index}')
print(f's5.values = {s5.values}')
print('')

array = np.array([1,2,3,np.nan,5,6,7,np.nan,9,10])
print(f'array = {array}')
print(f'array.mean() = {array.mean()}')
print(f'array.sum() = {array.sum()}')
print('')

s6 = pd.Series(array)
print(f's6 = {s6}')
print(f's6.mean() = {s6.mean()}')
print(f's6.sum() = {s6.sum()}')
print(f's6.mean(skipna=True) = {s6.mean(skipna=True)}')
print(f's6.sum(skipna=True) = {s6.sum(skipna=True)}')
print('')