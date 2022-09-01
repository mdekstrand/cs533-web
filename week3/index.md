# Week 3 — Presentation ({date}`wk3 range`)

:::{updated} F22
:::

These are the learning outcomes for this week:

* Create plots for data
* Identify the appropriate type of plot for data in question
* Read and interpret a plot
* Refine a plot to more clearly show data
* Write a well-organized notebook to present data analysis with text and visuals

We will primarily be using [Seaborn][] and [Matplotlib][] for our graphics, because it is easy to
get them fully working for both notebook and document-ready graphics in any Anaconda environment and
efficiently handles very large data sets. There are several other packages that are useful for
Python data visualization, and in some cases are easier to use. I personally use [plotnine][] for
most of my graphics, and [plotly][] is a very capable package with particularly strong support for
interactive graphics. The core graphics principles we study in this module will apply to most
packages you may use in the future.

:::{tip}
I do **not** recommend that you use Plotly for this course.  While it is very good for interactive graphics,
its support for static graphics to render in printable documents is rather new.
:::

:::{admonition} Seaborn upgrades
:class: note

Seaborn is undergoing some changes in its syntax.  In the old syntax, we pass the `x` and `y`
parameters as positional paremeters to a plotting function:

```
sns.lineplot('time', 'price', data=stocks)
```

In the new syntax, which will be required in a future Seaborn release, we use named parameters
for everything:

```
sns.lineplot(data=stocks, x='time', y='price')
```

All new material going forward will use the new syntax, but it takes time to update all of the
slides and videos.  You may see the old syntax.  It still works, but it issues a warning to let
you know the future syntax is changing.
:::

[Seaborn]: https://seaborn.pydata.org/
[Matplotlib]: https://matplotlib.org/
[plotnine]: https://plotnine.readthedocs.io/en/stable/
[plotly]: https://plotly.com/python/plotly-fundamentals/

## {{moverview}} Content Overview

:::{module} week3
:folder: 72054bfc-c064-4b87-aa01-ad960182a9e7
:::

## {{mcal}} Deadlines

