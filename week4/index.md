# Week 4 — Inference (9/13–17)

These are the learning outcomes for the week:

- Understand the elements of probability
- Interpret and write conditional probabilities for events
- Understand the key relationships between discrete and continuous probability
- Compute and interpret a confidence interval

## Revision Log

Thu, Sep. 16
:   updated quiz to reflect changed release/deadline

## {{moverview}} Content Overview

```{module} week4
:folder: 8a5c2081-e745-4084-ad98-ad9c018384ea
```

This week is at the upper end for total video of any week in the course, and also has some of the
trickier concepts.  The next week — Week 5 — is significantly lighter in terms of new material, and
we'll take a step back to try to solidify the things we've learned so far in the class before
proceeding to Week 6.

## {{mcal}} Deadlines

- Week 3 Quiz on **Monday, Sep. 20** at 12PM

## {{mvideo}} Introduction

:::{video}
:length: 10m36s
:name: 4-1 - Inference Intro
:::


## {{mvideo}} Probability

:::{video} probability
:length: 13m46s
:name: 4-2 - Probability
:::


## {{mvideo}} Joint and Conditional Probability

:::{video} joint-conditional
:length: 11m50s
:name: 4-3 - Joint and Conditional
:::


## {{mvideo}} Continuous Probability

:::{video}
:length: 11m48s
:name: 4-4 - Continuous Probability
:::

## {{mdoc}} Notes on Probability

:::{reading}
:title: Notes on Probability
:url: ../resources/probability/
:length: 349 words
:::

My [notes on probability](../resources/probability.md) provide a linear, summary treatment of the
concepts of probability that we have discussed, along with pointers for further reading.

I expect you will likely need to return to the probability material as we progress through the semester
and use it more and more.  A few particularly important things you need to be able to understand are:

- What does a probability $\P[A]$ mean?
- What does a conditional probability $\P[A|B]$ mean?
- What does a joint probability $\P[A,B]$ mean?
- What does an expected value $\E[X]$ mean?

In my teaching of later material, I use probability notation a lot, as it is a concise but
(relatively) unambiguous way to communicate many important concepts.  Also, while the philosophy of
probability is largely out of scope of this course, my own philosophy of probability (roughly,
instrumentalism) means that I use probabilities to describe things that a strict philosophical
frequentist likely would not.  One of the most practical implications for this class is that I will use
conditional probability as a shorthand for fractions of events or observations:

$$
\P[A|B] = \frac{|A \cap B|}{|B|}
$$

You can derive this fraction yourself from $\P[A] = \frac{|A|}{n}$, where $n$ is the total number of
possible events or observations, and cancelling the $n$.

## {{mvideo}} {{mnotebook}} Distributions

:::{video}
:length: 9m24s
:name: 4-5 - Distributions
:::

### Resources

- The [Probability Distribution notebook](Distributions.ipynb)
- Wikipedia has a good [list of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)

## {{mvideo}} Sampling and the Data Generation Process

:::{video} sampling
:length: 17m53s
:name: 4-6 - Sampling and the DGP
:::

### Resources

- [Sampling notebook](SamplingDists.ipynb)

## {{mvideo}} Confidence

:::{video} confidence
:length: 13m6s
:name: 4-7 - Confidence
:::

## {{mdoc}} Confidence in Confidence

```{reading} confidence-in-confidence
:url: https://medium.com/@EpiEllie/having-confidence-in-confidence-intervals-8f881712d837
:title: Having confidence in confindence intervals
:length: 225 words
```

Read [Having confidence in confidence intervals](https://medium.com/@EpiEllie/having-confidence-in-confidence-intervals-8f881712d837) by Ellie Murray.

## {{mvideo}} The Bootstrap

:::{video} bootstrap
:length: 7m26s
:name: 4-8 - The Bootstrap
:::

## {{mquiz}} Week 4 Quiz

The Week 4 quiz is on Canvas, and is due at 12pm (noon) on Monday, Sep. 20.

## {{mnotebook}} Penguin Inference

The [Penguin Inference notebook](../../resources/tutorials/PenguinSamples.ipynb) shows confidence intervals and hypothesis tests on the penguin data.

## 📚 Further Reading

If you want to dive more deeply into probability theory, Michael Betancourt's case studies are rather mathematically dense but quite good:

- [Probability Theory (For Scientists and Engineers)](https://betanalpha.github.io/assets/case_studies/probability_theory.html)
- [Conditional Probability](https://betanalpha.github.io/assets/case_studies/conditional_probability_theory.html)
- [Product Placement](https://betanalpha.github.io/assets/case_studies/probability_on_product_spaces.html) (probability over product spaces)

For a book:

- [Introduction to Probability](https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf) by Grinstead and Snell
- [An Introduction to Probability and Simulation](https://bookdown.org/kevin_davisross/probbook/) - a hands-on online book using Python simulations

## 📚 Extra Reading (Philosophy)

-   [Moving to a World Beyond “p < 0.05”](http://dx.doi.org/10.1080/00031305.2019.1583913), by Wasserstein, Schirm, and Lazar.

-   [Abandon Statistical Significance](http://www.stat.columbia.edu/~gelman/research/unpublished/abandon.pdf), by McShane, Gal, Gelman, Robert, and Tackett.
    While the title is provocative, this article is not advocating against computing statistical significance measures.
    It advocates using them as one piece of evidence among many, instead of as an end-of-the-story bright-line rule for establishing discovery.

-   [Interpretations of Probability](https://plato.stanford.edu/entries/probability-interpret/).
    I primarily operate from somewhere in the subjective school, with a strong dose of instrumentalism.

## {{massignment}} Assignment 2

[Assignment 2](../assignments/A2/index.md) is due on **September 26**.
