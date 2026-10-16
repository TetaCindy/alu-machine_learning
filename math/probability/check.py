import numpy as np
from exponential import Exponential
from normal import Normal
from binomial import Binomial

np.random.seed(0)
d = np.random.exponential(0.5, 100).tolist()
e1, e2 = Exponential(d), Exponential(lambtha=2)
print('f(1):', e1.pdf(1), e2.pdf(1))
print('F(1):', e1.cdf(1), e2.cdf(1))

np.random.seed(0)
d = np.random.normal(70, 10, 100).tolist()
n1, n2 = Normal(d), Normal(mean=70, stddev=10)
print('Mean/Std:', n1.mean, n1.stddev, n2.mean, n2.stddev)
print('Z(90):', n1.z_score(90), n2.z_score(90))
print('X(2):', n1.x_value(2), n2.x_value(2))
print('PSI(90):', n1.pdf(90), n2.pdf(90))
print('PHI(90):', n1.cdf(90), n2.cdf(90))

np.random.seed(0)
d = np.random.binomial(50, 0.6, 100).tolist()
b1, b2 = Binomial(d), Binomial(n=50, p=0.6)
print('n, p:', b1.n, b1.p, b2.n, b2.p)
print('P(30):', b1.pmf(30), b2.pmf(30))
print('F(30):', b1.cdf(30), b2.cdf(30))
