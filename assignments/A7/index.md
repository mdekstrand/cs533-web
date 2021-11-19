# 🚧 Assignment 7 🚧

:::{draft}
This assignment is still in draft state.
:::

This assignment is designed for you to practice the things that we've put together this semester, along with extracting data directly from an online API and splitting a data pipeline into multiple stages with scripts acquiring and pre-processing data.

It is due on **{date}`wk15 sun xlong`** at the end of the day.

For this assignment, you will submit a **GitHub repository** along with PDF(s) of your analyses.
It is also an open-ended assignment in terms of research questions — I will guide you through obtaining data, but not through the analysis itself.

In this assignment, you will:

1.  Integrate the MovieLens 25M data set with data from TMDB
2.  Carry out a basic descriptive analysis of your data and the variables you are preparing for use in your analysis
3.  Define and address 2 modest questions from this data

**Please read the entire assignment before beginning** — the last section describes what you should have in a complete assignment submission.

## Online Accounts

In order to complete this assignment, you will need accounts with two online services:

- [TMDB](https://www.themoviedb.org/) (The Movie DataBase), to obtain movie data.
- [GitHub](https://github.org), to share a git repository.

Once you have created your TMDb account, you need to create an application to obtain an API key.
Go to “Edit Profile” (in the menu when you click your profile picture in the top right), select “API”, and click “Create”.
You want to create a Developer application; on the following form, under Application Type, choose “Education”.
If you don't want to give them your own address, you can use the department's address (1910 University Drive, Boise, ID 83725-7055).

## Data Access

You are going to obtain data from at least two sources:

-   The [MovieLens 25M data set](https://grouplens.org/datasets/movielens/25m/) ­— this will take just over 1GB uncompressed.
    It is a lot like the HETREC data we have been using, except it is in a consistent CSV format and there is a lot more of it.
    It doesn't have all the fields from HETREC, though - it's just very basic metadata along with many user ratings.
-   The TMDB API, for example the [Movie Details endpoint](https://developers.themoviedb.org/3/movies/get-movie-details).
    This will allow you to fill in a lot more kinds of data, like we had in HETREC.

The ML-25M data set includes a file `links.csv` that includes TMDB and IMDB identifiers for the movies in MovieLens.
You can use this to integrate data between MovieLens and other data sources.

The TMDB API is accessed through an HTTP REST API.
The Python [Requests library](https://requests.readthedocs.io/en/master/user/quickstart/) is a very good library for accessing data sources like this.

If you have stored your API key in the variable `TMDB_KEY`, and you have a set of TMDB identifiers in the sequence `tmdb_ids` (this can be a list, or a Pandas series, or a NumPy array, or whatever), you can fetch their TMDB details with:

```python
tmdb_details = []
for mid in tmdb_ids:
    res = requests.get(f'https://api.themoviedb.org/3/movie/{mid}',
                       params={'api_key': TMDB_KEY})
    tmdb_details.append(res.json())
tmdb_details = pd.DataFrame.from_records(tmdb_details)
```

If you want to index by TMDB ID, you can use `tmdb_details.set_index('id')`.

:::{ltip} Progress Bar

If you want a progress bar, you can import TDQM:

```python
from tqdm.auto import tqdm
```

And then use it in your loop:

```python
tmdb_details = []
for mid in tqdm(tmdb_ids):
    res = requests.get(f'https://api.themoviedb.org/3/movie/{mid}',
                        params={'api_key': TMDB_KEY})
    tmdb_details.append(res.json())
```
:::

The [Movie Details endpoint documentation](https://developers.themoviedb.org/3/movies/get-movie-details) describes the fields that you will find in these objects.
TMDB also has several other endpoints you can query to obtain information about actors, directors, TV show episodes, etc.
You may need to query more than just the movie details for your research questions!
Browse their documentation to see more.
All of the read-only movie data endpoints are called in the same way, they just change the URL (and possibly the parameters) that you need to query with `requests`.

### Data Scripts

For this assignment, you need to create one (or more) Python *scripts* (see Week 14) that process the data and retrieve the TMDB data that you need.
They should write the results of the data out to CSV or Parquet files, so the notebooks answering your questions can read pre-integrated data.

I do not recommend that you fetch the TMDB data for **all** the movies, at least when you are first testing.
Pick movies somehow, such as a random sample, or prioritizing more popular movies.
Test your code with small numbers of movies (e.g 100), before running a run on the entire data set you are going to use.

### Saving Memory

If you want to reduce the memory consumption of processing the rating data, you can use `dtype`:

```python
ratings = pd.read_csv('ml-25m/ratings.csv', dtype={
    'movieId': 'i4',
    'userId': 'i4',
    'rating': 'f4',
    'timestamp': 'i4'
})
```

## Research Questions

For this assignment, you need to specify and answer **two** concrete research questions of your own choosing from the available data.
They can be any kind of analysis we have studied, including:

* Correlations
* Inference with regression models
* Predicting continuous or categorical outcomes

**At least one** question must involve using the MovieLens and TMDB data together.

I encourage you to be modest in the scope you target for your research questions — simple, well-executed questions with good insights are better than complex questions that are poorly executed.
For questions with outcome variables, you need to include include at least two potential predictors for its outcome variable (e.g. trying two predictors in a regression, or a correlation analysis that compares the outcome with at least two different variables).
Particularly interesting and well-defined questions with a single predictor are acceptable — if in doubt, raise your question by Piazza or in office hours to get feedback on its scope.
Grading will be based primarily on the quality of the execution and presentation of the question, not on scope, so slightly under-scoped but well-executed questions will receive nearly full points.

:::{tip}
TMDB provides quite a few data points you can use:

* Movie staff: actors, producers, directors, etc.
* Production locations
* Financial data (budget and revenue)

And many more.

For example, one potential research question you could ask is: does receiving many ratings in MovieLens predict whether a movie will be profitable?
This question can be extended to: can the average of the ratings a movie receives in its first week on MovieLens predict its profitability?

You are allowed to use this as one of your questions 🙂.
Answering both of these question variants together is a fine scope for one question.
:::

## Repository Format

Your work needs to be in a Git repository, with the following pieces:

1.  A file called `README.md` that describes the repository: what are the scripts and notebooks, what do they do, and in what order do they need to be run.
2.  Your data processing script(s).
3.  Notebooks answering your research questions. Each question should be in its own notebook.
4.  `.gitignore` file(s) that ignore your data files (ML data, outputs from data scripts, etc.)
    See [Git Resources](../../resources/git-resources.md) for a start here.

### Notebook Requirements

The notebooks should not do any data integration or preliminary data cleaning (dropping invalid records, clearing out invalid values, etc.).
They may do *question-specific* data cleaning, and handling of missing data (as I have encouraged you to handle missing data as late in an analysis as possible), but general data cleaning and integration should be in separate scripts.

Each notebook should include a brief descriptive analysis of the variables it is studying.
Describe the variables and their distributions, and any limitations their sources may have on your analysis.

## Final Submission

Your submission on {{LMS}} should include:

- A link to a **private** GitHub repository containing your code
- PDF exports of your two notebooks

In addition, invite my GitHub account ([mdekstrand](https://github.com/mdekstrand)) as a collaborator on your repository, so I can actually see it.
I only need read access.
You can invite me through the “Manage access” section of your repository settings.

### Rubric

I will use the normal assignment rubric, with points assigned as follows:

-   Repository construction and layout (15%)
-   README (15%)
-   Data processing (20%)
-   Research Question 1 (25%)
-   Research Question 2 (25%)

If you successfully use a third source of data (in addition to MovieLens and TMDB), it may earn extra credit.
Document this data in your README.
(This needs to be a third distinct source — using additional TMDB endpoints doesn't count.)
