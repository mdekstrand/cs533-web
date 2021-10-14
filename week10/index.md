# 🚧 Week 10 — Classification (Oct. 25–29) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
:::

## {{moverview}} Content Overview

:::{module} week10
:::

## :a-video: What is Classification? {: data-length="6m39s"}

In this video, I introduce the week and what classification is.

:::{video}
:id: 5c480e36-8608-402c-a129-ac5d001ff796
:length: 6m39s
:slide-id: 495979F9A431DDB0%2173290
:slide-auth: AIrnE1IeJheWGMo
:::

## :a-video: Log-Odds and Logistics {: data-length="10m4s"}

In this video, I introduce log-odds, along with the *logistic function* and its inverse, *logit*.

:::{video}
:id: 5443ea85-5c44-4fda-9945-ac5d001ff832
:length: 10m4s
:slide-id: 495979F9A431DDB0%2173292
:slide-auth: ADvOZLcsA-Eof-M
:::

## :a-video: Logistic Regression {: data-length="9m7s"}

We're now ready for our first classification model: *logistic regression*.

:::{video}
:id: 4e40bba2-840d-4c81-a9a3-ac5d001ff7bf
:length: 9m7s
:slide-id: 495979F9A431DDB0%2173293
:slide-auth: AMtiFgrMB1GajNQ
:::

## :a-video: The Confusion Matrix {: data-length="11m50s"}

The *confusion matrix* describes the outcomes of a classification model and is the basis for computing effectiveness metrics.

:::{video}
:id: da6ee201-03c8-4d93-9abe-ac5d001ff7f8
:length: 11m50s
:slide-id: 495979F9A431DDB0%2173294
:slide-auth: AP40RfAwO30CwLE
:::

### Resources

- The [Wikipedia article](https://en.wikipedia.org/wiki/Confusion_matrix) has a very good diagram of the confusion matrix and its derived metrics.

## :a-notebook: Logistic Regression Demo

The [demo notebook](LogitRegressionDemo.ipynb) for the first-half videos.

## :a-quiz: Week 10 Quiz

The Week 10 quiz will be posted to Blackboard.

## :a-reading: Floating Point

- [Floating Point Guide](https://floating-point-gui.de/)

This is provided for reference.

## :a-reading: StatsModels Documentation

The following StatsModels page documents its logistic regression:

- [Regression with Discrete Dependent Variable](https://www.statsmodels.org/stable/discretemod.html)

This is **not** an assigned reading - it is here for your reference.

## :a-video: Log Likelihood {: data-length="16m54s"}

This video describes the *log likelihood* that is the objective function used by logistic regression.

:::{video}
:id: 1e548030-76ea-45e9-b543-ac5f0054f199
:length: 16m54s
:slide-id: 495979F9A431DDB0%2173298
:slide-auth: ADOpJqu9OvKINK4
:::

## :a-video: Scikit-Learn {: data-length="6m42s"}

This video introduces SciKit-Learn, and using it for a logistic regression.

:::{video}
:id: 029a7a8d-a7fe-4474-a551-ac5f0054f129
:length: 6m42s
:slide-id: 495979F9A431DDB0%2173300
:slide-auth: AHK68fjvLEWn8GY
:::

## :a-notebook: SciKit-Learn Logistic Regression

The [SciKit Logistic](./SciKitLogistic.ipynb) notebook demonstrates training and using a logistic regression classifier with SciKit-Learn.

## :a-video: Receiver Operating Characteristic {: data-length="7m25s"}

This video introduces the *receiver operating characteristic* (ROC) curve, and its use in evaluating classifiers and selecting tradeoffs.

:::{video}
:id: 0a3a7981-c4cf-47a9-9236-ac5f0054f174
:length: 7m25s
:slide-id: 495979F9A431DDB0%2173301
:slide-auth: ABkYIOGgIpko-K4
:::

## :a-task: Practice

Load the Penguin data, and use a logistic regression to try to classify a penguin as Gentoo or Chinstrap using various measurements.
Delete the Adelie penguins first, so you have a binary classification problem.

## :a-video: Biases and Assumptions {: data-length="22m"}

This video revisits sources of bias and discusses the assumptions underlying prediction.

:::{video}
:id: eb40dfed-7a3e-4c08-a7f8-ac5f005a7e34
:length: 22m
:slide-id: 495979F9A431DDB0%2173303
:slide-auth: AHZT9DGmNOxGZxM
:::

## :a-reading: Prediction-Based Decisions {: data-length="3650 words"}

:::{reading} pdb
:title: Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions
:url: https://arxiv.org/abs/1811.07867
:length: 3650 words
:::

Read Sections 1 and 2 of the following paper:

> Shira Mitchell, Eric Potash, Solon Barocas, Alexander D'Amour, Kristian Lum. 2018.
> [Prediction-Based Decisions and Fairness: A Catalogue of Choices, Assumptions, and Definitions](https://arxiv.org/abs/1811.07867).
> arXiv:1811.07867 [stat.AP].

We'll come back to ideas here, but sections 1 and 2 describe the assumptions underlying most classification problems.

If you would like to learn more, I recommend:

- [Big Data's Disparate Impact](http://papers.ssrn.com/abstract=2477899)
- [Social Data](http://dx.doi.org/10.3389/fdata.2019.00013)

## :a-reading: Abolish the #TechToPrison Pipeline {: data-length="2000 words"}

Read [Abolish the #TechToPrison Pipeline](https://medium.com/@CoalitionForCriticalTechnology/abolish-the-techtoprisonpipeline-9b5b14366b16) (the Medium reading time estimate includes the thorough — and valuable — footnotes and list of 2435 signatories).
This article probes in more detail the assumptions underlying classes of criminal justice data science applications.

## :a-assignment: Assignment 5

[Assignment 5](../../assignments/A5/index.md) is due **November 7, 2020**.
