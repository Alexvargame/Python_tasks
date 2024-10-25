import pandas as pd
import numpy as np
d={'X': [78,85,96,80,86], 'Y': [84,94,89,83,86], 'Z': [86,97,96,72,83 ]}
df1=pd.DataFrame(d)
print(df1)
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)
print(df1.loc[df1['X']==86])
print(df1.iloc[[3]])
df.reset_index(level=0, inplace=True)
print(df)
print(df.to_string(index=False))
print(df.sample(frac=1))
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
print("Data Series:")
print(s1)
print(s2)
df1 = pd.concat([s1, s2], axis=1)
print("New DataFrame combining two series:")
print(df1)
print(df['name'].tolist())
print(df.sort_values(['attempts', 'name'], ascending=[True, True]))
