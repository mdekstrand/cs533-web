# Week 13 — Unsupervised
{% import 'video.md' as media %}

!!! warning "Draft content"

    This content is still in draft state and has not yet been finalized.
    Do not depend on it as the final requirements for this week.

In this week, we are going to talk more about *unsupervised learning* — learning without labels.
We are not going to have time to investigate these techniques very deeply, but I want you to know about them, and you are experimenting with them in Assignment 6.

This week's content is lighter, since we just had a large assignment and a midterm, and another assignment is due on Sunday.

There is **no quiz** this week due to the cluster of deliverables and upcoming assignment.
I will double-check that this is not a grading problem for anyone.

[TOC]

This week's videos are also available as a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=d4813668-d25c-4972-b077-ac74005f743a).

## :a-video: No Supervision {: data-length="2m51s"}

In this video, we review the idea of supervised learning and contrast it with unsupervised learning.

=== "Video"

    {{ media.video('cfa074b5-dd9c-4b45-8590-ac74005d8b2b') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173390', 'AHEM5KWN4LkcGB0') }}

{{ media.vidtext('13-1 - No Supervision') }}

## :a-video: Decomposing Matrices {: data-length="17m22s"}

This video introduces the idea of *matrix decomposition*, which we can use to *reduce the dimensionality* of data points.

=== "Video"

    {{ media.video('eae061db-3834-4514-9644-ac74005fa6b4') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173349', 'APzn98jtSv0QCak') }}

{{ media.vidtext('13-2 - Decomposing Matrices') }}

### Resources

- The next notebook
- The [PCADemo](./PCADemo.ipynb), demonstrating the PCA plots
- [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html)
- [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

## :a-notebook: Movie Decomposition

The [Movie Decomposition](../../resources/tutorials/MovieDecomp.ipynb) notebook demonstrates matrix decomposition with movie data.

## :a-video: Clustering {: data-length="6m56s"}

This video introduces the concept of *clustering*, another useful unsupervised learning technique.

=== "Video"

    {{ media.video('fc13ea03-e493-4662-8630-ac7400614a2f') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173391', 'ADR5dKQHSG5VznM') }}

{{ media.vidtext('13-3 - Clustering') }}

### Resources

- [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

## :a-notebook: Clustering Example

The [clustering example notebook](../../resources/tutorials/ClusteringExample.ipynb) shows how to use the `KMeans` class.

## :a-video: Vector Spaces {: data-length="7m27s"}

This video talks about *vector spaces* and transforms.

=== "Video"

    {{ media.video('fb68cbf0-6a7e-4a6e-b235-ac740062a396') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173394', 'ACkeUzx3rOug5do') }}

{{ media.vidtext('13-4 - Vectors and Spaces') }}

## :a-notebook: Practice: SVD on Paper Abstracts {: #practice}

The [Week 13 Exercise notebook](./Week13.ipynb) demonstrates latent semantic analysis on paper abstracts and has an exercise to classify text into new or old papers.

It requires the [chi-papers.csv](./chi-papers.csv) file, which is derived from the [HCI Bibliography](http://hcibib.org).
It is the abstracts from papers published at the CHI conference (the primary conference for human-computer interaction) over a period of nearly 40 years.

If you want to see how to create this file, see the [Fetch CHI Papers example](../../resources/tutorials/FetchCHIPapers.ipynb).

## :a-assignment: Assignment 6

[Assignment 6](../../assignments/A6/index.md) is due **November 22, 2020**.
