# Assignment 1

This assignment is to give you experience with exploratory analysis and describing a data set.

It is due on **Sunday, September 12, 2020** at the end of the day (11:59 PM).
Submit your `.ipynb` and PDF files to {{LMS}}.

:::{tip}
I recommend reading through the whole assignment before beginning. I begin this assignment
with a discussion of the goal, and some discussion of the specific variables you will need to use to
address that goal, and then have the specific requirements for the assignment.

In writing requirements, I often write such that the first sentence of a paragraph or requirement is
the high-level idea of that requirement, and the subsequent sentences (and possibly additional paragraphs or
bullet points) dive in to the details of what is expected for that requirement.
:::

## Revision Log

-   **Sep. 7, 2021** - corrected mention of nonexistence Pandas function “recode”, and clarified the hint.
    Clarified the hint about consulting the [📓 Building Data notebook](../../resources/tutorials/BuildingData.ipynb)
    for working with admissions policies.
    No requirements changes.

## Learning Outcomes

This assignment is designed to develop and assess your ability to:

1. Obtain a data set from a public source, and use its documentation to understand it
2. Set up a Jupyter notebook and data set to begin a new analysis
3. Carry out an exploratory analysis to understand a data set’s contents and communicate them to others.

Because of LO2, I will not be providing a notebook. You need to create your own notebook file.

To advance LO1, there are details you will need to obtain from the documentation that comes with the data.

For this assignment, you will need material through weeks 3, and the [tutorial notebooks](../../resources/tutorials/index.md).

## Context and Data

