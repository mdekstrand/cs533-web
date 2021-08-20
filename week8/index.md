# Week 8 — Regression
{% import 'video.md' as media %}

!!! warning "Draft content"

    This content is still in draft state and has not yet been finalized.
    Do not depend on it as the final requirements for this week.

In this week, we are learning about linear regression with StatsModels.
All the examples will use the StatsModels OLS (ordinary least squares) model, generally with the
[formula interface](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ols.html#statsmodels.formula.api.ols).

Activities:

[TOC]

## :a-video: Introducing Regression {: data-length="5m6s"}

=== "Video"

    {{ media.video('ce6dd7fd-7632-4853-b165-ac4e011f9745') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173250', 'AJyw9tJLQ2TII98') }}

## :a-video: Statistical Modeling {: data-length="8m6s"}

=== "Video"

    {{ media.video('a32df5bb-b919-439a-98fc-ac4e011f96f7') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173252', 'AFQ5ZkCaaa2Qn8Q') }}

### Resources

- Review the [Data Generating Process](../week4/index.md#sampling)
- [What is statistical modeling?](https://help.xlstat.com/s/article/what-is-statistical-modeling?language=en_US)

## :a-video: Single Regression {: data-length="10m14s"}

In this video, I introduce single-variable regression.

=== "Video"

    {{ media.video('6974f533-c84a-425f-85c6-ac4e011f97ae') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173257', 'AOpDY3zSpDSX2zw') }}

!!! note "Slide Clarification"

    On slide 6, where I show the slope, intercept, and variance in a model, I have extended the plot to include 0 at the left end of the *x*-axis.
    This is to highlight the meaning of the intercept. It is important to note that the intercept is where the line **crosses zero**, not where it crosses the left Y-axis.

    Also, when discussing this slide, I am imprecise but make it sound like the unexplained variance is the remainder after *projecting* the data onto the line.
    It is the variance remaining after *subtracting* the line.
    I am preparing a video for Week 9 that will provide more clarity on this relationship.

## :a-video: Prediction and Inference {: data-length="8m33s"}

=== "Video"

    {{ media.video('79719da0-ac88-4bfc-acf7-ac4e011f9777') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173259', 'ADukYiT1K4jLngk') }}

## :a-quiz: Week 8 Quiz

Complete the Week 8 quiz in Blackboard.

## :a-video: Categorical Predictors {: data-length="3m41s"}

=== "Video"

    {{ media.video('dd8e3e53-8776-4c62-9d23-ac5100090a29') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173270', 'AKJTXs7gpzSKE0Q') }}

## :a-video: Testing Assumptions {: data-length="9m46s"}

=== "Video"

    {{ media.video('9b75d72f-d616-497f-afda-ac51000909ef') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173266', 'APhGyKu3RTROISc') }}

## :a-reading: Regression Model Assumptions {: data-length="964 words"}

Read [Regression Model Assumptions](https://www.jmp.com/en_us/statistics-knowledge-portal/what-is-regression/simple-linear-regression-assumptions.html) from JMP.

## :a-video: Multiple Regression {: data-length="19m8s"}

=== "Video"

    {{ media.video('20d644fc-c4ca-40de-a03f-ac510014254e') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173268', 'ALxGFTYkfItgS8o') }}

## :a-video: Measuring Prediction Accuracy {: data-length="9m12s"}

=== "Video"

    {{ media.video('5ba717f5-1c46-4118-a89e-ac51001564cd') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173272', 'AEe-Etx_iJxpOiw') }}

## :a-video: Instances and Sampling {: data-length="9m40s"}

=== "Video"

    {{ media.video('ec19853e-2dfb-4774-b192-ac5100142bbb') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173274', 'ADEFTal_QoMtTcQ') }}

## :a-notebook: Supporting Notebook

- [Regression notebook](../../resources/tutorials/Regressions.ipynb) with code supporting the Penguin examples
- I have added the regression code to the [correlation notebook](../../resources/tutorials/Correlation.ipynb) to support the movie examples

## :a-reading: StatsModels Examples and User Guide

The following StatsModels pages document its OLS model:

- [Formula User Guide](https://www.statsmodels.org/stable/example_formulas.html)
- [OLS Examples](https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html)
- [Linear Regression](https://www.statsmodels.org/stable/regression.html)

## :a-reading: Bootstrapping Linear Regression {: data-length="1950 words"}

Read [Bootstrapping for Linear Regression](https://www.textbook.ds100.org/ch/18/hyp_regression.html).

## :a-assignment: Assignment 4

[Assignment 4](../../assignments/A4/index.md) is due **October 25, 2020**.
