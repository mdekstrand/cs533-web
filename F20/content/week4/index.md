# Week 4 — Inference

{% import 'video.md' as media %}

[TOC]

## :a-video: Introduction {: data-length="10m36s"}

=== "Video"

    {{ media.video('f04f8c08-04c0-4ac9-a17d-ac33002dc385') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173011', 'AHMCzDSGDskVEXM') }}


## :a-video: Probability {: data-length="13m46s"}

=== "Video"

    {{ media.video('db887c4d-b242-4f59-b418-ac33002dc3b9') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173013', 'AOl1L4WxuyHymCo') }}


## :a-video: Joint and Conditional Probability {: #joint-cond data-length="11m50s"}

=== "Video"

    {{ media.video('1cf9fe9f-3d68-442f-a4b1-ac330038e5b2') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173015', 'AFz6X3aaC0ZLhZI') }}


## :a-video: Continuous Probability {: data-length="11m56s"}

=== "Video"

    {{ media.video('3a9e1f25-e324-4939-a0ba-ac330026530e') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173017', 'AN8SCvQbSm_K8dQ') }}

## :material-clipboard-list: Week 4 Quiz

Submit the Week 4 quiz by **Monday night**.

## :a-video: :a-notebook: Distributions {: data-length="9m24s"}

=== "Video"

    {{ media.video('17e7f5ea-a53f-4a1a-bb45-ac3600436c11') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173025', 'AAYQ0zXcvwJjizw') }}

### Resources

- The [Probability Distribution notebook](Distributions.ipynb)
- Wikipedia has a good [list of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)

## :a-video: Sampling and the Data Generation Process {: #sampling data-length="17m53s"}

=== "Video"

    {{ media.video('3f70c0d7-c356-416e-a30e-ac360043f6e5') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173027', 'AEYcilW0NufzD8w') }}


### Resources

- [Sampling notebook](SamplingDists.ipynb)


## :a-video: Confidence {: data-length="13m6s"}

=== "Video"

    {{ media.video('73d0ce00-5ad3-4377-b8c4-ac3600436c31') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173029', 'AKuXoEDVB7bgX9g') }}


## :a-reading: Confidence in Confidence {: data-length="225 words"}

Read [Having confidence in confidence intervals](https://medium.com/@EpiEllie/having-confidence-in-confidence-intervals-8f881712d837) by Ellie Murray.

## :a-video: The Bootstrap {: #bootstrap data-length="7m26s"}

=== "Video"

    {{ media.video('df525810-e4df-4977-afee-ac3600436c8c') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173031', 'AOXsegoiRiZze-I') }}

## :a-video: Testing Hypotheses {: #hypotest data-length="14m51s"}

=== "Video"

    {{ media.video('b8f249ac-9101-4336-89e8-ac3600436c5a') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173033', 'APweDd4ZnAHFL6E') }}

## :material-image-frame: Cartoon

Read [XKCD #882: Significant](https://xkcd.com/882/).

This is called **_p_-hacking**: running tests until we find one that is significant.

## :a-notebook: Penguin Inference

The [Penguin Inference notebook](../../resources/tutorials/PenguinSamples.ipynb) shows confidence intervals and hypothesis tests on the penguin data.

## :a-reading: Further Reading

If you want to dive more deeply into probability theory, Michael Betancourt's case studies are rather mathematically dense but quite good:

- [Probability Theory (For Scientists and Engineers)](https://betanalpha.github.io/assets/case_studies/probability_theory.html)
- [Conditional Probability](https://betanalpha.github.io/assets/case_studies/conditional_probability_theory.html)
- [Product Placement](https://betanalpha.github.io/assets/case_studies/probability_on_product_spaces.html) (probability over product spaces)

For a book:

- [Introduction to Probability](https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf) by Grinstead and Snell
- [An Introduction to Probability and Simulation](https://bookdown.org/kevin_davisross/probbook/) - a hands-on online book using Python simulations

## :a-reading: Extra Reading (Philosophy)

-   [Abandon Statistical Significance](http://www.stat.columbia.edu/~gelman/research/unpublished/abandon.pdf), by McShane, Gal, Gelman, Robert, and Tackett.
    While the title is provocative, this article is not advocating against computing statistical significance measures.
    It advocates using them as one piece of evidence among many, instead of as an end-of-the-story bright-line rule for establishing discovery.

-   [Interpretations of Probability](https://plato.stanford.edu/entries/probability-interpret/).
    I primarily operate from somewhere in the subjective school.

## :material-inbox: Assignment 2

[Assignment 2](../../assignments/A2/index.md) is due on **September 27**.
