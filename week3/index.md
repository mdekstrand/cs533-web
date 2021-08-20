# Week 3 — Presentation

:::{draft}
This content is still in draft state and has not yet been finalized.
Do not depend on it as the final requirements for this week.
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

[Seaborn]: https://seaborn.pydata.org/
[Matplotlib]: https://matplotlib.org/
[plotnine]: https://plotnine.readthedocs.io/en/stable/
[plotly]: https://plotly.com/python/plotly-fundamentals/

## {{moverview}} Content Overview

:::{module} week3
:::

## {{mcal}} Deadlines

- Week 3 quiz at **8am on Thursday**
- [Assignment 1](../assigments/A1/index.md) at **midnight on Sunday**

## {{mvideo}} Presentation Goals and Audiences

:::{video}
:id: dc85b8a5-7e18-41f2-9b26-ac2a0188d445
:slide-id:
:slide-auth:
:length: 9m55s
:name: 3-1 - Goals and Audiences
:::

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
:id: c598b6dd-ed79-4546-9973-ac2b000e42a7
:slide-id:
:slide-auth:
:length: 14m15s
:name: 3-2 - Statistical Graphics
:::

## {{mvideo}} Manipulating Data

This video goes over the core Pandas data selection and manipulation operations.
Arguably it should have been last week, but we'll do it this week!

The video is primarily a tour guide — the technical content is in the notebooks.

:::{video}
:id: d11f8f0d-491e-4d6f-b705-ac2b0029c35c
:slide-id:
:slide-auth:
:length: 9m18s
:name: 3-3 - Manipulating Data
:::

### Resources

- [Selection Notebook](../../resources/tutorials/Selection.ipynb)
- [Reshaping Notebook](../../resources/tutorials/Reshaping.ipynb)

## {{mvideo}} Types of Charts

In this video, I discuss several common types of charts for statistical graphics, and how to choose an appropriate one.
It complements the “Statistical Data Presentation” reading.

:::{video}
:id: 902b507a-1683-4335-9be5-ac2b002d7995
:slide-id:
:slide-auth:
:length: 13m30s
:name: 3-4 - Types of Charts
:::

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172994', 'ABJfm2NS_eYRmjc')}}

### Resources

- [Notebook](../../resources/tutorials/Charting.ipynb)
- [Seaborn gallery](/seaborn/examples/index.html)
- [Seaborn tutorial](/seaborn/tutorial.html) — organized topically, **very good resource**
- [Matplotlib gallery](https://matplotlib.org/gallery.html)
- [Plotnine gallery](https://plotnine.readthedocs.io/en/stable/gallery.html)

## {{mvideo}} Metrics and Differences

We talked about the notion of “relative” differences, but what are they?

:::{video}
:id: 37e62ec4-1718-43a9-bf82-ac2e00263855
:slide-id:
:slide-auth:
:length: 6m50s
:name: 3-5 - Metrics and Differences
:::

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173004', 'ALSTQJtKdMDNs1Y') }}


## {{mvideo}} Charts from the Ground Up

In this video, I discuss how to design a chart from your questions, goals, and data.

:::{video}
:id: af1afc4c-0dee-4c1c-af34-ac2e00263882
:slide-id:
:slide-auth:
:length: 24m54s
:name: 3-6 - Charts from the Ground Up
:::

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172995', 'AEjOrH8X_6gmPOk') }}

### Resources

- [Supporting notebook](3-6 - Charts from the Ground Up.ipynb)

## {{mtask}} Plots in the Wild

Find a data presentation (plot, table, etc.) in a recent online publication, and create a post on Piazza (in the 'discuss' category) with a link, a copy of the image, and 3 observations about things it does well and/or needs to correct or improve.
This can be from a journal paper, a newspaper article, a blog post, or another source the class can all access.

Don't spend more than 30 minutes on this assignment.

## {{mnotebook}} Finishing Touches

The [Finishing Touches](../../resources/tutorials/ChartFinishingTouches.ipynb) notebook describes how to apply some finishing touches to your plots and save them to files.

## {{mvideo}} Organizing and Formatting Notebooks

How should you organize your notebook?
What makes a good notebook?
In this video we talk about that!

:::{video}
:id: 1bcb5b41-d2ca-4bbd-8c28-ac2e002638b6
:slide-id:
:slide-auth:
:length: 16m50s
:name: 3-7 - Organizing Notebooks
:::

### Resources

- [GitHub Markdown guide](https://guides.github.com/features/mastering-markdown/) — most of this syntax works in Jupyter as well
- [Jupyter's Markdown docs](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)

## {{mdoc}} Notebook Formatting Checklist

The [notebook checklist](../../resources/notebook-checklist.md) will help you make sure your notebooks are well-organized.

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
