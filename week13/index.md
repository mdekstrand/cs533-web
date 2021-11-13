# Week 13 — Unsupervised ({date}`wk13 range`)

In this week, we are going to talk more about *unsupervised learning* — learning without labels.
We are not going to have time to investigate these techniques very deeply, but I want you to know about them, and you are experimenting with them in Assignment 6.

This week's content is lighter, since we just had a large assignment and a midterm, and another assignment is due on Sunday.

## {{moverview}} Content Overview

:::{module} week13
:folder: 0ad54e44-0249-4039-b405-adc601833667
:::

## {{mcal}} Deadlines

- Quiz 13, {date}`wk13 thu long`
- [Assignment 6](../assignments/A6/index.md), {date}`wk13 sun long`

## {{mvideo}} No Supervision

In this video, we review the idea of supervised learning and contrast it with unsupervised learning.

:::{video}
:name: 13-1 - No Supervision
:length: 2m51s
:::

## {{mvideo}} Decomposing Matrices

This video introduces the idea of *matrix decomposition*, which we can use to *reduce the dimensionality* of data points.

:::{video} decomp
:name: 13-2 - Decomposing Matrices
:length: 17m22s
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
:name: 13-3 - Clustering
:length: 6m56s
:::

### Resources

- {py:class}`sklearn.cluster.KMeans`

## {{mnotebook}} Clustering Example

The [clustering example notebook](../resources/tutorials/ClusteringExample.ipynb) shows how to use the `KMeans` class.

## {{mvideo}} Vector Spaces

This video talks about *vector spaces* and transforms.

:::{video}
:name: 13-4 - Vectors and Spaces
:length: 7m27s
:::

## {{mvideo}} Information and Entropy

This video introduces the idea of *entropy* as a way to quantify information.  It's something I want to make sure you've seen
at least once by the end of the class.

:::{video}
:name: 13-5 - Information and Entropy
:length: 10m31s
:::

### Resources

* [<cite>An Introduction to Information Theory: Symbols, Signals & Noise</cite>](http://www.worldcat.org/oclc/1170834662) by John R. Pierce
* [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory)) on Wikipedia

## {{mquiz}} Week 13 Quiz

Take the Week 13 quiz on Canvas.

## {{mnotebook}} Practice: SVD on Paper Abstracts

The [Week 13 Exercise notebook](./Week13.ipynb) demonstrates latent semantic analysis on paper abstracts and has an exercise to classify text into new or old papers.

It requires the {download}`chi-papers.csv <../resources/data/chi-papers.csv>` file, which is derived from the [HCI Bibliography](http://hcibib.org).
It is the abstracts from papers published at the CHI conference (the primary conference for human-computer interaction) over a period of nearly 40 years.

If you want to see how to create this file, see the [Fetch CHI Papers example](../resources/tutorials/FetchCHIPapers.ipynb).

## {{massignment}} Assignment 6

[Assignment 6](../assignments/A6/index.md) is due **{date}`wk13 sun long`**.
