import numpy as np
import pandas as pd
from datetime import date
import os

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
print("---------")
letter_grades.columns = ['Grade']
print(f'letter_grades = \n{letter_grades}')

dataframe_1 = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
dataframe_1.columns = ['A','B','C']
dataframe_1.index = ['A','B','C']
print(f'dataframe_1 = \n{dataframe_1}')
print("")

dataframe_2 = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['A','B','C'],index=['AA','BB','CC'])
print(f'dataframe_2 = \n{dataframe_2}')
print("")

people = pd.Series(['tom','mason','susan','john'], index=['A','B','C','D'])
places = pd.Series(['CA','TX','OK'], index=['A','B','C'])
things = pd.Series(['orange','car','monitor'], index=['A','B','C'])
dataframe_3 = pd.DataFrame([people, places, things])
print(f'dataframe_3 = \n{dataframe_3}')
print("")

np.random.seed(2)
array_1 = np.random.choice(['A','B','C','D','F'], 100, p=[0.2, 0.4, 0.3, 0.08, 0.02])
array_2 = np.random.choice(['AA','BB','CC','DD','FF'], 50, p=[0.3, 0.4, 0.2, 0.1, 0])
array_3 = np.random.choice(['a','b','c','d','f'], 100, p=[0.2, 0.4, 0.3, 0.08, 0.02])
s1 = pd.Series(array_1)
s2 = pd.Series(array_2)
s3 = pd.Series(array_3)
dataframe_5 = pd.concat([s1,s2,s3], axis=1)
dataframe_5.columns = ['grade_1','grade_2','grade_2']
print(f'dataframe_5 = \n{dataframe_5}')
print("")

directory = os.getcwd()
print(f'directory = {directory}')
file_path = directory+'\\files\\ds_salaries.csv'
print(f'file_path = {file_path}')
dataframe = pd.read_csv(file_path, encoding='utf-8')
EID = ['EID' + str(i) for i in range(100, len(dataframe) + 100)]
# dataframe.index = EID # ?????????????????
print(f'dataframe = {dataframe}')
print(f'dataframe.columns = {dataframe.columns}')
print(f'dataframe.index = {dataframe.index}')
print(f'dataframe.shape = {dataframe.shape}')
print(f'dataframe.head() return \n{dataframe.head()}')
print(f'dataframe.tail() return \n{dataframe.tail()}')
print(f'dataframe.describe() return \n{dataframe.describe()}')
print(f'dataframe.info() return \n{dataframe.info()}')
print(f"dataframe['salary'] return \n{dataframe['salary']}")
print(f'dataframe.salary return \n{dataframe.salary}')
print(f"dataframe['salary','job_title'] return \n{dataframe[['salary','job_title']]}")
print(f"dataframe.loc[0] return \n{dataframe.loc[0]}")
print(f"dataframe.loc[0:5] return \n{dataframe.loc[0:5]}")
print(f"dataframe.iloc[0] return \n{dataframe.iloc[0]}")
print(f"dataframe.iloc[0:10] return \n{dataframe.iloc[0:10]}")
print(f"dataframe.iloc[0,3,5] return \n{dataframe.iloc[[0,3,5]]}")
print(f"dataframe.iloc[0:10][['salary']] return \n{dataframe.iloc[0:10][['salary']]}")
print(f"dataframe[['salary']].iloc[:5] return \n{dataframe[['salary']].iloc[:5]}")
print("")

