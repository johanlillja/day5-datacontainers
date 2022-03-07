# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:09:33 2022

@author: johan
"""
import pandas as pd


# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}


army = pd.DataFrame(raw_data)
army.set_index('origin')

print(army['veterans'])

print(army[['veterans','deaths']])

print(army.columns)



selection1 = army[(army['origin']=='Alaska') | (army['origin']=='Maine')][['origin','deaths','size','deserters']]

selection2 = army.iloc[3:7,3:6]

selection3 = army.iloc[4:,::]

selection4 = army.iloc[0:4,::]

selection5 = army.iloc[::,3:7]

selection6 = army[army['deaths']>50]

selection7 = army[(army['deaths']<50) | (army['deaths']>500)]

selection8 = army[army['regiment'] != 'Dragoons']

selection9 = army[(army['origin']=='Texas') | (army['origin'] == 'Arizona')]

selection10 = army[army['origin']=='Arizona'].iloc[:,2]

selection11 = army['deaths'].iloc[2]