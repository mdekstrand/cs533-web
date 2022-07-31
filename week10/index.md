# Week 10 — Classification ({date}`wk10 range`)

:::{updated} F21
:::

## {{moverview}} Content Overview

:::{module} week10
:::

## {{mvideo}} What is Classification?

In this video, I introduce the week and what classification is.

:::{video}
:length: 6m39s
:name: 10-1 - What Is Classification
:::

## {{mvideo}} Log-Odds and Logistics

In this video, I introduce {term}`log odds`, along with the *{term}`logistic function`* and its inverse, 
the *{term}`logit function`*.
Log odds are a useful concept in many situations!

:::{video} logistic
:name: 10-2 - Log-Odds and Logistics
:length: 10m4s
:::

## {{mvideo}} Logistic Regression

We're now ready for our first classification model: *logistic regression*.

:::{video}
:name: 10-3 - Logistic Regression
:length: 9m7s
:::

## {{mvideo}} The Confusion Matrix

The *confusion matrix* describes the outcomes of a classification model and is the basis for computing effectiveness metrics.

:::{video} confusion
:name: 10-4 - The Confusion Matrix
:length: 11m48s
:::

### Resources

- The [Wikipedia article](https://en.wikipedia.org/wiki/Confusion_matrix) has a very good diagram of the confusion matrix and its derived metrics.

## {{mnotebook}} Logistic Regression Demo

The [demo notebook](../resources/tutorials/LogitRegressionDemo.ipynb) for our initial logistic regression videos.

## {{mvideo}} Baseline Models

:::{video} baselines
:name: 10-5 - Baselines
:length: 9m44s
:::

## {{mdoc}} Floating Point

- [Floating Point Guide](https://floating-point-gui.de/)

This is provided for reference.

## {{mdoc}} StatsModels Documentation

The following StatsModels page documents its logistic regression:

- [Regression with Discrete Dependent Variable](https://www.statsmodels.org/stable/discretemod.html)

This is **not** an assigned reading - it is here for your reference.

## {{mvideo}} Log Likelihood

This video describes the *log likelihood* that is the objective function used by logistic regression.

:::{video}
:length: 16m54s
:name: 10-6 - Log Likelihood
:::

## {{mvideo}} Scikit-Learn

This video introduces SciKit-Learn, and using it for a logistic regression.

:::{video}
:length: 6m42s
:name: 10-7 - Scikit-Learn
:::

## {{mnotebook}} SciKit-Learn Logistic Regression

The [SciKit Logistic](../resources/tutorials/SciKitLogistic.ipynb) notebook demonstrates training and using
{py:class}`sklearn.linear_model.LogisticRegression`.

## {{mvideo}} Receiver Operating Characteristic

This video introduces the *receiver operating characteristic* (ROC) curve, and its use in evaluating classifiers and selecting tradeoffs.

:::{video}
:length: 7m25s
:name: 10-8 - Receiver Operating Characteristic
:::

## {{mtask}} Practice

Load the Penguin data, and use a logistic regression to try to classify a penguin as Gentoo or Chinstrap using various measurements.
Delete the Adelie penguins first, so you have a binary classification problem.

## {{mvideo}} Biases and Assumptions

This video revisits sources of bias and discusses the assumptions underlying prediction.

:::{video}
:length: 22m
:name: 10-9 - Biases and Assumptions
:::

## {{mdoc}} Prediction-Based Decisions

:::{reading} pdb
:title: Prediction-Based Decisions and Fairness
:url: https://arxiv.org/abs/1811.07867
:length: 3650 words
:::

Read Sections 1 and 2 of the following paper:

> Shira Mitchell, Eric Potash, Solon Barocas, Alexander D'Amour, Kristian Lum. 2018.
> [Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions](https://arxiv.org/abs/1811.07867).
> arXiv:1811.07867 [stat.AP].

We'll come back to ideas here, but sections 1 and 2 describe the assumptions underlying most classification problems.
While the overall topic of the paper is fairness in making these decisions, I am not assigning it because it is a fairness paper;
rather, those first two sections provide a succinct description of the assumptions that we make when we undertake most
classification problems.  They apply no matter what properties of a classification problem or model we care about.

If you would like to learn more, I recommend:

- [Big Data's Disparate Impact](http://papers.ssrn.com/abstract=2477899)
- [Social Data](http://dx.doi.org/10.3389/fdata.2019.00013)

## {{mquiz}} Week 10 Quiz

The Week 10 quiz will be posted to {{LMS}}.

## {{mdoc}} Abolish the #TechToPrison Pipeline

:::{reading} tech-to-prison
:length: 2000 words
:url: https://medium.com/@CoalitionForCriticalTechnology/abolish-the-techtoprisonpipeline-9b5b14366b16
:title: "Abolish the #TechToPrison Pipeline"
:::

Read [Abolish the #TechToPrison Pipeline](https://medium.com/@CoalitionForCriticalTechnology/abolish-the-techtoprisonpipeline-9b5b14366b16) (the Medium reading time estimate includes the thorough — and valuable — footnotes and list of 2435 signatories).
This article probes in more detail the assumptions underlying classes of criminal justice data science applications.

## {{massignment}} Assignment 5

[Assignment 5](../../assignments/A5/index.md) is due **{date}`wk11 sun long`**.
