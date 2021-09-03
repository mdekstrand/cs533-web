# 🚧 Week 4 — Inference (9/13–17) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
Do not depend on it as the final requirements for this week.
:::

These are the learning outcomes for the week:

- Understand the elements of probability
- Interpret and write conditional probabilities for events
- Understand the key relationships between discrete and continuous probability
- Compute and interpret a confidence interval
- Compute and interpret hypothesis test
- Avoid {term}`p-hacking` and {term}`HARKing`

## {{moverview}} Content Overview

```{module} week4
```

This week probably has the most total video of any week in the course, and also has some of the more
trickier concepts.  The next week — Week 5 — is significantly lighter in terms of new material, and
we'll take a step back to try to solidify the things we've learned so far in the class before
proceeding to Week 6.

## {{mcal}} Deadlines

- Week 3 Quiz on **Thursday, Sep. 16** at 8AM

## {{mvideo}} Introduction

:::{video}
:id: f04f8c08-04c0-4ac9-a17d-ac33002dc385
:length: 10m36s
:slide-id: 495979F9A431DDB0%2173011
:slide-auth: fAHMCzDSGDskVEXM
:name: 4-1 - Inference Intro
:::


## {{mvideo}} Probability

:::{video} probability
:id: db887c4d-b242-4f59-b418-ac33002dc3b9
:length: 13m46s
:slide-id: 495979F9A431DDB0%2173013
:slide-auth: fAOl1L4WxuyHymCo
:name: 4-2 - Probability
:::


## {{mvideo}} Joint and Conditional Probability

:::{video} joint-conditional
:id: 1cf9fe9f-3d68-442f-a4b1-ac330038e5b2
:length: 11m50s
:slide-id: 495979F9A431DDB0%2173015
:slide-auth: fAFz6X3aaC0ZLhZI
:name: 4-3 - Joint and Conditional
:::


## {{mvideo}} Continuous Probability

:::{video}
:id: 3a9e1f25-e324-4939-a0ba-ac330026530e
:length: 11m56s
:slide-id: 495979F9A431DDB0%2173017
:slide-auth: fAN8SCvQbSm_K8dQ
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
:id: 17e7f5ea-a53f-4a1a-bb45-ac3600436c11
:length: 9m24s
:slide-id: 495979F9A431DDB0%2173025
:slide-auth: fAAYQ0zXcvwJjizw
:name: 4-5 - Distributions
:::

### Resources

- The [Probability Distribution notebook](Distributions.ipynb)
- Wikipedia has a good [list of probability distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)

## {{mvideo}} Sampling and the Data Generation Process

:::{video} sampling
:id: 3f70c0d7-c356-416e-a30e-ac360043f6e5
:length: 17m53s
:slide-id: 495979F9A431DDB0%2173027
:slide-auth: fAEYcilW0NufzD8w
:name: 4-6 - Sampling and the DGP
:::

### Resources

- [Sampling notebook](SamplingDists.ipynb)

## {{mvideo}} Confidence

:::{video} confidence
:id: 73d0ce00-5ad3-4377-b8c4-ac3600436c31
:length: 13m6s
:slide-id: 495979F9A431DDB0%2173029
:slide-auth: fAKuXoEDVB7bgX9g
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
:id: df525810-e4df-4977-afee-ac3600436c8c
:length: 7m26s
:slide-id: 495979F9A431DDB0%2173031
:slide-auth: fAOXsegoiRiZze-I
:name: 4-8 - The Bootstrap
:::

## {{mvideo}} Testing Hypotheses

:::{video} hypotest
:id: b8f249ac-9101-4336-89e8-ac3600436c5a
:length: 14m51s
:slide-id: 495979F9A431DDB0%2173033
:slide-auth: fAPweDd4ZnAHFL6E
:name: 4-9 - Testing Hypotheses
:::

### Resources

- [Statistical test selection flowchart](http://timdraws.net/files/StatisticalTestFinder.pdf)

(p-hacking-cartoon)=
## 💥 Cartoon

Read [XKCD #882: Significant](https://xkcd.com/882/).

This is called **_p_-hacking**: running tests until we find one that is significant.

## {{mquiz}} Week 4 Quiz

The Week 4 quiz is on Blackboard, and is due at 8AM on Thursday.

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
