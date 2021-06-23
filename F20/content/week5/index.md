# Week 5 — Filling In
{% import 'video.md' as media %}

This week is primarily for **practice** and **solidifying concepts**.
I'm also going to take a step back and give some more context to some of the things we're talking about.

[TOC]

This week's videos are also in a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=c8e7bd6c-cb7b-43b4-ac97-ac3c0051c38e).

## :material-clipboard-list: Week 5 Quiz

The Week 5 quiz is about material **through the end of Week 4**.
Nothing from this week will be on it, except that things here may clarify some of last week's material for you.

## :material-notebook: Assignment 1 Solution

I will post the Assignment 1 solution to Piazza (sorry, I'm not posting it to the entire Internet).

## :material-file-document: Glossary Updates

I have extensively updated the [course glossary](../../resources/glossary.md).
Please post on Piazza if you have suggested additions!

## :material-notebook: Writing Functions

I've used Python *functions* in a few of my example notebooks.
[The function notebook](../../resources/tutorials/Functions.ipynb) talks more about them, how to write them, and how to use them.

## :material-video: Comparing Distributions {: #qqplot data-length="5m6s"}

This video describes how to use Q-Q plots to compare data against a distribution.

=== "Video"

    {{ media.video('7ea91346-6e57-48d2-86fc-ac3c0041be0a') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173197', 'ANF7mADxGho6ZDs') }}

### Resources

- [NIST Handbook on quantile-quantile plots](https://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm)

## :material-video: T-tests {: #ttest data-length="12m24s"}

This video discusses the *t*-test in more detail, and the different kinds of *t*-tests that we can run.
It also introduces **degrees of freedom**.

=== "Video"

    {{ media.video('49c92951-3a9a-4534-ae1a-ac3c0041be38') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173195', 'APaucCdchKCkwZk') }}

## :material-video: Python Errors {: #debug data-length="7m28s"}

This video discusses common Python errors and how to read errors.

=== "Video"

    {{ media.video('e6dd1cb3-4659-4d91-ae16-ac3c0041bda5') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173199', 'AKtFQ6RgMhVAQk4') }}

## :material-video: Python Libraries {: data-length="3m43s"}

=== "Video"

    {{ media.video('9dc67550-0754-42e7-95eb-ac3c0041bddb') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173202', 'AGJDocG2Hv-tifk') }}

### Resources

- [NIST Handbook on quantitative meaures](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm) (has info on 1-sample and 2-sample *t*-tests)

## :material-notebook: One Sample Notebook

The [One Sample notebook](../../resources/tutorials/OneSample.ipynb) demonstrates how to compute a one-sample *t*-test, and draw a Q-Q plot to compare a distribution with normal.

## :material-video: Epistemology {: data-length="25m44s"}

In this video, I talk about how the quantitative data science methods we are learning fit into a broader picture of source of knowledge.

=== "Video"

    {{ media.video('8477f2e8-ed2e-4c23-a489-ac3c0041d182') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172947', 'AJXLT9KELkhPfOQ') }}

## :material-video: Learning More {: data-length="5m10s"}

=== "Video"

    {{ media.video('1e85c17a-bd99-4cd5-861a-ac3c00438ee2') }}

## :fontawesome-solid-tasks: Practice

There are a few things you can do to keep practing the material:

-   The [HETREC data](https://grouplens.org/datasets/hetrec-2011/) contains two data sets besides the movie data: Delicious bookmarks and Last.FM listening records.
    Download this data set and apply some of our exploratory techniques to it.
-   Download the SBA data from Week 4's activity and describe the distributions of more of the variables.
-   Apply the inference techniques from Week 4 to statistically test the differences you observed in [Assignment 1](../../assignments/A1/index.md).

## :material-notebook: More Examples

Some more examples from my own work (these are *not* all cleaned up to our checklist standards):

- [Data summary from book gender paper](DataSummary.ipynb) - shows a number of descriptive things, including a stacked area chart.
- [Linkage statistics from book data](https://github.com/BoiseState/bookdata-tools/blob/master/LinkageStats.ipynb) - shows some matploblib things, and computing data linking statistics.

## :material-notebook: Tutorials

The [indexing notebook](../../resources/tutorials/Indexing.ipynb) is now up!

## :material-inbox: Assignment 2

[Assignment 2](../../assignments/A2/index.md) is due on **September 27**.
