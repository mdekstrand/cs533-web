# 🚧 Week 9 — Models & Prediction (Oct. 18–22) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
:::

## {{moverview}} Content Overview

:::{module} week9
:::

## {{mvideo}} Introduction

This video introduces the week.

:::{video}
:id: 6ec6be44-653a-44d0-8db3-ac57000b2560
:length: 3m7s
:slide-id: 495979F9A431DDB0%2173276
:slide-auth: AHsbW2hF0gaAAXM
:::

## {{mvideo}} Simulation

This video talks more about simulation as a method for studying statistical techniques, which you are doing in the assignment.
I also describe more of NumPy's random number generation facilities.

:::{video}
:id: db2449d6-c0ec-454b-b813-ac57000b2514
:length: 14m48s
:slide-id: 495979F9A431DDB0%2173277
:slide-auth: AMmsQqYDB60pYbk
:::

:::{tip}
You should set random seeds for all work that will need randomness, including train/test splits for evaluating predictors.
:::

## {{mvideo}} Variance, R², and the Sum of Squares

This video provides more detail on *explained variance* and what the $R^2$ means.

:::{video}
:id: ee53066a-f9c1-48fc-abc8-ac57000b2537
:length: 5m59s
:slide-id: 495979F9A431DDB0%2173278
:slide-auth: APvhgyfko-eH9MU
:::

### Resources

- [Penn State R² notes](https://online.stat.psu.edu/stat462/node/95/)
- [Penn State Sum of Squares Notes](https://online.stat.psu.edu/stat462/node/104/)
- [Proof of SSTO = SSR + SSE](https://web.njit.edu/~wguo/Math644_2012/Math644_Chapter%201_part4.pdf) (on Page 2)

## {{mvideo}} Overfitting

This video introduces the idea of *overfitting*: learning too much from the training data so we can't predict the testing data.

:::{video}
:id: 026f0abb-b736-4238-8e38-ac57000b2588
:length: 10m31s
:slide-id: 495979F9A431DDB0%2173279
:slide-auth: ABqv_ZE_MmpDcLk
:::

## {{mnotebook}} Overfitting Simulation

- [Overfitting Simulation notebook](./OverfittingSimulation.ipynb)

## {{mdoc}} Overfitting Example

:::{reading}
:title: Example of overfitting and underfitting in machine learning
:url: https://keeeto.github.io/blog/bias_variance/
:length: 1180 words
:::

Read [Example of overfitting and underfitting in machine learning](https://keeeto.github.io/blog/bias_variance/).

## {{mvideo}} Replication, Bias, and Variance

:::{video}
:id: 9762d0fb-57b9-4880-9d97-ac580037f27d
:length: 9m16s
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

:::{video}
:id: e68b9f9d-13a6-4d98-8a4d-ac580037f259
:length: 14m3s
:slide-id: 495979F9A431DDB0%2173288
:slide-auth: AKxIYJP7LW4ct2Y
:::

## {{mnotebook}} Loss-Based Regression Notebook

Read the [minimization regression notebook](./BadRegression.ipynb) notebook.

## {{mquiz}} Week 9 Quiz

Take the Week 9 quiz in Blackboard (will be up by end of Saturday).

## {{mtask}} Practice

There are several ways you can practice the material so far:

- Practice more regressions with World Bank data
- Measure World Bank data predictive accuracy with train-test evaluation and mean squared error

## {{massignment}} Assignment 4

Assignment 4 is due **October 25, 2020**.
