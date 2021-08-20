# Week 9 — Models & Prediction
{% import 'video.md' as media %}

!!! warning "Draft content"

    This content is still in draft state and has not yet been finalized.
    Do not depend on it as the final requirements for this week.

Activities:

[TOC]

This week's videos are also available in a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=0f0932a0-8a98-4ee2-bf8f-ac57000f5e14).

## :a-video: Introduction {: data-length="3m7s"}

This video introduces the week.

=== "Video"

    {{ media.video('6ec6be44-653a-44d0-8db3-ac57000b2560') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173276', 'AHsbW2hF0gaAAXM') }}

## :a-video: Simulation {: data-length="14m48s"}

This video talks more about simulation as a method for studying statistical techniques, which you are doing in the assignment.
I also describe more of NumPy's random number generation facilities.

=== "Video"

    {{ media.video('db2449d6-c0ec-454b-b813-ac57000b2514') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173277', 'AMmsQqYDB60pYbk') }}

!!! tip Random Seed

    You should set random seeds for all work that will need randomness, including train/test splits for evaluating predictors.

## :a-video: Variance, R², and the Sum of Squares {: data-length="5m59s"}

This video provides more detail on *explained variance* and what the $R^2$ means.

=== "Video"

    {{ media.video('ee53066a-f9c1-48fc-abc8-ac57000b2537') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173278', 'APvhgyfko-eH9MU') }}

### Resources

- [Penn State R² notes](https://online.stat.psu.edu/stat462/node/95/)
- [Penn State Sum of Squares Notes](https://online.stat.psu.edu/stat462/node/104/)
- [Proof of SSTO = SSR + SSE](https://web.njit.edu/~wguo/Math644_2012/Math644_Chapter%201_part4.pdf) (on Page 2)

## :a-video: Overfitting {: data-length="10m31s" }

This video introduces the idea of *overfitting*: learning too much from the training data so we can't predict the testing data.

=== "Video"

    {{ media.video('026f0abb-b736-4238-8e38-ac57000b2588') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173279', 'ABqv_ZE_MmpDcLk') }}

## :a-notebook: Overfitting Simulation

- [Overfitting Simulation notebook](./OverfittingSimulation.ipynb)

## :a-reading: Overfitting Example {: data-length="1180 words"}

Read [Example of overfitting and underfitting in machine learning](https://keeeto.github.io/blog/bias_variance/).

## :a-quiz: Week 9 Quiz

Take the Week 9 quiz in Blackboard (will be up by end of Saturday).

## :a-video: Replication, Bias, and Variance {: data-length="9m16s"}

=== "Video"

    {{ media.video('9762d0fb-57b9-4880-9d97-ac580037f27d') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173280', 'ANKJOxuY0wR0nIQ') }}

## :a-reading: Bias-Variance Tradeoff {: data-length="3000 words"}

Read [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html).

### Resources

Further reading: [Lecture 12: Bias-Variance Tradeoff](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote12.html).

## :a-video: Optimizing Loss {: data-length="14m3s"}

=== "Video"

    {{ media.video('e68b9f9d-13a6-4d98-8a4d-ac580037f259') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173288', 'AKxIYJP7LW4ct2Y') }}


## :a-notebook: Loss-Based Regression Notebook

Read the [minimization regression notebook](./BadRegression.ipynb) notebook.

## :a-task: Practice

There are several ways you can practice the material so far:

- Practice more regressions with World Bank data
- Measure World Bank data predictive accuracy with train-test evaluation and mean squared error

## :a-assignment: Assignment 4

Assignment 4 is due **October 25, 2020**.
