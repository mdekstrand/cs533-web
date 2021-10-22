# Notebook Checklist & Guide

In this class, it is not enough to create a notebook that contains code to compute correct results.
You also need to ensure that your notebooks are well-structured documents that communicate your work
and findings.

## Standalone Documents

As I discuss in {video}`week3:notebooks`, a notebook is first a **document** — a document that
incorporates code and visuals to present data with written explanation.

This means that you need to provide text that walks your reader through the story of your
data analysis: what you are doing, why, how, and what we learn.  This does not mean you need
to describe every little detail, but you need to provide the context for what the analyses mean
and what we can learn from them.

Further, your assignment notebooks should be readable even without having read the original
assignment description: they should stand alone.  You can reuse a moderate amount of text
from the assignment description (e.g. including the questions verbatim in block quotations is
entirely acceptable), but you're going to need to do more writing and structuring to present
your results in a readable document.

The reason for this is so that you learn to produce outputs that will be useful for your future
studies and work — documents that will communicate results to your colleagues, adviser, etc.
This is a class about doing data science, including communicating it, not just about writing
data science code.

## Process

I recommend that you leave time before submitting your assignments to go back through the notebook
and clean it up for final presentation.

Sometimes it works best to start with the notebook you have and delete unnecessary code, remove
excess debugging outputs, and improve the writing.

Sometimes it works best to start a fresh notebook, start putting together the structure, and copy
over the code you actually need for the final solution.

Either way, you should produce a final notebook that is:

- readable
- executable from top to bottom
- clean of extraneous or unnecessary outputs, particularly without explanation

This last point is to avoid the “sea of charts” effect.  If there are a lot of charts and tables
that don't advance your story, it is much harder to read.

## Checklist

This checklist is to help you ensure your notebook is well-structured and well-written.
I may expand or revise it as we progress through the semester.

### Structure

-   Does the notebook re-run without error from top to bottom?
-   Does re-running the notebook produce correct charts and results?
-   Does the notebook begin with the document title as an L1 heading?
-   Are headings correctly nested (H2 within H1, H3 in H2, etc.)?
-   Are headings short titles? (No full sentences!)

### Writing and Output

-   Does the introduction state the notebook's purpose?
-   Does either the introduction or the data section describe where the data come from?
    -   If it's publicly downloadable, is there a link?
    -   If there are multiple options, which one is used?
-   Does it use correct grammar and spelling?
-   Does it use formatting to provide appropriate emphasis and clarity?
    -   Are Python variable, function, etc. names marked as `code`?
    -   Are lists used when helpful to break down points?
    -   Is mathematical notation used to precisely define measurements when it will increase clarity?
-   Do all outputs help advance the notebook's story?  Have you removed ones only for debugging or trying things out?
-   Do charts & conclusion-supporting outputs have surrounding text explaining their purpose and any extra information needed for accurate interpretation?

### Graphics

-   Do all charts have properly labeled axes and legends (color codes, etc.)?
-   Do charts have titles if purpose is not clear from axes or immediately preceding text?
    -   If there are multiple variants of a chart w/ same axes, they **must** have titles to quickly distinguish.
-   Are charts legible?
-   Do charts present lessons learned without distortions?
-   If you did not create the chart, would you be able to interpret it correctly?
-   Do facets, colors, and axes draw the reader to the most important comparisons or patterns?
-   Does surrounding text, if any, accurately interpret the chart?

The [Data Visualization Checklist](https://depictdatastudio.com/checklist/) is useful, if opinionated.

### Content

-   Are observations and conclusions substantiated by data and/or sound argument?
-   Are goals and observations made clear, both for the document and for individual pieces of analysis?

### Post-Export

-   Are plots correctly displayed in the resulting PDF?  See [common problems](prob-mangled-pdf) for solutions.
