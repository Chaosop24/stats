import scipy.stats
import math

X = float(input('Enter the hypothetical mean value: '))
xbar = float(input('Enter the sample mean, xbar: '))
stddev = float(input('Enter the standard deviation: '))
n = float(input('Enter the sample size: '))

ZScore = (xbar - X) / (stddev / (math.sqrt(n)))
print(ZScore)

CI = int(input('Enter the Confidence level: '))
alpha = 1 - (CI / 100)
si = str(alpha)

CV = scipy.stats.norm.ppf(1 - alpha / 2)
cv = str(CV)

print('The critical value at ' + si + ' significance level is: ' + cv)

if ZScore < 0:
    neg = CV * (-1)
    print('Since ZScore is negative, negative value of CV will be used')
    if ZScore < neg:
        print('Ho is rejected')
    else:
        print('Ho is accepted i.e there not enough statistical data at the given confidence level to reject Ho')

if ZScore > 0:
    if ZScore > CV:
        print('Ho is rejected')
    else:
        print('Ho is accepted i.e there not enough statistical evidence at the given confidence level to reject Ho')
