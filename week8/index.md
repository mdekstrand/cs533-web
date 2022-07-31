# Week 8 — Regression ({date}`wk8 range`)

:::{updated} F21
:::

In this week, we are learning about linear regression with StatsModels.
All the examples will use the StatsModels OLS (ordinary least squares) model, generally with the
[formula interface](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ols.html#statsmodels.formula.api.ols).

## {{moverview}} Content Overview

:::{module} week8
:folder: cee8983d-7d3c-4329-8f30-adb8012576fa
:::

## {{mcal}} Deadlines

- Week 8 Quiz **Thursday Oct. 14 at 8AM**

## {{mvideo}} Introducing Regression

:::{video}
:name: 8-1 - Introducing Regression
:id: ce6dd7fd-7632-4853-b165-ac4e011f9745
:length: 5m6s
:slide-id: 495979F9A431DDB0%2173250
:slide-auth: AJyw9tJLQ2TII98
:::

## {{mvideo}} Statistical Modeling

:::{video}
:name: 8-2 - Modeling
:id: a32df5bb-b919-439a-98fc-ac4e011f96f7
:length: 8m6s
:slide-id: 495979F9A431DDB0%2173252
:slide-auth: AFQ5ZkCaaa2Qn8Q
:::

### Resources

- Review {video}`week4:sampling`
- [What is statistical modeling?](https://help.xlstat.com/s/article/what-is-statistical-modeling?language=en_US)

## {{mvideo}} Single Regression

In this video, I introduce single-variable regression.

:::{video} single-regression
:name: 8-3 - Single Regression
:id: 6974f533-c84a-425f-85c6-ac4e011f97ae
:length: 10m14s
:slide-id: 495979F9A431DDB0%2173257
:slide-auth: AOpDY3zSpDSX2zw
:::

:::{admonition} Slide Clarification
:class: note

On slide 6, where I show the slope, intercept, and variance in a model, I have extended the plot to include 0 at the left end of the *x*-axis.
This is to highlight the meaning of the intercept. It is important to note that the intercept is where the line **crosses zero**, not where it crosses the left Y-axis.

Also, when discussing this slide, I am imprecise but make it sound like the unexplained variance is the remainder after *projecting* the data onto the line.
It is the variance remaining after *subtracting* the line.
A video in Week 9 provides more clarity on this relationship.
:::

## {{mvideo}} Prediction and Inference

:::{video} pred-inf
:name: 8-4 - Prediction and Inference
:id: 79719da0-ac88-4bfc-acf7-ac4e011f9777
:length: 8m33s
:slide-id: 495979F9A431DDB0%2173259
:slide-auth: ADukYiT1K4jLngk
:::

## {{mvideo}} Categorical Predictors

:::{video}
:name: 8-5 - Categorical Predictors
:id: dd8e3e53-8776-4c62-9d23-ac5100090a29
:length: 3m41s
:slide-id: 495979F9A431DDB0%2173270
:slide-auth: AKJTXs7gpzSKE0Q
:::

## {{mvideo}} Testing Assumptions

:::{video}
:name: 8-6 - Testing Assumptions
:id: 9b75d72f-d616-497f-afda-ac51000909ef
:length: 9m46s
:slide-id: 495979F9A431DDB0%2173266
:slide-auth: APhGyKu3RTROISc
:::

## {{mdoc}} Regression Model Assumptions

:::{reading}
:title: Regression Model Assumptions
:url: https://www.jmp.com/en_us/statistics-knowledge-portal/what-is-regression/simple-linear-regression-assumptions.html
:length: 964 words
:::

Read [Regression Model Assumptions](https://www.jmp.com/en_us/statistics-knowledge-portal/what-is-regression/simple-linear-regression-assumptions.html) from JMP.

## {{mvideo}} Multiple Regression

:::{video}
:name: 8-7 - Multiple Regression
:id: 20d644fc-c4ca-40de-a03f-ac510014254e
:length: 19m8s
:slide-id: 495979F9A431DDB0%2173268
:slide-auth: ALxGFTYkfItgS8o
:::

## {{mvideo}} Measuring Prediction Accuracy

:::{video} prediction-accuracy
:name: 8-8 - Prediction Accuracy
:id: 5ba717f5-1c46-4118-a89e-ac51001564cd
:length: 9m12s
:slide-id: 495979F9A431DDB0%2173272
:slide-auth: AEe-Etx_iJxpOiw
:::

## {{mvideo}} Instances and Sampling

:::{video}
:name: 8-9 - Instances and Sampling
:id: ec19853e-2dfb-4774-b192-ac5100142bbb
:length: 9m40s
:slide-id: 495979F9A431DDB0%2173274
:slide-auth: ADEFTal_QoMtTcQ
:::

## {{mnotebook}} Supporting Notebooks

- [Regression notebook](../../resources/tutorials/Regressions.ipynb) with code supporting the Penguin examples
- The [correlation notebook](../../resources/tutorials/Correlation.ipynb) includes regression to support the movie examples

## {{mquiz}} Week 8 Quiz

Complete the Week 8 quiz in {{LMS}}.

## {{mdoc}} StatsModels Examples and User Guide

The following StatsModels pages document its OLS model:

- [Formula User Guide](https://www.statsmodels.org/stable/example_formulas.html)
- [OLS Examples](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html)
- [Linear Regression](https://www.statsmodels.org/stable/regression.html)

## {{mdoc}} Bootstrapping Linear Regression

:::{reading}
:title: Bootstrapping for Linear Regression
:length: 1950 words
:url: https://olebo.github.io/textbook/ch/18/hyp_regression.html
:::

Read [Bootstrapping for Linear Regression](https://olebo.github.io/textbook/ch/18/hyp_regression.html).

## {{massignment}} Assignment 4

[Assignment 4](../../assignments/A4/index.md) is due **October 24, 2020**.
