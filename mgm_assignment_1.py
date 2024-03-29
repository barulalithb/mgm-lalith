# -*- coding: utf-8 -*-
"""MGM Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j4J0Uz5S8EyFhKNj_FjcHFlzroSkVUwx

#Question 1
Sampling using MLE
"""

import numpy as np

# A function for our question.
def sample_green_or_blue(n=1, p=2/3, trials=10):
  for i in range(trials):
    sample = np.random.binomial(1, 2/3, size=None)
    if sample==0:
      k="Blue Ball"
    if sample ==1:
      k="Green ball"
    print(">> Random Sample obtained from the desired distribution: ", k)
  return None

# number of trials, probability of each trial
# as per question n=1 and p=2/3
n, p = 1, 2/3

# also we consider no of trials = None as per the question
# we obatin only one single random trial
s = np.random.binomial(1, 2/3, size=None)

sample_green_or_blue()

"""#Question 2
Sampling using inverse CDF transform
"""

import numpy as np
import matplotlib.pyplot as plt

# As per question
rolls = np.array([1, 3, 2, 4, 2, 3, 5, 6, 3, 2])

# R_X
outcomes = np.array([1, 2, 3, 4, 5, 6])

# The PMF
pmf = [np.sum(rolls == outcome) / len(rolls) for outcome in outcomes]
print(pmf)

# The CDF: cumulative sum of the PMF
cdf = np.cumsum(pmf)
print(cdf)

# PMF plot (I wanted to make it look like that was given in lecture slides)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(outcomes, pmf, color='b')
plt.vlines(x=[1, 2, 3, 4, 5, 6], ymin=[0, 0, 0, 0, 0, 0], ymax=pmf, colors='b', lw=2)
plt.title('Probability Mass Function (PMF)')
plt.xlabel('Die Roll Outcome')
plt.ylabel('Probability')
plt.xticks(outcomes)
plt.yticks(np.linspace(0, 0.6, num=7))


# Plotting the CDF
plt.subplot(1, 2, 2)
plt.step(outcomes, cdf, where='post', color='green')
plt.scatter(outcomes, cdf, color='k')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Die Roll Outcome')
plt.ylabel('Cumulative Probability')
plt.xticks(outcomes)
plt.yticks(np.linspace(0, 1, num=11))

plt.tight_layout()
plt.show()

# PMF and CDF values
print("The PMF vlaues:",pmf,"\n", "The CDF values", cdf)

# Sampling from the uniform distribution [0, 1] i.e., u ~ Uniform[0,1]
u = np.random.uniform(0, 1)

# now we need to find the smallest outcome x such that F(x) >= y
# The function np.argmax returns the first index of the maximum value, which in this case
# is the first occurrence where CDF is greater than or equal to y_sample and so we write the code as below,
x = outcomes[np.argmax(cdf >= u)]
print(u, "and", x)

import numpy as np
import matplotlib.pyplot as plt
#n-sided generalization problem
# Now we Simulate die rolls and plot the Probability Mass Function (PMF).
# Number of sides on the die = n
# Number of times the die is rolled or the sampling = n_samples:

def n_sided_die_roll(n, n_samples):
    # I am putting seed to reproduce my results
    np.random.seed(0)

    #a random variable assumed for die roll, where randint produces integer in the given range [1,n]
    rolls = np.random.randint(1, n + 1, size=n_samples)

    #calculating the histogram for PMF
    pmf, bin_edges = np.histogram(rolls, bins=n, range=(1 -0.5, n + 1-0.5), density=True)
    # print(pdf, "\n", bin_edges)

    #the outcomes to plot on x-axis
    outcomes = bin_edges[:-1] + np.diff(bin_edges) / 2
    # print(outcomes)

    # the PMF plot
    plt.figure(figsize=(8, 6))
    plt.bar(outcomes, pmf, width=0.8, color='r')
    plt.title('Probability Mass Function (PMF) for a {}-Sided Die'.format(n))
    plt.xlabel('Die Roll')
    plt.ylabel('Probability Value')
    plt.xticks(outcomes)
    plt.yticks(np.linspace(0, max(pmf)+0.2, num=11))
    plt.show()

# some example that we can play with
n_sides = 10
n_samples = 2 * n_sides
n_sided_die_roll(n_sides, n_samples)

# The task is to write code to generate inverse CDF sampling to find the sample corresponding to a given uniform random value.
# possible outcomes = outcomes
# cdf values = cdf
# uniform random variable = u => u ~ Uniform[0,1]
# the outcome must be a sample that is correspoding to the uniform random variable u.


def inverse_cdf_sampling(outcomes, cdf, u):

    # Finding the index where u lies in the CDF array
    # in question this index = k
    index = np.searchsorted(cdf, u, side='right') - 1

    # consider the case where u = 1
    if index == len(cdf) - 1:
        return outcomes[index]

    # distances given in the question
    distance_to_left = u - cdf[index]
    distance_to_right = cdf[index + 1] - u

    # Comparing distances and selecting the sample
    if distance_to_left < distance_to_right:
        return outcomes[index]
    elif distance_to_right < distance_to_left:
        return outcomes[index + 1]
    else:
        # If distances are equal, flip a fair coin to decide
        return outcomes[index] if np.random.rand() < 0.5 else outcomes[index + 1]

# Example for generating a vlaue by inverse CDF from a uniform random varibale pick
# For a 6-sided die
outcomes = np.arange(1, 7)
#fair die cdf values
cdf_values = np.cumsum([1/6] * 6)
#uniform random variable ~ Uniform[0,1]
u = np.random.uniform(0, 1)

sample = inverse_cdf_sampling(outcomes, cdf_values, u)
print(">>> Our generated sample from inverse cdf sampling: ",sample)