- [Finding a plot](#plots-in-the-wild) before class on Thursday
- Week 3 quiz at **8am on Thursday**
- [Assignment 1](../assigments/A1/index.md) at **midnight on Sunday**

## {{mvideo}} Presentation Goals and Audiences

:::{video}
:id: cb6d0907-59fa-4a15-96b9-ad9601830ba0
:slide-id: 495979F9A431DDB0%2173737
:slide-auth: ALZ3EwW8-lyv3jE
:length: 9m55s
:name: 3-1 - Goals and Audiences
:::

## {{mnotebook}} Data and Notebook

These resources are used throughout many of the videos in this class:

- [Movie Scores notebook](../resources/tutorials/CriticScores.ipynb)
- The [HETREC data](https://grouplens.org/datasets/hetrec-2011/)

## {{mdoc}} Statistical Data Presentation

:::{reading}
:title: Statistical Data Presentation
:url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5453888/
:length: 4300 words
:::

Read [Statistical Data Presentation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5453888/) by Junyong In and Sangseok Lee.

## {{mvideo}} Introducing Statistical Graphics

This video introduces basic principles of statistical graphics.

:::{video}
:id: f87fc754-ecbd-4970-ad3b-ad9601830c4f
:slide-id: 495979F9A431DDB0%2173740
:slide-auth: AJRz3rErjz_tmt8
:length: 14m15s
:name: 3-2 - Statistical Graphics
:::

## {{mvideo}} Manipulating Data

This video goes over the core Pandas data selection and manipulation operations.
It is primarily a tour guide — the technical content is in following notebooks.

:::{video}
:id: 7ee3707b-0e2d-4a18-8de1-ad9601830ce7
:slide-id: 495979F9A431DDB0%2173739
:slide-auth: ABw3xd9psf1k5Y8
:length: 9m18s
:name: 3-3 - Manipulating Data
:::

## {{mnotebook}} Selecting Data

:::{reading}
:title: Selecting Data
:url: ../resources/tutorials/Selection.html
:length: 1866 words
:::

Read the [{{mnotebook}} Selecting Data] tutorial notebook to learn how to select data from a data frame.

I encourage you to read relevant tutorial notebooks throughout the semester, and link to them when
appropriate; I am making three ones this week specifically assigned readings.


## {{mnotebook}} Reshaping Data

:::{reading}
:title: Reshaping Data
:url: ../resources/tutorials/Reshaping.html
:length: 2363 words
:::

Read the [{{mnotebook}} Reshaping Data](../resources/tutorialsReshaping.ipynb) tutorial notebook to learn
how to manipulate the shape of data frames in various ways, including merging two data frames into one.

## {{mnotebook}} Missing Data

:::{reading}
:title: Missing Data
:url: ../resources/tutorials/MissingData.html
:length: 3850 words
:::

Read the [{{mnotebook}} Missing Data](../resources/tutorials/MissingData.ipynb) tutorial notebook.

## {{mvideo}} Types of Charts

In this video, I discuss several common types of charts for statistical graphics, and how to choose an appropriate one.
It complements the “Statistical Data Presentation” reading.

:::{video}
:id: 9077db8e-b57d-4825-a472-ad9601830d80
:slide-id: 495979F9A431DDB0%2173738
:slide-auth: AGlTa7w8X6LcIkM
:length: 13m30s
:name: 3-4 - Types of Charts
:::

### Resources

- [Notebook](../resources/tutorials/Charting.ipynb)
- [Seaborn gallery](https://seaborn.pydata.org/examples/index.html)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html) — organized topically, **very good resource**
- [Matplotlib gallery](https://matplotlib.org/gallery.html)
- [Plotnine gallery](https://plotnine.readthedocs.io/en/stable/gallery.html)

## {{mvideo}} Metrics and Differences

We talked about the notion of “relative” differences, but what are they?

:::{video}
:id: 457472b2-1bb3-455b-9dd4-ad9601830e8b
:slide-id: 495979F9A431DDB0%2173741
:slide-auth: AHCb6UrENZqsRi0
:length: 6m50s
:name: 3-5 - Metrics and Differences
:::

## {{mvideo}} Charts from the Ground Up

In this video, I discuss how to design a chart from your questions, goals, and data.

:::{video} charts-ground-up
:id: bb921f27-23a5-4103-afff-ad970182fbb2
:slide-id: 495979F9A431DDB0%2173742
:slide-auth: ANGH7yWhHchpLB4
:length: 22m14s
:name: 3-6 - Charts from the Ground Up
:::

### Resources

- [Supporting notebook](3-6-ChartsFromTheGroundUp.ipynb) — code for most of the charts (using Seaborn)
- [Book data statistics notebook](https://nbviewer.jupyter.org/github/BoiseState/bookdata-tools/blob/master/LinkageStats.ipynb) — code for the stacked bar charts (using raw Matplotlib)
- My book experiments have many facet examples — see [DataSummary](https://nbviewer.jupyter.org/github/BoiseState/book-author-gender/blob/master/DataSummary.ipynb) and [ProfileDataPrep](https://nbviewer.jupyter.org/github/BoiseState/book-author-gender/blob/master/ProfileDataPrep.ipynb).

## {{mtask}} Plots in the Wild

In preparation for Thursday's class, find a data presentation (plot, table, etc.) in a recent online
publication, and share it with your team through a post on Piazza (in the 'discuss' category) with a
link, a copy of the image. This can be from a journal paper, a newspaper article, a blog post, or
another source the class can all access.

In class we will discuss these plots!

:::{tip}
Don't spend more than 30 minutes on this assignment.
:::

## {{mnotebook}} Finishing Touches

The [Finishing Touches](../resources/tutorials/ChartFinishingTouches.ipynb) notebook describes how to apply some finishing touches to your plots and save them to files.

## {{mvideo}} Organizing and Formatting Notebooks

How should you organize your notebook?
What makes a good notebook?
In this video we talk about that!

:::{video} notebooks
:id: 80e425d4-f295-4f1b-b73a-ad9601830f06
:slide-id: 495979F9A431DDB0%2173736
:slide-auth: APudMYTIAHl2Ao8
:length: 16m50s
:name: 3-7 - Organizing Notebooks
:::

### Resources

- [GitHub Markdown guide](https://guides.github.com/features/mastering-markdown/) — most of this syntax works in Jupyter as well
- [Jupyter's Markdown docs](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)

## {{mdoc}} Notebook Formatting Checklist

The [notebook checklist](../resources/notebook-checklist.md) will help you make sure your notebooks are well-organized.

## {{mquiz}} Week 3 Quiz

The Week 3 quiz will be over all of the assigned material for this week, and is in {{LMS}}.

The sections below this are for your further study and practice.

## {{mbook}} Textbook

This week primarily uses Chapter 9 of {book}`p4da`, with some material from chapters 8 and 10.

## 📚 Futher Reading

For further study on these topics, see:

* The Seaborn and Matplotlib galleries
* <cite>The Visual Display of Quantitative Information</cite> by Edward R. Tufte
* <cite>W. E. B. Du Bois's Data Portraits: Visualizing Black America</cite>, edited by Whitney Battle-Baptiste and Britt Rusert

## {{mtask}} Practice

Doing this work well takes a lot of practice.  Create some notebooks and experiment with drawing interesting charts from some of the data sets we have been exploring, or new data you find!
The HETREC data has a number of variables of different types that are useful for practicing manipulations and visualizations.

## {{massignment}} Assignment 1

Assignment 1 is due on **Sunday, Sep. 12** at the end of the day (11:59 pm).

The [tutorial notebooks](../resources/tutorials/index.md) are going to be very useful for this assignment.
