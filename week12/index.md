# Week 12 — Text ({date}`wk12 range`)

:::{attention}
The second midterm is on **{date}`wk12 tue xlong`**.
:::

This week we are going to talk about *unstructured data*, particularly text.

## {{moverview}} Content Overview

:::{module} week12
:folder: 6686c43b-1af7-4d8c-b577-adc6018332e3
:::

## {{mcal}} Deadlines

- Midterm B, {date}`wk12 tue long`
- Quiz 12, {date}`wk12 thu long`

(midterm-b)=
## {{mquiz}} Midterm B

The second midterm will be in-class (9AM) on **{date}`wk12 tue xlong`**.
It follows the same structure and rules as [Midterm A](midterm-a), and is over
material through Week 11.

## {{mvideo}} Unstructured Data

This video introduces the week and describes the key ideas of extracting features from unstructured data.

:::{video} intro
:name: 12-1 - Unstructured Data
:length: 2m57s
:::

## {{mvideo}} Unicode and Encodings

In this video, I describe Unicode and text encodings.

:::{video}
:name: 12-2 - Unicode and Encodings
:length: 28m45s
:::

### Resources

- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [Twitter thread on the politics of emoji decomposition](https://twitter.com/brookLYNevery1/status/1167409916899934209)

## {{mvideo}} The Text Processing Pipeline

This video discusses the basic steps of text processing, beginning with tokenization.
The result is a document/term matrix, possibly normalized.

:::{video} pipeline
:name: 12-3 - Text Processing Pipeline
:length: 17m36s
:::

### Resources

- {py:class}`~sklearn.feature_extraction.text.CountVectorizer`
- {py:class}`~sklearn.feature_extraction.text.TfidfVectorizer`
- [NLTK](https://www.nltk.org/)
- [Stanza](https://stanfordnlp.github.io/stanza/) (formerly StanfordNLP)

## {{mvideo}} Vectors and Similarity

This video describes the concept of a *vector representation*, and how to compute the similarity between two documents.

:::{video} similarity
:name: 12-4 - Vectors and Similarity
:length: 6m58s
:::

## {{mvideo}} Classifying Text

:::{index} naïve Bayes
:::

This video introduces *classifying text*, and the use of a {term}`naïve Bayes` classifier based on term frequencies.

:::{video} classifying-text
:name: 12-5 - Classifying Text
:length: 6m9s
:::

### Resources

- {py:class}`sklearn.neighbors.KNeighborsClassifier`
- {py:class}`sklearn.naive_bayes.MultinomialNB` ({term}`Naïve Bayes`)

## {{mnotebook}} Spam Filter Example

The [Spam Filter Example](../../resources/tutorials/SpamFilter.ipynb) demonstrates tokenization and classification with text.

## {{mquiz}} Week 12 Quiz

The Week 12 quiz is on Blackboard.

## {{massignment}} Assignment 6

[Assignment 6](../assignments/A6/index.md) is available and is due **{date}`wk13 sun long`**.
