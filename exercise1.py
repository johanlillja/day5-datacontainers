# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:18:58 2022

@author: johan
"""

from scipy import linalg as la
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


A = np.reshape((np.arange(9)+1),[3,3])
b = np.array([1,2,3])

x = la.solve(A,b)

test_val = np.dot(A,x)

B = np.random.rand(3,3)

X = la.solve(A,B)

test = np.dot(A,X)  

eigenmatrix,eigenvals = la.eig(A)
print(eigenmatrix)
print(eigenvals)

inverse = la.inv(A)
determinant = la.det(A)

norm_1 = la.norm(A,ord=1)
norm_2 = la.norm(A,ord=2)



mu = 5
poissondist = stats.poisson(mu)

x1 = np.arange(stats.poisson.ppf(0.01,mu),stats.poisson.ppf(0.99,mu))



plt.bar(x1,poissondist.pmf(x1))

plt.bar(x1,poissondist.cdf(x1))

plt.hist(poissondist.rvs(size=1000))

mu = 5
sigma = 2

normaldist = stats.norm(mu,sigma) 

x2 = np.arange(stats.norm.ppf(0.01,mu,sigma),stats.norm.ppf(0.99,mu,sigma))


plt.bar(x2,normaldist.pdf(x2))
plt.bar(x2,normaldist.cdf(x2))
plt.hist(normaldist.rvs(size=1000))

t,p=  stats.ttest_ind(normaldist.rvs(size=1000),normaldist.rvs(size=1000))

if p>0.05:
    print('We can not reject the null hypothesis')
