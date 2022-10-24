# Week 1 — Questions ({date}`wk1 range`)

:::{updated} F22
:::

The key learning outcomes for this week are:

- Ask and refine questions that can be answered with data
- Install and run the software required for the course
- Write and run basic Python code in a Jupyter notebook
- Begin to think about the complexity of meaningful questions

This week draws from chapters 1–4 from {book}`p4da` and chapters 1-2 of {book}`tlds`.
If you already know Python, the Python parts should mostly be review.

## {{moverview}} Content Overview

:::{module} week1
:folder: 953b341a-9d2d-4c4b-bbf3-aef6015e22df
:::

## {{mcal}} Deadlines

This week has the following deadlines:

- [Pre-class inventory](#pre-class-inventory) at **noon on Wednesday**
- [Week 1 quiz](#week-1-quiz) at **8am on Thursday**
- [Assignment 0](#assignment-0) at **11:59 pm on Sunday**

## {{mvideo}} Introduction

This video introduces the course and our learning outcomes for the term.

:::{video} introduction
:length: 11m11s
:name: 1-1 - Introduction
:::

## {{mvideo}} Asking Questions

In this video, I introduce *questions* in their broader context of using data to advance goals. 
I also introduce the idea of **operationalization**, which will be a key concept throughout the class.

:::{video} asking-questions
:length: 10m35s
:name: 1-2 - Asking Questions
:::

### Further Reading

* [How to Ask the Right Questions](https://towardsdatascience.com/how-to-ask-the-right-questions-as-a-data-scientist-913621907411)

## {{mvideo}} Questioning Questions

We make our {term}`operationalizations <Operationalization>` better by questioning them.  What do they capture?  Who or what do they prioritize?

:::{video} questioning-questions
:length: 8m54s
:name: 1-3 - Questioning Questions
:::

:::{note}
In this video, I talk about asking what it takes to *improve* a metric.  It would be more
precise to ask what would *change* a metric; whether increasing or decreasing a metric is
an improvement depends on the metric and application context.  The metric itself does not
improve or get worse without that context.

When I re-record this video for a future revision, I'll change my language.
:::

## {{mbook}} Textbook Chapters - Questions

The first videos of this class go with chapters 1 and 2 of {book}`tlds`.

## {{mclass}} Tuesday Class

On Tuesday, we will meet on Zoom and do the following:

- Introduce the class
- Start working on defining and clarifying questions
- Set expectations for the week and semester

## {{mtask}} Pre-Class Inventory

Fill out the [pre-class skill inventory and survey](https://forms.gle/gUXW7V59rA4thqR87) by **noon on Wednesday**.

## {{mtask}} Install Software

Make sure you have [installed the course software](../../resources/software.md) so you can complete the assignment.

## {{mquiz}} Week 1 Quiz

The Week 1 individual quiz (in {{LMS}}) is due at **8am Thursday**.
It is only over material prior to this point.

You will have **30 minutes** from when you start the quiz to complete it.
These quizzes are never going to be terribly long; this one is particularly designed to be pretty easy, as an
initial quick check and to give you experience with the quiz process.

:::{tip}
I recommend watching the remaining videos before class Thursday as well, but they will not
be tested over in the quiz.
:::

## {{mvideo}} {{mnotebook}} Our First Python Notebook

This video shows you how to start Jupyter, create a notebook, and run Python code.
It also shows you how to prepare a notebook to submit as an assignment.

:::{video}
:length: 9m30s
:name: 1-4 - Our First Python
:alt-id: 6711ca83-10fb-4e4d-8a09-aef6015f4caf
:alt-title: Onyx Video
:::

:::{note}
I have seen cases where the instructions to export to a PDF do not work correctly in Firefox; they result in a mangled
PDF file that does not correctly display charts.  If you encounter this problem, I have documented some fixes over in
the [common problems](prob-mangled-pdf) page.
:::

### Resources

- [Notebook](DemoNotebook.ipynb)
- [Tutorial notebooks](../../resources/tutorials/index.md)

## {{mclass}} Thursday class

In class on Thursday, we will:

- Meet our teams
- Take the Week 1 team quiz (over the same material as the individual quiz)
- Debug software installations
- Activity to dive deeper into defining problems and questions

## {{mbook}} Textbook Chapters - Python

The Python material we are working on this week is a subset of the material in chapters **1–4** of
the [textbook](../../resources/index.md#books). I don't expect to you get through all 3 chapters
thoroughly this week, and we will be introducing more Python features as we need them throughout the
semester. I will note specific chapters and sections relevant to videos in their _Resources_
subsections.

## {{mvideo}} Data Types and Control Flow

This video introduces fundamental Python data types and operations, along with variables and basic control flow.

:::{video}
:length: 19m17s
:name: 1-5 - Data Types and Operations
:::

### Resources

- [Slide deck notebook](1-7-types-operations)
- [Tutorial notebook](../resources/tutorials/TypesAndOperations.ipynb) with the same content
- [Python tutorial](https://docs.python.org/3/tutorial/index.html)
- Textbook 2.3, 3.1
- Tutorial notebook [Fun with Numbers](../resources/tutorials/FunWithNumbers.ipynb)

## {{mvideo}} Control Structures

This video introduces Python control structures and code layout.

:::{video}
:length: 6m56s
:name: 1-6 - Control Structures
:::

## {{mdoc}} Further Python study

If you would like further study on Python fundamentals, especially if programming in general is new to you, here are some resources:

- Python comes with a [quite good tutorial](https://docs.python.org/3/tutorial/)
- [Learn Python the Hard Way](https://learnpythonthehardway.org/python3/) is quite in-depth, and extensive lecture videos are available.
- [Lecture notes from MIT's intro to Python course](https://ocw.mit.edu/courses/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/pages/lectures/)

## {{mvideo}} Scientific Python

This video introduces NumPy {py:class}`numpy.ndarray`, the fundamental numeric array data structure for scientific computing.

:::{video}
:length: 13m20s
:name: 1-7 - Scientific Python
:::

### Resources

- Textbook Ch. 4

## {{massignment}} Assignment 0

Complete and submit [Assignment 0](../../assignments/A0/index.md) by **midnight on {date}`wk1 sun long`**.
