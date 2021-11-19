# 🚧 Week 14 — Workflow ({date}`wk14 range`) 🚧

:::{draft}
This content is still in draft state and has not yet been finalized.
:::

In this week, we are going to talk more about *workflows*.
What does it look like to build a practical data science pipeline?

## {{moverview}} Content Overview

:::{module} week14
:folder: da13b422-df02-491a-bc43-adc601833918
:::

## {{mcal}} Deadlines

- Quiz 14, {date}`wk14 thu long`
- Assignment 7, {date}`week15 sun long`

## {{mvideo}} From Notebooks to Workflows

In this video, we introduce going beyond notebooks to broader structures for our Python projects.

:::{video}
:name: 14-1 - From Notebooks to Workflows
:length: 3m44s
:slide-id: 495979F9A431DDB0%2173401
:slide-auth: AKrc_UfM5PLb-hc
:::

## {{mvideo}} Scripts and Modules

This video introduces Python scripts and modules, and how to organize Python code outside of a notebook.

:::{video}
:name: 14-2 - Scripts and Modules
:length: 15m33s
:slide-id: 495979F9A431DDB0%2173403
:slide-auth: AA0tIVINHt7Z2GE
:::

### Resources

- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [docopt](http://docopt.org/), a very useful tool for processing command-line arguments
- [Environment Variables in glossary](../../resources/glossary.md#envvar)
- [LK Demo Experiment](https://github.com/lenskit/lk-demo-experiment), which I used in the demo; this also uses DVC
- [tmux](https://github.com/tmux/tmux/wiki)

## {{mvideo}} Introducing Git

This video introduces version control with Git.

:::{video}
:name: 14-3 - Introducing Git
:length: 12m2s
:slide-id: 495979F9A431DDB0%2173404
:slide-auth: ACF19qqHL2TJnCs
:::

### Resources

- [Git Resources](../../resources/git-resources.md) (including my example `.gitignore` file)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Resources to Learn Git](https://try.github.io/)
- [Version Control by Example](https://ericsink.com/vcbe/index.html)
- [GitHub Student Developer Pack](https://education.github.com/pack)

## {{mvideo}} Git for Data Science

How do you use Git effectively in a data science project?

:::{video}
:name: 14-4 - Git for Data Science
:length: 6m52s
:slide-id: 495979F9A431DDB0%2173405
:slide-auth: AGba4PqAto3WUCU
:::

### Resources

-   [NoteBook DIff and MErge (nbdime)](https://nbdime.readthedocs.io/en/latest/) — tools for diff/merge of notebooks.  Available in Conda:

        conda install nbdime

-   [git-lfs](https://git-lfs.github.com/)


## {{mvideo}} Extract, Transform, Load

The Extract, Transform, Load (ETL) pipeline is a common design pattern for data ingest.
Sometimes it is adjusted to Extract, Load, Transform.

:::{video}
:name: 14-5 - ETL
:length: 6m46s
:slide-id: 495979F9A431DDB0%2173407
:slide-auth: AEmcmPne5UWF0ts
:::

{{ media.vidtext('14-5 - ETL') }}

### Resources

- [ETL — Understanding It and Effectively Using It](https://medium.com/hashmapinc/etl-understanding-it-and-effectively-using-it-f827a5b3e54d)
- [ETL vs. ELT](https://www.iri.com/blog/data-transformation2/etl-vs-elt-we-posit-you-judge/)
- [Wikipedia article on ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load)
- The [{{mvideo}} Week 7 Example](../week7/index.md#example) uses an ELT design

## {{mvideo}} Split, Apply, Combine

We've seen group-by operations this semester; they're a specific form of a general paradigm called *split, apply, combine*.

:::{video}
:name: 14-6 - Split Apply Combine
:length: 6m45s
:slide-id: 495979F9A431DDB0%2173408
:slide-auth: AEuwR_CdpmKJj_o
:::

### Resources

- [Split, Apply, Combine at Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)

## {{mvideo}} Tuning Hyperparameters

How can we move beyond `GridSearchCV` in our quest to tune hyperparameters?

:::{video}
:name: 14-7 - Tuning Hyperparameters
:length: 10m49s
:slide-id: 495979F9A431DDB0%2173409
:slide-auth: ACJeAazU69nVuOI
:::

### Resources

- [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)
- [scikit-optimize](https://scikit-optimize.github.io/stable/)
- [BayesSearchCV example](https://scikit-optimize.github.io/stable/auto_examples/sklearn-gridsearchcv-replacement.html)

## {{mnotebook}} Tuning Example

The [Tuning Example](../resources/tutorials/TuningExample.ipynb) notebook demonstrates hyperparameter tuning by cross-validation with multiple techniques.

## {{mvideo}} Reproducible Pipelines

I provide *very brief* pointers to additional tools you may want for workflow management in more advanced projects.

:::{video}
:name: 14-8 - Reproducible Pipelines
:length: 8m28s
:slide-id: 495979F9A431DDB0%2173410
:slide-auth: ADPxMcuuaI3Kv0w
:::

### Resources

Some software that supports data and/or workflow management:

- [Data Version Control](https://dvc.org) — I use this
- [MLflow](https://mlflow.org/) — support for machine learning workflows

## {{mdoc}} Software Environments

:::{reading}
:title: Software Environments
:url: ../resources/environments.md
:length: 1068 words
:::

Read [software environments](../resources/environments.md).

## {{mquiz}} Weekly Quiz 14

Take **Quiz 14** in {{LMS}}.

## {{mnotebook}} More Examples

My [book author gender](https://github.com/BoiseState/book-author-gender) project is an example of an advanced workflow with DVC.

## {{massignment}} Assignment 7

[Assignment 7](../../assignments/A7/index.md) is due **{{wk15 sun xlong}}**.