For this assignment, you will work with the data set underlying the Department of Education’s [College Scorecard](https://collegescorecard.ed.gov/data/).

This is a medium-sized data set. For this assignment, we will only work with the most recent cohort’s data.

On this site, you will find a few things:

-   The data itself.  We want “Most Recent Institution-Level Data”
-   The documentation.  Of particular note:
    - The Data Dictionary contains concise definitions of key fields
    - The Technical Documentation for Institution-Level Data Files contains more thorough discussion of the different variables, and on pages 33–37 describes where the data came from and how was collected.

The lack of direct links is deliberate.
I want you to navigate the site yourself to find the relevant files, so you gain experience collecting information about a data set.

We are primarily interested in understanding *completion rates* and the distribution of various variables that describe the type of school.
Consult the dictionary and documentation for how to get this!

:::{tip}
Excel or LibreOffice Calc is useful for viewing the CSV data file such that you can scroll back and forth.
You can also view column names with `schools.columns`, if you have loaded it into a Pandas data frame stored in the variable `schools`.
:::

## Question

Our analysis is motivated by the following question:

:::{admonition} Overall Question
:class: question

How do completion rates differ for different types of students and different types of schools?
:::

We want to look at this by:

- Student race
- Admission policy and rate
- Public/private status (the documentation describes this as “control” — what is the legal or financial control status of the school?)

:::{admonition} Significance
We do not have the statistical tools yet to assess the *significance* of any differences we may observe between completion rates.
We will learn that in Week 4, and one of the self-study practice exercises that week will be to go back to this assignment and more accurately measure the differences.
Our purpose here is just to observe the differences in the data, without testing whether they are “real” effects or not.
:::

## Notes on Variables

This section describes considerations for some of the variables you need to work with.
You will need to consult the documentation — these provide guidance on *how* to apply the documentation.

### Notes on Multiple Variables

Page 21 and following of the technical documentation describe the completion rate statistics.
There are several different variables for recording completion rates, broken down in a few ways:

- Completion within 100% or 150% of expected time (for a 4-year school, this is 4 or 6 years)
- Both pooled and unpooled versions are available
- 4-year and less-than-4-year schools report outcomes with different sets of variables
- Overall completion rate and rates broken down by race

You will need to compare the variable names available in your data with the description in the documentation to correctly understand how the data is laid out.

For the 4/L4 distinction (4-year vs. less-than-4-year), are any schools in both categories?  If not, does it make sense to combine two variables into one completion rate variable?  The {py:meth}`pandas.Series.combine_first` method will combine two series.  To fill in the missing values in `s1` with values from `s2`, do:

    s1.combine_first(s2)

The [Missing Data notebook](../../resources/tutorials/MissingData.ipynb) provides hints for working with missing values in general.

:::{tip}
If you know SQL, Pandas `combine_first` works like SQL `COALESCE`.
:::

For the other options (pooling, 100/150%), read the documentation about completion rates, and pick the variables to use.  **Justify your decision.**

:::{admonition} Selecting Variables
:class: tip

If we want to look at completion rate by race, and want our analysis to be self-consistent, what implications does that have for our choice of completion rate variables?
:::

### Notes on Admission

Pages 10–11 describe admissions data.  There are two variables that describe the admissions practices. First, whether it has an open admissions policy.
Second, schools that do not have an open admissions policy report the admission rate.

Since we don't yet have the tools to examine relationships between numeric variables, we're going to *bucketize* the admissions policy.
Define three categories of schools:

- Open-admission schools
- Low-selectivity schools, where the admission rate is *higher* than the median admission rate
- High-selectivity schools, where the admission rate is *lower* than the median admission rate

:::{admonition} Difference from Database Terminology
:class: warning

If you have taken a database class, note that the definitions of selectivity here are the *reverse* from the way the term is used in databases.  In database terminology, a “highly selective” condition is one that selects many rows, but in higher education, “highly selective” means it does *not* select many of its applicants.
:::

:::{admonition} Tutorial Notebooks
:class: tip

The [Building Data](../../resources/tutorials/BuildingData.ipynb) notebook provides useful hints for this part of the assignment.
In particular, pay attention to the “Building Up” subsection.
:::

## Assignment Requirements

Submit a Jupyter notebook that describes the following (grade percentages and estimated times are in parentheses):

1.  A basic structural description of the data set (10%):
    -   How many schools and variables?
    -   How many schools are there per state?
    -   How are schools-per-state distributed?  Compute a state-level variable '# of schools', and describe its distribution numerically and visually.

2.  The distribution of the overall completion rate (15%):
    -   Provide choice of completion rate variable with a justification for that choice.
    -   Describe the distribution of that variable numerically and visually.
    -   What is the mean?  Is the distribution skewed?

3.  The distribution of the admission rate, both numerically and graphically (15%).
    After describing the distribution of the continuous admission rate, compute the admissions category (open, low-selectivity, or high-selectivity).
    Do **not** hard-code the median — compute the median, and use the computed value (stored in a Python variable) to bucketize the admission rates.
    Show the distribution of admissions category (how many schools are in each category?).

4.  The break down (sometimes called a {term}`disaggregation`) of completion rate by race, by the school
    characteristics described in “Question”, and by one additional school characteristic you select
    (30%). Give a justification for your choice of additional characteristic — why do you think it might be
    interesting?

    You need to show these breakdowns both numerically and graphically.
    Box plots are useful for this, as are bar charts.

    *   Race is a per-student characteristic; schools report completion rate separately for each racial category, in addition to the overall completion rate.
        The resulting chart should have one bar or box for each racial group.
    *   The other characteristics — selectivity, public/private status, and your chosen additional one — are per-school statistics.
        The resulting chart should have one box or bar for each value of the chosen characteristic (e.g. for selectivity, these are open, low, and high).

    Describe differences you see, with references to specific features in the charts.
    What kinds of schools seem to be doing the best in terms of getting students to completion?

    :::{tip}
    Race is recorded as multiple variables per school, but it is difficult to directly pass data in this form to one of the plotting routines.
    The {py:meth}`pandas.DataFrame.melt` method is really useful for this — it can take the various race completion rate columns and pivot them into *long* format, where there's a column for the variable name and another for the value.
    You can then “recode” the name variable to change the names used for its levels, and then you can e.g. use the name variable for an axis in your chart, or group by it!

    There at least three good ways to recode such a variable:

    -   Convert it to a categorical data type, and use {py:meth}`pandas.Series.cat.rename_categories`.
    -   Treat it as a string, and use {py:meth}`pandas.Series.str.replace` to adjust the strings to be more readable values with a regular expression.
    -   Create a new series with the desired values (see the [📓 Building Data notebook](../../resources/tutorials/BuildingData.ipynb))
    :::

5.  The answers to 5 questions of your choice from sections 3.1, 3.2, and 3.3 of {reading}`week2:datasheets`, based on the documentation for the college scorecard data (20%).
    Questions should come from at least 2 different sections of the paper.

7.  Write 2 paragraphs reflecting on what you learned about this data, higher education, and data science through this assignment (10%).

Submit the final assignment (both `.ipynb` and `.pdf` files) to {{LMS}}.

## Extra Credit

Look at differences in completion rates by race for schools with different characteristics.
Do some kinds of schools seem to do better at racial equality in completion rates than others?

## Notebook Notes & Requirements

**Structure your notebook well.** Use heading levels, in a suitable order.

**Read your notebook.** Do you find it pleasant to read?

**Describe your work.** Use Markdown cells to explain why we are doing different analyses, and what we learn from them. When using a data set variable, explain what the variable means, because they have cryptic names.

The [Notebook Checklist](../../resources/notebook-checklist.md) will help you correctly format your
notebook. This assignment is graded using the [general rubric](asn-rubric), and the difference
between *Basically Correct* (95%) and *Exemplary* (100%) is primarily in the quality and clarity of your
presentation.


## Time Estimate

I've tried to estimate about how long I expect each of the components of the assignment to take.
These numbers are aimed to target about the 80th %ile of how long it would take the students in this
class, but I admit it's just my best guess. My hope is that it helps you calibrate your work and
expectations.  If you have feedback on how accurate these estimates are, I encourage you to include
that in your reflection in your notebook.

1. Load data and structural description: 1 hour
2. Distribution of completion rate: 30 minutes
3. Distribution and discretization of admission rate: 1 hour
4. Completion rate breakdown: 2 hours
5. Datasheets answers: 1–2 hours
6. Cleaning up presentation & writing reflection: 1 hour
