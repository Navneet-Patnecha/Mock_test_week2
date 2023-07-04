'''
 Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as 
 input, representing two samples. The function should perform a two-sample t-test and 
 return the p-value. Use the ‘scipy.stats’ module in Python to calculate the t-test 
 and p-value.

'''


from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_value, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [10, 15, 20, 25, 30]
sample2 = [20, 30, 40, 50, 60]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)