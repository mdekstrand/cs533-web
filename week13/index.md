# 🚧 Week 13 — Unsupervised ({date}`wk13 range`) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
:::

In this week, we are going to talk more about *unsupervised learning* — learning without labels.
We are not going to have time to investigate these techniques very deeply, but I want you to know about them, and you are experimenting with them in Assignment 6.

This week's content is lighter, since we just had a large assignment and a midterm, and another assignment is due on Sunday.

## {{moverview}} Content Overview

:::{module} week13
:::

## {{mcal}} Deadlines

- Quiz 13, {date}`wk13 thu long`
- [Assignment 6](../assignments/A6/index.md), {date}`wk13 sun long`

## {{mvideo}} No Supervision

In this video, we review the idea of supervised learning and contrast it with unsupervised learning.

:::{video}
:id: cfa074b5-dd9c-4b45-8590-ac74005d8b2b
:name: 13-1 - No Supervision
:length: 2m51s
:slide-id: 495979F9A431DDB0%2173390
:slide-auth: AHEM5KWN4LkcGB0
:::

## {{mvideo}} Decomposing Matrices

This video introduces the idea of *matrix decomposition*, which we can use to *reduce the dimensionality* of data points.

:::{video} decomp
:id: eae061db-3834-4514-9644-ac74005fa6b4
:name: 13-2 - Decomposing Matrices
:length: 17m22s
:slide-id: 495979F9A431DDB0%2173349
:slide-auth: APzn98jtSv0QCak
:::

### Resources

- The next notebook
- The [PCADemo](../resources/tutorials/PCADemo.ipynb), demonstrating the PCA plots
- {py:class}`sklearn.decomposition.TruncatedSVD`
- {py:class}`sklearn.decomposition.PCA`

## {{mnotebook}} Movie Decomposition

The [Movie Decomposition](../resources/tutorials/MovieDecomp.ipynb) notebook demonstrates matrix decomposition with movie data.

## {{mvideo}} Clustering

This video introduces the concept of *clustering*, another useful unsupervised learning technique.

:::{video}
:id: fc13ea03-e493-4662-8630-ac7400614a2f
:name: 13-3 - Clustering
:length: 6m56s
:slide-id: 495979F9A431DDB0%2173391
:slide-auth: ADR5dKQHSG5VznM
:::

### Resources

- {py:class}`sklearn.cluster.KMeans`

## {{mnotebook}} Clustering Example

The [clustering example notebook](../resources/tutorials/ClusteringExample.ipynb) shows how to use the `KMeans` class.

## {{mvideo}} Vector Spaces

This video talks about *vector spaces* and transforms.

:::{video}
:id: fb68cbf0-6a7e-4a6e-b235-ac740062a396
:name: 13-4 - Vectors and Spaces
:length: 7m27s
:slide-id: 495979F9A431DDB0%2173394
:slide-auth: ACkeUzx3rOug5do
:::

## {{mquiz}} Week 13 Quiz

The Week 13 quiz is due on Thursday morning.

## {{mnotebook}} Practice: SVD on Paper Abstracts

The [Week 13 Exercise notebook](./Week13.ipynb) demonstrates latent semantic analysis on paper abstracts and has an exercise to classify text into new or old papers.

It requires the {download}`chi-papers.csv <../resources/data/chi-papers.csv>` file, which is derived from the [HCI Bibliography](http://hcibib.org).
It is the abstracts from papers published at the CHI conference (the primary conference for human-computer interaction) over a period of nearly 40 years.

If you want to see how to create this file, see the [Fetch CHI Papers example](../resources/tutorials/FetchCHIPapers.ipynb).

## {{massignment}} Assignment 6

[Assignment 6](../assignments/A6/index.md) is due **{date}`wk13 sun long`**.
