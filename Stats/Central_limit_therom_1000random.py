from scipy.stats import norm
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
random_dataset = np.random.default_rng(12345).random(100000)
random_dataset *= 100

database_of_means = np.zeros(1000)
database_of_meansA = np.zeros(1000)
database_of_meansB = np.zeros(1000)
database_of_meansC = np.zeros(1000)

for i in range(1000):
    database_of_meansA[i] = np.random.choice(random_dataset, size=100).mean()
    database_of_meansB[i] = np.random.choice(random_dataset, size=1000).mean()
    database_of_meansC[i] = np.random.choice(random_dataset, size=10000).mean()

plt.hist(database_of_meansA, edgecolor="blue", bins=20)
plt.show()
meanA = database_of_meansA.mean()
stdevA = database_of_meansA.std()
x_axis = np.arange(0, 100, 0.01)
plt.plot(x_axis, 100 * norm.pdf(x_axis, meanA, stdevA))
plt.show()

plt.hist(database_of_meansB, edgecolor="blue", bins=20)
plt.show()
meanB = database_of_meansB.mean()
stdevB = database_of_meansB.std()
x_axis = np.arange(0, 100, 0.01)
plt.plot(x_axis, 1000 * norm.pdf(x_axis, meanB, stdevB))
plt.show()

plt.hist(database_of_meansC, edgecolor="blue", bins=20)
plt.show()
meanC = database_of_meansC.mean()
stdevC = database_of_meansC.std()
x_axis = np.arange(0, 100, 0.01)
plt.plot(x_axis, 10000 * norm.pdf(x_axis, meanC, stdevC))
plt.show()