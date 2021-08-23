# Week 1 — Questions

The key learning outcomes for this week are:

- Ask and refine questions that can be answered with data
- Install and run the software required for the course
- Write and run basic Python code in a Jupyter notebook
- Begin to think about the complexity of meaningful questions

This week draws from chapters 1–4 from {book}`p4da` and chapters 1-2 of {book}`tlds`.
If you already know Python, the Python parts should mostly be review.

## {{moverview}} Content Overview

:::{module} week1
:playlist: https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=462597a6-abd8-4685-89a3-ad88013f7c35
:::

## {{mcal}} Deadlines

This week has the following deadlines:

- [Pre-class inventory](#pre-class-inventory) at **11:59 pm on Tuesday**
- [Week 1 quiz](#week-1-quiz) at **8am on Thursday**
- [Assignment 0](#assignment-0) at **11:59 pm on Sunday**

## {{mvideo}} Introduction

This video introduces the course and our learning outcomes for the term.

:::{video} introduction
:id: 52f6698f-a7dd-4943-86eb-ad7501790760
:length: 12m34s
:slide-id: 495979F9A431DDB0%2173705
:slide-auth: AP_wALvN9RZhibw
:name: 1-1 - Introduction
:amara: https://amara.org/en/videos/RexP2ZyVNfU3/info/https52f6698f-a7dd-4943-86eb-ad7501790760-fc4269eb-1399-4a33-9140-ad8c0105606bmp4invocationid08872c6d-6303-ec11-a9e9-0a1a827ad0ec/
:::

## {{mvideo}} Asking Questions

In this video, I introduce *questions* in their broader context of using data to advance goals. 
I also introduce the idea of **operationalization**, which will be a key concept throughout the class.

:::{video} asking-questions
:id: 1b19dc1f-fee8-4505-9294-ad7501796f97
:length: 10m35s
:slide-id: 495979F9A431DDB0%2172944
:slide-auth: AFZ_21-M4BmFQyE
:name: 1-2 - Asking Questions
:amara: https://amara.org/en/videos/ChlYL843WN78/info/https1b19dc1f-fee8-4505-9294-ad7501796f97-4e0a033c-d7ab-4c00-a03e-ad8c010d5105mp4invocationid1644c8dc-6503-ec11-a9e9-0a1a827ad0ec/
:::

### Further Reading

* [How to Ask the Right Questions](https://towardsdatascience.com/how-to-ask-the-right-questions-as-a-data-scientist-913621907411)

## {{mvideo}} Questioning Questions

We make our {term}`operationalizations <Operationalization>` better by questioning them.  What do they capture?  Who or what do they prioritize?

:::{video} questioning-questions
:id: 564e8ea0-13c3-4722-aeca-ad7501798e69
:length: 8m54s
:slide-id: "495979F9A431DDB0%2172946"
:slide-auth: ADgXZwd15GxB2yo
:name: 1-3 - Questioning Questions
:amara: https://amara.org/en/videos/ON0uD7esRCyo/info/https564e8ea0-13c3-4722-aeca-ad7501798e69-8faeb2ce-79d2-480f-b337-ad8c0110cfc1mp4invocationid7b7b05c5-6603-ec11-a9e9-0a1a827ad0ec/
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

On Tuesday, we will:

- Introduce the class
- Start working on defining and clarifying questions
- Set expectations for the week and semester

## {{mtask}} Pre-Class Inventory

Fill out the [pre-class skill inventory and survey](https://forms.gle/mNgETf37Sr2RqdTd7) by **11:59 pm on Tuesday**.

## {{mtask}} Install Software

Make sure you have [installed the course software](../../resources/software.md) so you can complete the assignment.

## {{mquiz}} Week 1 Quiz

The Week 1 individual quiz (in Canvas) is due at **8am Thursday**.
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
:id: e87e6ac9-4313-4943-87b1-ad75015b95bb
:length: 9m30s
:name: 1-4 - Our First Python
:amara: https://amara.org/en/videos/LUWU3QdwyY0u/info/httpse87e6ac9-4313-4943-87b1-ad75015b95bb-6042448d-66e9-47b4-8b32-ad8c0111f3d4mp4invocationid2e65da02-6d03-ec11-a9e9-0a1a827ad0ec/
:alt-id: dbd531fb-904f-4b2f-b0a3-ad75015afd4c
:alt-title: Onyx Video
:alt-amara: https://amara.org/en/videos/7pm0dwa8XK45/info/httpsdbd531fb-904f-4b2f-b0a3-ad75015afd4c-7ee12dfe-0986-47af-b8df-ad8c011dfdd5mp4invocationid242d7851-6e03-ec11-a9e9-0a1a827ad0ec/
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
:id: 76daa00b-e512-4b20-9f63-ad75015afb57
:length: 19m17s
:name: 1-5 - Data Types and Operations
:amara: https://amara.org/en/videos/cI0umOhazm8A/info/https76daa00b-e512-4b20-9f63-ad75015afb57-119d4d43-a18a-418e-a2fd-ad8c0121c100mp4invocationid2b13d876-6f03-ec11-a9e9-0a1a827ad0ec/
:::

### Resources

- [Slide deck notebook](1-7-types-operations)
- [Python tutorial](https://docs.python.org/3/tutorial/index.html)
- Textbook 2.3, 3.1
- Tutorial notebook [Fun with Numbers](../resources/tutorials/FunWithNumbers.ipynb)

## {{mvideo}} Control Structures

This video introduces Python control structures and code layout.

:::{video}
:id: fb58d0e3-0e42-41ee-b5a6-ad75015afcbf
:length: 6m56s
:slide-id: 495979F9A431DDB0%2172965
:slide-auth: ABwaNR_XOZeDHwo
:name: 1-6 - Control Structures
:amara: https://amara.org/en/videos/d5SOz7zmqbxC/info/httpsfb58d0e3-0e42-41ee-b5a6-ad75015afcbf-2bbdb9c5-cb09-436f-9ff5-ad8c0120ab50mp4invocationid1a5223d2-6e03-ec11-a9e9-0a1a827ad0ec/
:::

## {{mvideo}} Scientific Python

This video introduces NumPy {py:class}`numpy.ndarray`, the fundamental numeric array data structure for scientific computing.

:::{video}
:id: bb427c78-988a-4d4a-b671-ad75015afbf6
:length: 13m20s
:slide-id: 495979F9A431DDB0%2172967
:slide-auth: AMuE85znE-djS3E
:name: 1-7 - Scientific Python
:amara: https://amara.org/en/videos/tOInHEcE0n64/info/httpsbb427c78-988a-4d4a-b671-ad75015afbf6-951fa520-04d5-48a8-a858-ad8c0122cddemp4invocationidcef9e109-7003-ec11-a9e9-0a1a827ad0ec/
:::

### Resources

- Textbook Ch. 4

## {{massignment}} Assignment 0

Complete and submit [Assignment 0](../../assignments/A0/index.md) by **midnight on Sunday, August 30**.
