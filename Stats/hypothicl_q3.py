import scipy.stats
import math

X = float(input('Enter the hypothetical average(mean) value: '))
xbar = float(input('Enter the sample mean, xbar: '))
stddev = float(input('Enter the standard deviation: '))
n = float(input('Enter the sample size: '))

ZScore = (xbar - X) / (stddev / (math.sqrt(n)))  # test statistics
print(ZScore)

alpha = float(input('Enter the significance level: '))

si = str(alpha)

CV = scipy.stats.norm.ppf(alpha)
cv = str(CV)

print('The critical value at ' + si + ' significance level is: ' + cv)

if ZScore > CV:
    print("Ho is accepted i.e the ABC company should purchase the site")
else:
    print("Ho is rejected")
2