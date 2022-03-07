# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:56:38 2022

@author: johan
"""

import pandas as pd


drinks = pd.read_csv('drinks.csv')
drinks.set_index('continent')


continent = drinks[['beer_servings','continent']].groupby('continent').mean()
print(continent.idxmax())

continent_wine = drinks[['wine_servings','continent']].groupby('continent').mean()

print(continent_wine)

continent_all = drinks[['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol','continent']].groupby('continent').mean()

print(continent_all)

continent_all_median = drinks[['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol','continent']].groupby('continent').median()

print(continent_all_median)

spirit = drinks.agg({'spirit_servings':['min','max','median']})

