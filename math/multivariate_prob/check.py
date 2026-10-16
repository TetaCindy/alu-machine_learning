import importlib
import numpy as np
mean_cov = importlib.import_module('0-mean_cov').mean_cov
correlation = importlib.import_module('1-correlation').correlation
from multinormal import MultiNormal

cov = [[36, -30, 15], [-30, 100, -20], [15, -20, 25]]
np.random.seed(0)
X = np.random.multivariate_normal([12, 30, 10], cov, 10000)
mean, c = mean_cov(X)
print(mean)
print(c)

print(correlation(np.array(cov)))

np.random.seed(0)
data = np.random.multivariate_normal([12, 30, 10], cov, 10000).T
mn = MultiNormal(data)
print(mn.mean)
print(mn.cov)

x = np.random.multivariate_normal([12, 30, 10], cov, 1).T
print(x)
print(mn.pdf(x))
