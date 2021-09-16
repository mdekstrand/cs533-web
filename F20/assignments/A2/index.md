# Assignment 2

The purpose of Assignment 2 is to practice data processing, visualization, and
inference using the [HETREC Movie](https://grouplens.org/datasets/hetrec-2011/)
data we have been using for examples in class.

It is due **September 27, 2020** at the end of the day (11:59 PM). Submit your `.ipynb` and PDF files to Blackboard.

## Revision Log

September 22, 2020
:   Corrected *Comparing Ratings* to talk about Rating instead of Score.

September 21, 2020
:   Corrected to talk about 20 genres instead of 10
:   Added note about NAN policy

## Data and Setup (25%)

For this assignment, you will work with the [HETREC Movie data](https://grouplens.org/datasets/hetrec-2011/).

Consult the work from class and the tutorial notebooks for code to load the data, and many hints!

Pay attention to the [Missing Data](../../resources/tutorials/MissingData.ipynb) notebook for handling missing data.
**Use the strategies in that notebook to replace the '0's used to encode unknown RottenTomatoes ratings with missing (NA) values.**

:material-check-circle: Set up your notebook to load the data, convert erroneous 0s to NAs, and show the size & columns of your data set.

## Comparing Ratings (30%)

:material-check-circle: **Describe the distributions** of the RottenTomatoes critic ratings (All Critics and Top Critics), the Audience Rating, and the mean rating given to a movie by MovieLens users, both numerically and graphically.

:material-check-circle: **Describe the distribution** of the *difference* between the All Critics and Top Critics ratings for movies where both are defined, both numerically and graphically.

:material-check-circle: Answer the following questions using **paired T-tests** (the SciPy `ttest_rel` function computes this):

- Do the data indicate a difference between the ratings given to movies by all critics and those given by top critics?
- Do the data indicate a difference between the average audience rating RottenTomatoes users give to a movie and the mean rating MovieLens users give to it?

Consider: why is the paired t-test the appropriate test here?

!!! tip "Missing Data"

    The SciPy test functions have an `nan_policy` function, and if you pass `nan_policy='omit'` they will ignore missing values instead of propagating them into NaN results.  I recommend doing this, and also dropping NAs in your bootstraps.

## Confidence Intervals (25%)

We now want to see if some genres of movies fare better with critics than others.

:material-check-circle: For each of the 20 genres, compute the mean and a 95% confidence interval for the all-critic scores using the standard error method.
Show the results as a data frame sorted by decreasing mean (look up the `sort_values` method in Pandas).
Does it look like the top two genres have different mean critic scores? Does it look like the top and bottom genres have different mean critic scores?
Defend your answers using the confidence intervals.

!!! tip "Vectorization"

    You can do all of this with vectorized operations. Start with a frame whose rows are genres, and whose columns are the mean, count, and standard deviation (and/or SEM, standard error of the mean) of the all-critic scores for movies in that genre.  That will let you compute all the confidence intervals in just a handful of Python operations.

!!! tip "Joining"

    If you join or merge the movie genre table with your movie info or stats table on the movie ID, it will **duplicate** each movie for each genre it has.  Grouping by genres and aggregating will then compute your aggregate statistics, such as the mean, correctly.

:material-check-circle: For each of the 20 genres, compute the mean and a 95% bootstrapped confidence interval for the mean all-critic score.
Show the result in a table.  Does this look the same as the standard error CIs?

!!! tip "Group-Apply"

    Remember the group-apply we saw in [Penguin Inference](../../resources/tutorials/PenguinSamples.ipynb)?  That will help here too!  You can bootstrap inside the function instead of computing an error-based confidence interval.

!!! note "Independence"

    These groups are *not* indepednent. We can compute confidence intervals, but making group comparisons require more care.

## Popularity and Bootstraps (20%)

Action movies are most likely more popular than documentaries.  By this I mean that more people are likely to watch an action movie than a documentary.

Compute the number of MovieLens users who have rated each movie.  This will yield observations of *movies* and their *number of ratings*.

:material-check-circle: Test the null hypothesis that action movies and documentaries have the same *median number of ratings* using a bootstrapped *p*-value.  Does your test accept or reject the null? What *are* the median number of ratings for movies in each of these genres?

What if you use the # of audience ratings from RottenTomatoes instead of the # of MovieLens ratings?

!!! tip "Bootstrapping the Test"

    This will use the same technique as we used in [Penguins](../../resources/tutorials/PenguinSamples.ipynb) to bootstrap a test for different means.

:material-check-circle: Compare the mean of the critic ratings (using the All Critics ratings from Rotten Tomatoes) between action and documentary movies. Is there a difference? Test the difference with both the bootstrap and an approprate *t*-test.
