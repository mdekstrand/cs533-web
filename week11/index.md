# Week 11 — More Modeling ({date}`wk11 range`)

In this week, we're going to learn more about model building, that will be useful in Assignment 5:

- Feature engineering
- SciKit-Learn pipelines and workflows
- Regularization
- Analyzing model results

## {{moverview}} Content Overview

:::{module} week11
:::

## {{mvideo}} Intro & Context

In this video, I review where we are at conceptually, and recap the ideas of estimating conditional probability and expectation.

:::{video} eval-intro
:length: 4m39s
:name: 11-1 - Intro and Context
:id: 40a41051-8c07-443c-b7d1-ac66002b3208
:slide-id: 495979F9A431DDB0%2173320
:slide-auth: AJXlvBsutNDBkoE
:::

## {{mvideo}} Feature Transforms

What are some useful techniques for engineering features in an application?

:::{video}
:length: 21m3s
:name: 11-2 - Feature Transforms
:id: 80203946-b811-4ecb-b703-ac660033edd1
:slide-id: 495979F9A431DDB0%2173322
:slide-auth: ABC9rmLnxkHsstY
:::

## {{mvideo}} Workflow

How do you do feature engineering and model selection in a machine learning workflow?
What is the iterative process involved?

:::{video}
:length: 14m29s
:name: 11-3 - Workflow
:id: 71b1aa35-8435-4eae-ae32-ac660033ee09
:slide-id: 495979F9A431DDB0%2173324
:slide-auth: AGk8GhY4fx1Mnm8
:::

## {{mvideo}} SciKit Pipelines

In this video, I introduce SciKit *pipelines* that put multiple transformations together.

:::{video}
:length: 7m19s
:name: 11-4 - SciKit Pipelines
:id: f448da70-c2d2-4c1b-942b-ac66003656a1
:slide-id: 495979F9A431DDB0%2173328
:slide-auth: ACahS4jRCAE3ueU
:::

## {{mdoc}} SciKit Learn Pipelines

Read the [SciKit-Learn User Guide chapter on pipelines](https://scikit-learn.org/stable/modules/compose.html).

## {{mdoc}} SciKit Learn Preprocessing

Read the [SciKit-Learn User Guide chapter on pre-processing](https://scikit-learn.org/stable/modules/preprocessing.html).

## {{mvideo}} Regularization

This video introduces regularization: ridge regression, lasso regression, and the elasticnet.
Lasso regression can help with (semi-)automatic feature selection.

:::{video} regularization
:length: 15m4s
:name: 11-5 - Regularization
:id: fa457314-7344-48cd-af1f-ac660039cbc4
:slide-id: 495979F9A431DDB0%2173326
:slide-auth: APzIM2g9IcVX0XQ
:::

## {{mnotebook}} Pipeline and Regularization

[This notebook](../resources/tutorials/SciKitPipeline.ipynb) demonstrates pipelines and $L_2$ regression, and performs a significance test of classifier improvement.

It also shows a training of a decision tree (next video).

## {{mnotebook}} Advanced Pipelines

The [Advanced Pipelines notebook](../resources/tutorials/AdvancedPipeline.ipynb) demonstrates a much more advanced SciKit-Learn pipeline.

## {{mvideo}} Models and Depth

What does the world look like beyond logistic regression?
Can a model output be a feature?

:::{video}
:length: 7m23s
:name: 11-6 - Models and Depth
:id: 220a8acb-a901-49e7-bf9e-ac66003d7033
:slide-id: 495979F9A431DDB0%2173330
:slide-auth: APtXIrllUsY0_vY
:::

## {{mvideo}} Inference and Ablation

How do we understand, *robustly*, the performance of our system?
What contributes to its performance?

:::{video} ablation
:length: 14m55s
:name: 11-7 - Inference and Ablation
:id: 589628b2-30ce-4c38-ba45-ac66003f5163
:slide-id: 495979F9A431DDB0%2173331
:slide-auth: "%21AAlNEpWRX05DM90"
:::

## {{mdoc}} Statistical Significance Tests

:::{reading}
:title: Statistical Significance Tests for Comparing Machine Learning Algorithms
:url: https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/
:length: 3400 words
:::

Read [Statistical Significance Tests for Comparing Machine Learning Algorithms](https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/).

:::{note}
In the Week 9 activity, we used the paired *t*-test for comparing the output of two regression models.
Our use of this test did **not** violate the guidance in this reading — why is that?
:::

For further reading, you can also see [Approximate Statistical Tests](http://dx.doi.org/10.1162/089976698300017197).

## {{mvideo}} Dates

This video discusses how to use work with dates in Pandas.

:::{video}
:length: 8m34s
:name: 11-8 - Dates
:id: db1dc799-8ed1-4a7b-960e-ac69001a590d
:slide-id: 495979F9A431DDB0%2173338
:slide-auth: ALt4_zuupKaPObs
:::

### Links

- [Date operations notebook](./Dates.ipynb)
- [Pandas time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- [Pandas time deltas](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)
- [DateOffset](https://pandas.pydata.org/pandas-docs/stable/reference/offset_frequency.html)
- [Format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

## {{mquiz}} Quiz 11

Quiz 11 is in Canvas.

## {{massignment}} Assignment 5

[Assignment 5](../../assignments/A5/index.md) is due **{date}`wk11 sun long`**.
