# Week 5 — Filling In (9/20–24)

This week introduces one new statistical concept — the {term}`hypothesis test` — and is otherwise about **practice** and **solidifying concepts**.
I'm also going to take a step back and give some more context to some of the things we're talking about.

Our learning outcomes are:

- Compute and interpret hypothesis test
- Avoid {term}`p-hacking` and {term}`HARKing`
- Understand how to read and interpret Python errors
- Understand how the quantitative techniques we are learning in this class fit in a broader landscape of epistemologies

## {{moverview}} Content Overview

:::{module} week5
:folder: 2ecc3b3f-df3b-437c-a5d0-ad9c018388de
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
:length: 5m6s
:name: 5-1 - Comparing Distributions
:::

### Resources

- [NIST Handbook on quantile-quantile plots](https://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm)

## {{mvideo}} Testing Hypotheses

:::{video} hypotest
:length: 14m51s
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
:length: 12m24s
:name: 5-3 - T-tests
:::

## {{mvideo}} Epistemology

In this video, I talk about how the quantitative data science methods we are learning fit into a broader picture of source of knowledge.

:::{video}
:length: 25m44s
:name: 5-4 - Epistemology
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
:length: 7m28s
:name: 5-5 - Python Errors
:::

## {{mvideo}} Python Libraries

:::{video}
:length: 3m43s
:name: 5-6 - Python Libraries
:::

## {{mvideo}} Learning More

In this video I talk about how I go about expanding my own data science knowledge and techniques, with the goal
of giving you ideas for how you can continue learning beyond this class.

:::{video}
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
