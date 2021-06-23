# Week 14 — Workflow
{% import 'video.md' as media %}

In this week, we are going to talk more about *workflows*.
What does it look like to build a practical data science pipeline?

[TOC]

This week's videos are also available as a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=67ac8104-6d5d-458c-a546-ac82004d4567).

## :a-video: From Notebooks to Workflows {: data-length="3m44s"}

In this video, we introduce going beyond notebooks to broader structures for our Python projects.

=== "Video"

    {{ media.video('0eccb59d-2a96-440a-82eb-ac82004d0a86') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173401', 'AKrc_UfM5PLb-hc') }}

{{ media.vidtext('14-1 - From Notebooks to Workflows') }}

## :a-video: Scripts and Modules {: data-length="15m33s"}

This video introduces Python scripts and modules, and how to organize Python code outside of a notebook.

=== "Video"

    {{ media.video('3af006eb-8e58-434e-b7f7-ac8200547864') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173403', 'AA0tIVINHt7Z2GE') }}

{{ media.vidtext('14-2 - Scripts and Modules') }}

### Resources

- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [docopt](http://docopt.org/), a very useful tool for processing command-line arguments
- [Environment Variables in glossary](../../resources/glossary.md#envvar)
- [LK Demo Experiment](https://github.com/lenskit/lk-demo-experiment), which I used in the demo; this also uses DVC
- [tmux](https://github.com/tmux/tmux/wiki)

## :a-video: Introducing Git {: data-length="12m2s"}

This video introduces version control with Git.

=== "Video"

    {{ media.video('bf2603f3-2329-49b7-aafb-ac8200547812') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173404', 'ACF19qqHL2TJnCs') }}

{{ media.vidtext('14-3 - Introducing Git') }}

### Resources

- [Git Resources](../../resources/git-resources.md) (including my example `.gitignore` file)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Resources to Learn Git](https://try.github.io/)
- [Version Control by Example](https://ericsink.com/vcbe/index.html)
- [GitHub Student Developer Pack](https://education.github.com/pack)

## :a-quiz: Weekly Quiz 14

Take **Quiz 14** in Blackboard.

## :a-video: Git for Data Science {: data-length="6m52s"}

How do you use Git effectively in a data science project?

=== "Video"

    {{ media.video('501f007d-6a32-44fd-802d-ac820054783e') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173405', 'AGba4PqAto3WUCU') }}

{{ media.vidtext('14-4 - Git for Data Science') }}

### Resources

-   [NoteBook DIff and MErge (nbdime)](https://nbdime.readthedocs.io/en/latest/) — tools for diff/merge of notebooks.  Available in Conda:

        conda install nbdime

-   [git-lfs](https://git-lfs.github.com/)


## :a-video: Extract, Transform, Load {: data-length="6m46s"}

The Extract, Transform, Load (ETL) pipeline is a common design pattern for data ingest.
Sometimes it is adjusted to Extract, Load, Transform.

=== "Video"

    {{ media.video('493fed70-4eff-4fd0-9e90-ac820056c58f') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173407', 'AEmcmPne5UWF0ts') }}

{{ media.vidtext('14-5 - ETL') }}

### Resources

- [ETL — Understanding It and Effectively Using It](https://medium.com/hashmapinc/etl-understanding-it-and-effectively-using-it-f827a5b3e54d)
- [ETL vs. ELT](https://www.iri.com/blog/data-transformation2/etl-vs-elt-we-posit-you-judge/)
- [Wikipedia article on ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load)
- The [:a-video: Week 7 Example](../week7/index.md#example) uses an ELT design

## :a-video: Split, Apply, Combine {: data-length="6m45s"}

We've seen group-by operations this semester; they're a specific form of a general paradigm called *split, apply, combine*.

=== "Video"

    {{ media.video('a87c9e55-f0c3-4b93-996e-ac82005bf3f7') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173408', 'AEuwR_CdpmKJj_o') }}

{{ media.vidtext('14-6 - Split Apply Combine') }}

### Resources

- [Split, Apply, Combine at Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)

## :a-video: Tuning Hyperparameters {: data-length="10m49s"}

How can we move beyond `GridSearchCV` in our quest to tune hyperparameters?

=== "Video"

    {{ media.video('a8a2d475-1b2d-48a0-a351-ac82005bf3b2') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173409', 'ACJeAazU69nVuOI') }}

{{ media.vidtext('14-7 - Tuning Hyperparameters') }}

### Resources

- [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)
- [scikit-optimize](https://scikit-optimize.github.io/stable/)
- [BayesSearchCV example](https://scikit-optimize.github.io/stable/auto_examples/sklearn-gridsearchcv-replacement.html)

## :a-notebook: Tuning Example

The [Tuning Example](../../resources/tutorials/TuningExample.ipynb) notebook demonstrates hyperparameter tuning by cross-validation with multiple techniques.

## :a-video: Reproducible Pipelines {: data-length="8m28s"}

I provide *very brief* pointers to additional tools you may want for workflow management in more advanced projects.

=== "Video"

    {{ media.video('260993ac-f0a9-4054-ae5c-ac82005bf383') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173410', 'ADPxMcuuaI3Kv0w') }}

{{ media.vidtext('14-8 - Reproducible Pipelines') }}

### Resources

Some software that supports data and/or workflow management:

- [Data Version Control](https://dvc.org) — I use this
- [MLflow](https://mlflow.org/) — support for machine learning workflows

## :material-notebook: More Examples

My [book author gender](https://github.com/BoiseState/book-author-gender) project is an example of an advanced workflow with DVC.

## :a-assignment: Assignment 7

[Assignment 7](../../assignments/A7/index.md) is due **December 13, 2020**.
