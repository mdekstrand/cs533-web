# Week 9 — Models & Prediction (Oct. 18–22)

:::{updated} F21
:::

This week talks more about regression, simulation, and introduces the idea of minimizing a loss function.

## {{moverview}} Content Overview

:::{module} week9
:folder: eba298d6-9234-4791-88f6-adc101859673
:::

## {{mvideo}} Introduction

This video introduces the week.

:::{video}
:length: 3m7s
:name: 9-1 - More Regression
:slide-id: 495979F9A431DDB0%2173276
:slide-auth: AHsbW2hF0gaAAXM
:::

## {{mvideo}} Simulation

This video talks more about simulation as a method for studying statistical techniques, which you are doing in the assignment.
I also describe more of NumPy's random number generation facilities.

:::{video}
:length: 14m48s
:name: 9-2 - Simulation
:slide-id: 495979F9A431DDB0%2173277
:slide-auth: AMmsQqYDB60pYbk
:::

:::{tip}
You should set random seeds for all work that will need randomness, including train/test splits for evaluating predictors.
:::

## {{mvideo}} Variance, R², and the Sum of Squares

This video provides more detail on *explained variance* and what the $R^2$ means.

:::{video}
:length: 5m59s
:name: 9-3 - Variance and Sums of Squares
:slide-id: 495979F9A431DDB0%2173278
:slide-auth: APvhgyfko-eH9MU
:::

### Resources

- [Penn State R² notes](https://online.stat.psu.edu/stat462/node/95/)
- [Penn State Sum of Squares Notes](https://online.stat.psu.edu/stat462/node/104/)
- [Proof of SSTO = SSR + SSE](https://web.njit.edu/~wguo/Math644_2012/Math644_Chapter%201_part4.pdf) (on Page 2)

## {{mvideo}} Overfitting

This video introduces the idea of *overfitting*: learning too much from the training data so we can't predict the testing data.

:::{video} overfitting
:length: 10m31s
:name: 9-4 - Overfitting
:slide-id: 495979F9A431DDB0%2173279
:slide-auth: ABqv_ZE_MmpDcLk
:::

## {{mnotebook}} Overfitting Simulation

- [Overfitting Simulation notebook](../resources/tutorials/OverfittingSimulation.ipynb)

## {{mdoc}} Overfitting Example

:::{reading}
:title: Example of overfitting and underfitting in machine learning
:url: https://keeeto.github.io/blog/bias_variance/
:length: 1180 words
:::

Read [Example of overfitting and underfitting in machine learning](https://keeeto.github.io/blog/bias_variance/).

## {{mvideo}} Replication, Bias, and Variance

:::{video}
:length: 9m16s
:name: 9-5 - Bias-Variance
:slide-id: 495979F9A431DDB0%2173280
:slide-auth: ANKJOxuY0wR0nIQ
:::

## {{mdoc}} Bias-Variance Tradeoff

:::{reading}
:title: Understanding the Bias-Variance Tradeoff
:url: http://scott.fortmann-roe.com/docs/BiasVariance.html
:length: 3000 words
:::

Read [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html).

### Resources

Further reading: [Lecture 12: Bias-Variance Tradeoff](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote12.html).

## {{mvideo}} Optimizing Loss

:::{video} optimizing-loss
:length: 15m23s
:name: 9-6 - Optimizing Loss
:::

### Links

- The {py:func}`scipy.optimize.minimize` function.
- The [minimization regression notebook](../resources/tutorials/MinimizeRegression.ipynb) notebook.
- Our introduction to the idea of an {term}`objective function`.

## {{mquiz}} Week 9 Quiz

Take the Week 9 quiz in Blackboard (will be up by end of Saturday).

Since this is the second of two very closely intertwined weeks, there are questions about {module}`week8` in the quiz ads well.

## {{mtask}} Practice

There are several ways you can practice the material so far:

- Practice more regressions with World Bank data
- Measure World Bank data predictive accuracy with train-test evaluation and mean squared error

## {{massignment}} Assignment 4

Assignment 4 is due **October 24, 2021**.
