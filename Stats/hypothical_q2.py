import scipy.stats
import math

p = float(input('Enter the hypothetical proportion: '))
sp = 70 / 400
n = float(input('Enter the sample size: '))

ZScore = (sp - p) / math.sqrt((p * (1 - p)) / n)
print(ZScore)

CI = int(input('Enter the significance level percentage: '))
alpha = (CI / 100)
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
        print('Ho is accepted i.e there not enough statistical evidence at the given confidence level to reject Ho')

if ZScore > 0:
    if ZScore > CV:
        print('Ho is rejected')
    else:
        print('Ho is accepted i.e there not enough statistical evidence at the given confidence level to reject Ho')
