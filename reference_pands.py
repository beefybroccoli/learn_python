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

s7 = pd.Series(np.random.sample(5), index=['a','b','c','d','e'])
print(f's7 = {s7}')
print(f"s7.loc['a'] = {s7.loc['a']}")
print(f"s7.loc['a','c'] = {s7.loc[['a','c']]}")
print(f"s7.loc['a':'c'] = {s7.loc['a':'c']}")
print(f"s7.iloc[0] = {s7.iloc[0]}")
print(f"s7.iloc[[0,2]] = {s7.iloc[[0,2]]}")
print(f"s7.iloc[0:2] = {s7.iloc[0:2]}")
print("")

grades1 = pd.Series([17,44,28,8,3,0], index=['A','B','C','D','F','G'])
grades2 = pd.Series([76,122,151,21,0], index=['D','C','B','A','F'])
print(f'grades1 = {grades1}')
print(f'grades2 = {grades2}')
print(f'grades1 + grades2 = {grades1 + grades2}')
print(f'grades1.add(grades2) = {grades1.add(grades2)}')
print(f'grades1.add(grades2, fill_value=10) = {grades1.add(grades2, fill_value=0)}')
print("")

dies1 = pd.Series(np.random.randint(1,7, (100,)))
dies2 = pd.Series(np.random.randint(1,7, (100,)))
print(f'dies1 == dies2 return {dies1 == dies2}')
print("")

def convert_to_letter(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 65:
        return 'D'
    else:
        return 'F'

np.random.seed(1)
exam_grades = pd.Series(np.random.randint(60,101,100))
print(f'exam_grades = {exam_grades}')
curved_grades = exam_grades.multiply(1.05)
print("-------")
print(f'curved_grades = {curved_grades}')
print("-------")
letter_grades = curved_grades.apply(convert_to_letter)
print(f'letter_grades = {letter_grades}')
print("-------")
print(f'letter_grades.loc[:50] = {letter_grades.loc[:5]}')
print("-------")
print(f'letter_grades.iloc[:50] = {letter_grades.iloc[:5]}')

