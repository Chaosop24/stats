# Importing library
from scipy.stats import f_oneway

# Performance when each of the engine
# oil is applied
performance1 = [6,5,5]
performance2 = [7,5,4]
performance3 = [3,3,3]
performance4 = [8,7,4]

# Conduct the one-way ANOVA
oneway = f_oneway(performance1, performance2, performance3, performance4)
print(oneway)