# Week 2 — Description

:::{draft}
This content is still in draft state and has not yet been finalized.
Do not depend on it as the final requirements for this week.
:::

The learning outcomes for this week are:

- To load a data file into Pandas and describe its basic structural characteristics.
- To identify the type of a variable and descriptive statistics appropriate to it.
- To describe the distribution of a variable numerically and visually.
- To describe how data was collected.
- To reason about limitations of the collection of data.

We'll do this through several resources and activities:

[TOC]

This week's material uses chapters 5 and 10 of the textbook.

The videos are also available as a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=e65324ca-97ca-4585-b1b3-ac24004be07e).

## :material-video: Describing Data {: data-length="6m27s"}

This video introduces the week's topic: describing data and data sets.
We discuss the pipeline by which phenomena become a data set.

=== "Video"

    {{ media.video('53e2a763-0208-45ab-bfbf-ac240049618e') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172971', 'AGb5_joj5Xdvfk0') }}

## :material-file-document: What is a Dataset? {: data-length="1950 words"}

Read [What is a Dataset?](https://blog.ldodds.com/2013/02/09/what-is-a-dataset/) by Leigh Dodds.
This article looks at how the term ‘data set’ is defined by different communities, and the common themes to these definitions.

This article does reference some concepts we haven't yet gotten to.
For example, when they talk about whether the data has been labeled for a particular task, they are referring to labels we would use for a prediction or classification task, which we will discuss in a few weeks when we talk about regression and classification.
Don't feel like you need to understand every concept in this article in your first read; understand what you can, and we'll return to it.

## :material-file-download: MovieLens Data

Download the [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/).  The Zip file is 250MB, and the files take about 1.2GB uncompressed.

You can use the smaller 20M or `latest-small` versions for practice if you want to play with a smaller version.

I will be using this dataset in the demo notebooks for this week.

!!! cite "MovieLens Paper"

    Harper, F. M. and Konstan, J. A. (2015) ‘The MovieLens Datasets: History and Context’, <cite>ACM Transactions on Interactive Intelligent Systems</cite>, 5(4), pp. 19:1–19:19.
    DOI [10.1145/2827872](http://dx.doi.org/10.1145/2827872).

    This paper is **not** an assigned reading — it is here for your information.

## :material-video: Pandas Basics {: data-length="8m26s"}

In this video, I introduce Pandas and the Pandas `DataFrame` data structure.
We see how to load a CSV file and inspect the resulting data frame.

=== "Video"

    {{ media.video('3280df0e-dccd-4042-9edb-ac24004b64cf') }}

=== "Slides"

    <div class=slide-container>
    <iframe class=slide-embed src="2-2-slides.html"></iframe>
    </div>

### Resources

* [Notebook](2-2 - Pandas Basics.ipynb)
* Textbook section 5.1

## :material-video: Variables and Types {: data-length="15m46s"}

In this video, we learn the different types of data (_variables_) that we will encounter.

=== "Video"

    {{ media.video('592e8114-9269-4ccc-bad4-ac24004c2a06') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172975', 'AEdM3U338m0PRso') }}

### Resources

* [Palmer Penguins data set](https://github.com/allisonhorst/palmerpenguins)

## :material-file-document: Datasheets for Datasets {: data-length="4100 words"}

Read [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Timnit Gebru et al.

## :material-clipboard-list: Week 2 Quiz

Submit the Week 2 quiz by **Monday night**.

## :material-book: Textbook Chapters {: #textbook}

This week's material uses chapters 5 and 10 of the textbook.
We aren't getting to everything in those chapters though.

## :material-video: Groups and Aggregates {: #group-agg data-length="14m12s"}

In this video, we discuss how compute aggregate statistics in Pandas.

=== "Video"

    {{ media.video('9307fa0c-b4e2-4900-b1a3-ac270026d232') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0!72980', 'APZCbpVCLFI74-U') }}

### Resources

- [Notebook for this video](2-4 - Aggregates and Groups.ipynb)
- Textbook 10.1–10.2

## :material-video: Descriptive Statistics {: data-length="16m32s"}

In this video, we discuss descriptive statistics for numeric variables.

=== "Video"

    {{ media.video('d91cd2fc-a7f6-4610-a6d0-ac270026d1b7') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172978', 'AF4pIDEqeSJMSR8') }}

## :material-video: Describing Distributions {: data-length="10m17s"}

This video introdues the concept of _distributions_, and how we can see the shape and layout of our data.

=== "Video"

    {{ media.video('3064cb1d-8fea-46c7-b863-ac270024fd1b') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172985', 'AFKFlxWtifklVVE') }}

### Resources

- [Notebook](2-6 - Describing Distributions.ipynb)

## :material-video: Data Sources and Bias {: data-length="8m46s"}

=== "Video"

    {{ media.video('cd0f028e-970a-498c-8bbf-ac270026d15b') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172983', 'AAJ1g0hwAUBmF1c')}}

### Resources

- Olteanu, Alexandra and Castillo, Carlos and Diaz, Fernando and Kiciman, Emre, Social Data: Biases, Methodological Pitfalls, and Ethical Boundaries (December 20, 2016). <cite>Frontiers in Big Data</cite> 2:13. doi: [10.3389/fdata.2019.00013](https://dx.doi.org/10.3389/fdata.2019.00013), Available at SSRN: <http://dx.doi.org/10.2139/ssrn.2886526>

## :material-video: Codings and Encodings {: data-length="8m57s"}

This video talks more about how data is encoded, and what we need to document about that.

=== "Video"

    {{ media.video('d8673453-458b-4c03-baf9-ac270026d187') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2172987', 'APm1GElna_P6o40') }}

### Resources

- [float.exposed](https://float.exposed/0x3dcccccd) - explore floating-point numbers

## :material-notebook: Tutorial Notebooks

The [tutorial notebooks](../../resources/tutorials/index.md) contain more info on the Python code, including more systematic overviews of the different Python and Pandas features.

**We will not get to all Pandas features you might need in videos.**
These notebooks, the textbook, and the [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html) all provide additional information on Pandas, NumPy, and SciPy.

## :fontawesome-solid-tasks: Practice

In a few videos, I have used the *Palmer Penguins* data set.

- [Download data in CSV](penguins.csv) (provided under CC-0)
- Look at the documentation and references in the [source repository](https://github.com/allisonhorst/palmerpenguins)
- Describe the distributions of the different variables numerically and graphically
- See how many questions from *Datasheets for Datasets* you can find answers to in the penguin data documentation

For more practice, you can look at the paper for the MovieLens data and try to answer Datasheets questions for it too!

## :material-inbox: Assignment 1

Start working on [Assignment 1](../../assignments/A1/index.md).  It is due at the end of Week 3.
