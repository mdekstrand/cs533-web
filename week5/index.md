# 🚧 Week 5 — Filling In (9/20–24) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
:::

This week introduces one new statistical concept — the {term}`hypothesis test` — and is otherwise about **practice** and **solidifying concepts**.
I'm also going to take a step back and give some more context to some of the things we're talking about.

Our learning outcomes are:

- Compute and interpret hypothesis test
- Avoid {term}`p-hacking` and {term}`HARKing`
- Understand how to read and interpret Python errors
- Understand how the quantitative techniques we are learning in this class fit in a broader landscape of epistemologies

## {{moverview}} Content Overview

:::{module} week5
:::

## {{mcal}} Deadlines

- Week 5 Quiz is due on **Thursday** at 8AM.
- [Assignment 2](../assignments/A2/index.md) is due on **Sunday, Sep. 26** at 11:59 PM.
- Midterm A is next week, on **Tuesday, Sep. 28**.

## {{mnotebook}} Assignment 1 Solution

I will post the Assignment 1 solution to Canvas (sorry, I'm not posting it to the entire Internet).

## {{mdoc}} Course Glossary

If you haven't yet, I highly recommend consulting the [course glossary](../../resources/glossary.md).
Please post on Piazza if you have suggested additions!

The midterm is also likely to be useful in studying for the exam.

## {{mnotebook}} Writing Functions

I've used Python *functions* in a few of my example notebooks.
[The function notebook](../../resources/tutorials/Functions.ipynb) talks more about them, how to write them, and how to use them.

## {{mvideo}} Comparing Distributions

This video describes how to use Q-Q plots to compare data against a distribution.

:::{video}
:id: 7ea91346-6e57-48d2-86fc-ac3c0041be0a
:length: 5m6s
:slide-id: 495979F9A431DDB0%2173197
:slide-auth: ANF7mADxGho6ZDs
:name: 5-1 - Comparing distributions
:::

### Resources

- [NIST Handbook on quantile-quantile plots](https://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm)

## {{mvideo}} Testing Hypotheses

:::{video} hypotest
:id: b8f249ac-9101-4336-89e8-ac3600436c5a
:length: 14m51s
:slide-id: 495979F9A431DDB0%2173033
:slide-auth: fAPweDd4ZnAHFL6E
:name: 5-2 - Testing Hypotheses
:::

### Resources

- [Statistical test selection flowchart](http://timdraws.net/files/StatisticalTestFinder.pdf)

(p-hacking-cartoon)=
## 💥 Cartoon

Read [XKCD #882: Significant](https://xkcd.com/882/).

This is called **_p_-hacking**: running tests until we find one that is significant.

## {{mvideo}} T-tests

This video discusses the *t*-test in more detail, and the different kinds of *t*-tests that we can run.
It also introduces {term}`degrees of freedom`.

:::{video} t-test
:id: 49c92951-3a9a-4534-ae1a-ac3c0041be38
:length: 12m24s
:slide-id: 495979F9A431DDB0%2173195
:slide-auth: APaucCdchKCkwZk
:name: 5-3 - T-tests
:::

## {{mquiz}} Week 5 Quiz

The Week 5 quiz is about material **through this point**.
The subsequent videos are to help you better understand and contextualize material.

## {{mnotebook}} One Sample Notebook

The [One Sample notebook](../../resources/tutorials/OneSample.ipynb) demonstrates how to compute a one-sample *t*-test, and draw a Q-Q plot to compare a distribution with normal.

### Resources

- [NIST Handbook on quantitative meaures](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm) (has info on 1-sample and 2-sample *t*-tests)

## {{mvideo}} Python Errors

This video discusses common Python errors and how to read errors.

:::{video}
:id: e6dd1cb3-4659-4d91-ae16-ac3c0041bda5
:length: 7m28s
:slide-id: 495979F9A431DDB0%2173199
:slide-auth: AKtFQ6RgMhVAQk4
:name: 5-4 - Python Errors
:::

## {{mvideo}} Python Libraries

:::{video}
:id: 9dc67550-0754-42e7-95eb-ac3c0041bddb
:length: 3m43s
:slide-id: 495979F9A431DDB0%2173202
:slide-auth: AGJDocG2Hv-tifk
:name: 5-5 - Python Libraries
:::

## {{mvideo}} Epistemology

In this video, I talk about how the quantitative data science methods we are learning fit into a broader picture of source of knowledge.

:::{video}
:id: 8477f2e8-ed2e-4c23-a489-ac3c0041d182
:length: 25m44s
:slide-id: 495979F9A431DDB0%2172947
:slide-auth: AJXLT9KELkhPfOQ
:name: 5-6 - Epistemology
:::

## {{mvideo}} Learning More

In this video I talk about how I go about expanding my own data science knowledge and techniques, with the goal
of giving you ideas for how you can continue learning beyond this class.

:::{video}
:id: 1e85c17a-bd99-4cd5-861a-ac3c00438ee2
:length: 5m10s
:name: 5-7 - Learning More
:::

## {{mtask}} Practice

There are a few things you can do to keep practicing the material:

-   The [HETREC data](https://grouplens.org/datasets/hetrec-2011/) contains two data sets besides the movie data: Delicious bookmarks and Last.FM listening records.
    Download this data set and apply some of our exploratory techniques to it.
-   Download the SBA data from Week 4's activity and describe the distributions of more of the variables.
-   Apply the inference techniques from Week 4 to statistically test the differences you observed in [Assignment 1](../../assignments/A1/index.md).

## {{mnotebook}} More Examples

Some more examples from my own work (these are *not* all cleaned up to our checklist standards):

- [Data summary from book gender paper](https://nbviewer.jupyter.org/github/BoiseState/book-author-gender/blob/master/DataSummary.ipynb) - shows a number of descriptive things, including a stacked area chart; it also uses Plotnine.
- [Linkage statistics from book data](https://github.com/BoiseState/bookdata-tools/blob/master/LinkageStats.ipynb) - shows some matploblib things, and computing data linking statistics.

## {{mnotebook}} Tutorials

The [tutorial notebooks](tutorials) include many useful things, and have a couple of additions moved over from {module}`week4`.

## {{massignment}} Assignment 2

[Assignment 2](../assignments/A2/index.md) is due on **September 26**.
