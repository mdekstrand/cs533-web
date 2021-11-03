# Week 12 — Text ({date}`wk12 range`)

:::{attention}
The second midterm is on **{date}`wk12 tue xlong`**.
:::

This week we are going to talk about *unstructured data*, particularly text.

## {{moverview}} Content Overview

:::{module} week12
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
:id: dde82af5-7c5f-4df4-807b-ac6d004d1d34
:name: 12-1 - Unstructured Data
:length: 2m57s
:slide-id: 495979F9A431DDB0%2173340
:slide-auth: AP4XTmNhYJeUW4A
:::

## {{mvideo}} Unicode and Encodings

In this video, I describe Unicode and text encodings.

:::{video}
:id: 7b4ca444-6d1a-4848-aafd-ac6d00539b23
:name: 12-2 - Unicode and Encodings
:length: 28m45s
:slide-id: 495979F9A431DDB0%2173344
:slide-auth: AJWLHFsJ8GwmbUg
:::

### Resources

- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [Twitter thread on the politics of emoji decomposition](https://twitter.com/brookLYNevery1/status/1167409916899934209)

## {{mvideo}} The Text Processing Pipeline

This video discusses the basic steps of text processing, beginning with tokenization.
The result is a document/term matrix, possibly normalized.

:::{video} pipeline
:id: 58038e58-a1d6-49bf-82c9-ac6d005a287a
:name: 12-3 - Text Processing Pipeline
:length: 17m36s
:slide-id: 495979F9A431DDB0%2173342
:slide-auth: AJ1kEb9itG5obig
:::

### Resources

- [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer)
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)
- [NLTK](https://www.nltk.org/)
- [Stanza](https://stanfordnlp.github.io/stanza/) (formerly StanfordNLP)

## {{mvideo}} Vectors and Similarity

This video describes the concept of a *vector representation*, and how to compute the similarity between two documents.

:::{video} similarity
:id: 10db2775-5258-4adc-8eaf-ac6d005a2848
:name: 12-4 - Vectors and Similarity
:length: 6m58s
:slide-id: 495979F9A431DDB0%2173347
:slide-auth: PpcK
:::

## {{mvideo}} Classifying Text

This video introduces *classifying text*, and the use of a naïve Bayes classifier based on term frequencies.

:::{video}
:id: 8e92f9de-2437-4633-af10-ac6d005b10e8
:name: 12-5 - Classifying Text
:length: 6m9s
:slide-id: 495979F9A431DDB0%2173351
:slide-auth: APyYW6VLHuHdq_s
:::

### Resources

- [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
- [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB) (Naïve Bayes)

## {{mnotebook}} Spam Filter Example

The [Spam Filter Example](../../resources/tutorials/SpamFilter.ipynb) demonstrates tokenization and classification with text.

## {{mquiz}} Week 12 Quiz

The Week 12 quiz is on Blackboard.

## {{massignment}} Assignment 6

[Assignment 6](../assignments/A6/index.md) is available and is due **{date}`wk13 sun long`**.
