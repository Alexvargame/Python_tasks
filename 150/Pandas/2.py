import pandas as pd
import numpy as np
d={'X': [78,85,96,80,86], 'Y': [84,94,89,83,86], 'Z': [86,97,96,72,83 ]}
df=pd.DataFrame(d)
print(df)
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print(df)
print("-")
print(df.info)
print("-")
print(df.iloc[:3])
print("-")
print(df.iloc[[1,3,5,6],:1])
print("-")
print(df.count())
print(len(df.axes[0]))
print(len(df.axes[1]))
print(df[df['score'].isnull()])
print(df[df['score'].between(15,20)])
print(df[(df['score']>15)&(df['attempts']<3)])
df.loc['d','score']=11.5
print(df)
print(df['attempts'].sum())
print(df['score'].mean())
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print(df)
df=df.drop('k')
print(df)
df.sort_values(by=['name', 'score'], ascending=[False, True])
print(df)
df['name'] = df['name'].replace('James', 'Suresh')
print(df)
color = ['Red', 'Blue', 'Orange', 'Red', 'White', 'White', 'Blue', 'Green', 'Green', 'Red']
df['color']=color
print(df)
print(df.info)
print(list(df.columns.values))
print(list(df.rows.values))
