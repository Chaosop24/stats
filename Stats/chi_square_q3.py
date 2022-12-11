from scipy.stats import chi2_contingency

# defining the table
data = [2,6,30,52,67,56,32,10,1]
stat, p, dof, expected = chi2_contingency(data)

# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (H0 holds true)')