# Week 12 — Text
{% import 'video.md' as media %}

[TOC]

This week's videos are also available in a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=6eab80fb-6bb6-43b4-a916-ac6d005b60d4).

## :a-video: Unstructured Data {: #intro data-length="2m57s"}

This video introduces the week and describes the key ideas of extracting features from unstructured data.

=== "Video"

    {{ media.video('dde82af5-7c5f-4df4-807b-ac6d004d1d34') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173340', 'AP4XTmNhYJeUW4A') }}

## :a-video: Unicode and Encodings {: #encoding data-length="28m45s"}

In this video, I describe Unicode and text encodings.

=== "Video"

    {{ media.video('7b4ca444-6d1a-4848-aafd-ac6d00539b23') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173344', 'AJWLHFsJ8GwmbUg') }}

### Resources

- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Python Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
- [Twitter thread on the politics of emoji decomposition](https://twitter.com/brookLYNevery1/status/1167409916899934209)

## :a-video: The Text Processing Pipeline {: #pipeline data-length="17m36s"}

This video discusses the basic steps of text processing, beginning with tokenization.
The result is a document/term matrix, possibly normalized.

=== "Video"

    {{ media.video('58038e58-a1d6-49bf-82c9-ac6d005a287a') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173342', 'AJ1kEb9itG5obig') }}

### Resources

- [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer)
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)
- [NLTK](https://www.nltk.org/)
- [Stanza](https://stanfordnlp.github.io/stanza/) (formerly StanfordNLP)

## :a-quiz: Week 12 Quiz

The Week 12 quiz is on Blackboard.

## :a-video: Vectors and Similarity {: #similarity data-length="6m58s"}

This video describes the concept of a *vector representation*, and how to compute the similarity between two documents.

=== "Video"

    {{ media.video('10db2775-5258-4adc-8eaf-ac6d005a2848') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173347', 'APpcK-wozJflEL8') }}

## :a-video: Classifying Text {: data-length="6m9s"}

This video introduces *classifying text*, and the use of a naïve Bayes classifier based on term frequencies.

=== "Video"

    {{ media.video('8e92f9de-2437-4633-af10-ac6d005b10e8') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173351', 'APyYW6VLHuHdq_s') }}

### Resources

- [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier)
- [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB) (Naïve Bayes)

## :a-notebook: Spam Filter Example

The [Spam Filter Example](../../resources/tutorials/SpamFilter.ipynb) demonstrates tokenization and classification with text.

## :a-assignment: Assignment 5

[Assignment 5](../../assignments/A5/index.md) is due **November 11, 2020**.

## :a-quiz: Midterm 2

The second midterm will be released at **5PM** on **Wednesday, November 11**.

## :a-assignment: Assignment 6

[Assignment 6](../../assignments/A6/index.md) is available and is due **November 22, 2020**.
