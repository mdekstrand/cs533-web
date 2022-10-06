# Week 8 — Regression ({date}`wk8 range`)

:::{updated} F22
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
:length: 5m6s
:::

## {{mvideo}} Statistical Modeling

:::{video}
:name: 8-2 - Modeling
:length: 8m6s
:::

### Resources

- Review {video}`week4:sampling`
- [What is statistical modeling?](https://help.xlstat.com/s/article/what-is-statistical-modeling?language=en_US)

## {{mvideo}} Single Regression

In this video, I introduce single-variable regression.

:::{video} single-regression
:name: 8-3 - Single Regression
:length: 10m14s
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
:length: 8m33s
:::

## {{mvideo}} Categorical Predictors

:::{video}
:name: 8-5 - Categorical Predictors
:length: 3m41s
:::

## {{mvideo}} Testing Assumptions

:::{video}
:name: 8-6 - Testing Assumptions
:length: 9m46s
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
:length: 19m8s
:::

## {{mvideo}} Measuring Prediction Accuracy

:::{video} prediction-accuracy
:name: 8-8 - Prediction Accuracy
:length: 9m12s
:::

## {{mvideo}} Instances and Sampling

:::{video}
:name: 8-9 - Instances and Sampling
:length: 9m40s
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
