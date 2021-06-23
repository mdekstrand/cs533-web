# Week 11 — Evaluation
{% import 'video.md' as media %}

Activities:

[TOC]

There is **no quiz** this week.

This week's videos are also available as a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=94fc0cc9-53df-43b5-b46d-ac66003dd5e1).

## :a-video: Intro & Context {: #intro data-length="4m39s"}

In this video, I review where we are at conceptually, and recap the ideas of estimating conditional probability and expectation.

=== "Video"

    {{ media.video('40a41051-8c07-443c-b7d1-ac66002b3208') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173320', 'AJXlvBsutNDBkoE') }}

## :a-video: Feature Transforms {: data-length="21m03s"}

What are some useful techniques for engineering features in an application?

=== "Video"

    {{ media.video('80203946-b811-4ecb-b703-ac660033edd1') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173322', 'ABC9rmLnxkHsstY') }}

## :a-video: Workflow {: data-length="14m29s"}

How do you do feature engineering and model selection in a machine learning workflow?
What is the iterative process involved?

=== "Video"

    {{ media.video('71b1aa35-8435-4eae-ae32-ac660033ee09') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173324', 'AGk8GhY4fx1Mnm8') }}

## :a-video: SciKit Pipelines {: data-length="7m19s"}

In this video, I introduce SciKit *pipelines* that put multiple transformations together.

=== "Video"

    {{ media.video('f448da70-c2d2-4c1b-942b-ac66003656a1') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173328', 'ACahS4jRCAE3ueU') }}

## :a-reading: SciKit Learn Pipelines

Read the [SciKit-Learn User Guide chapter on pipelines](https://scikit-learn.org/stable/modules/compose.html).

## :a-reading: SciKit Learn Preprocessing

Read the [SciKit-Learn User Guide chapter on pre-processing](https://scikit-learn.org/stable/modules/preprocessing.html).

## :a-video: Regularization {: data-length="15m4s"}

This video introduces regularization: ridge regression, lasso regression, and the elasticnet.
Lasso regression can help with (semi-)automatic feature selection.

=== "Video"

    {{ media.video('fa457314-7344-48cd-af1f-ac660039cbc4') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173326', 'APzIM2g9IcVX0XQ') }}

## :a-notebook: Pipeline and Regularization

[This notebook](../../resources/tutorials/SciKitPipeline.ipynb) demonstrates pipelines and $L_2$ regression, and performs a significance test of classifier improvement.

It also shows a training of a decision tree (next video).

## :a-video: Models and Depth {: data-length="7m23s"}

What does the world look like beyond logistic regression?
Can a model output be a feature?

=== "Video"

    {{ media.video('220a8acb-a901-49e7-bf9e-ac66003d7033') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173330', 'APtXIrllUsY0_vY') }}

## :a-video: Inference and Ablation {: #ablation data-length="14m55s"}

How do we understand, *robustly*, the performance of our system?
What contributes to its performance?

=== "Video"

    {{ media.video('589628b2-30ce-4c38-ba45-ac66003f5163') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173331', '%21AAlNEpWRX05DM90') }}

## :a-reading: Statistical Significance Tests {: data-length="3400 words"}

Read [Statistical Significance Tests for Comparing Machine Learning Algorithms](https://machinelearningmastery.com/statistical-significance-tests-for-comparing-machine-learning-algorithms/).

For further reading, you can also see [Approximate Statistical Tests](http://dx.doi.org/10.1162/089976698300017197).

## :a-video: Dates {: data-length="8m34s"}

This video discusses how to use work with dates in Pandas.

=== "Video"

    {{ media.video('db1dc799-8ed1-4a7b-960e-ac69001a590d') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173338', 'ALt4_zuupKaPObs') }}

### Links

- [Date operations notebook](./Dates.ipynb)
- [Pandas time series / date functionality](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- [Pandas time deltas](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html)
- [DateOffset](https://pandas.pydata.org/pandas-docs/stable/reference/offset_frequency.html)
- [Format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

## :a-assignment: Assignment 5

[Assignment 5](../../assignments/A5/index.md) is due **November 11, 2020**.
