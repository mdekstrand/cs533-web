# Assignment 6

This assignment is designed to develop your ability to process data sets, use scikit-learn models, and analyze their output.
You will do this by classifying, clustering, and analyzing news articles from the BBC.

This will demonstrate the following skills:

- Multi-class (more than 2 classes) classification using naïve Bayes and *k*-nearest neighbors classifiers
- Clustering with the *k*-means algorithm
- SciKit pipelines
- Dimensionality reduction with SVD and NMF

This assignment is due **midnight, November 22, 2020**.
Upload your solution notebook and PDF export to Blackboard.

[TOC]

## Revision Log

November 21, 2020
:   Correct missing `make_scorer` call in `GridSearchCV` snippet.

November 17, 2020
:   Added encoding to reading files
:   Fixed typo in SVD example code
:   Added note about removing stop words

November 16, 2020
:   Fixed typo in `MultinomialNB` code.

## SciKit-Learn Classes

There are two different text vectorizers you will need to use:

- [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer)
- [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer)

You can also use `CountVectorizer` with `TfidfTransformer` to get the same result as `TfidfVectorizer`.

I recommend using the vectorizer in a pipeline with your other learning class(es).

You will need to use the following classifiers and models:

- [`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB), the naïve Bayes classifier.
- [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier), the *k*-nearest neighbors classifier.
- [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans), the *k*-means clustering algorithm.
- [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD), the dimensionality reduction algorithm.

## Load and Prepare Data (20%)

Download the Raw text files for the main ‘BBC’ data set from <http://mlg.ucd.ie/datasets/bbc.html>.
This will be a Zip file that contains text files with data.

You can read the files into a Pandas data frame with the following code:

```python
from pathlib import Path
articles = pd.DataFrame.from_records(
    ((f.parent.name, f.name, f.read_text(encoding='latin1'))
     for f in Path('bbc').glob('*/*.txt')),
    columns=['category', 'file', 'text']
)
```

This loops over all text files and reads them into records, that you then turn into a Pandas data frame.

:a-task: Set aside 20% of the data for testing your classifiers.

:a-task: Show the distribution of categories - how many articles are there in each category? Do this with a suitable plot.

## Classification (25%)

:a-task: Train a naïve Bayes classifier ([`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB)) to predict an article's category using its **term counts**.
Report its accuracy on both the training and the test data.

!!! tip Pipeline

    You can do this in one shot with a pipeline consisting of a `CountVectorizer` followed by a `MultinomialNB`:

    ```python
    bayes_pipe = Pipeline([
        ('word_count', CountVectorizer()),
        ('classify', MultinomialNB())
    ])
    bayes_pipe.fit(train['text'], train['category'])
    ```

:a-task: Train a *k*-NN classifier (`KNeighborsClassifier`) with 5 neighbors on TF-IDF term vectors.
Report its accuracy on both the training and the test data.
You can do this with a pipeline.

Remember `LogisticRegressionCV` that used cross-validation on the training data to select regularization parameters?
[`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV) lets us do that for any parameters of any model.
For example:

```python
GridSearchCV(KNeighborsClassifier(), {
    'n_neighbors': [1, 2, 3, 5, 7, 10]
}, scoring=make_scorer(accuracy_score))
```

This will select the `n_neighbors` with the highest cross-validation accuracy on the training data.

:a-task: Train a *k*-NN classifier with `GridSearchCV` to pick the neighborhood size.
Report its accuracy on both the training and test data.
Does tuning the neighborhood size result in better test accuracy?

!!! note Stop words

    Should you remove stop words? Are stop words useful for this classification task?

## Dimensionality Reduction (15%)

We can also search for neighbors in a vector space with reduced dimension, using either `TruncatedSVD` (to compute a singular value decomposition) or `NMF` (to compute a non-negative matrix factorization).

You can use `TruncatedSVD` in a pipeline, either as the last step (so you need to call `transform(X)` on the pipeline instead of `predict`), or in between your vectorizer and your classifier.
The `transform(X)` method will return a matrix where the rows correspond to your data points, and the columns correspond to your reduced-dimension features.
So, if you want to get some reduced-dimension representations of texts, you can do:

```python
svd_pipe = Pipeline([
    ('word_vec', TfidfVectorizer()),
    ('svd', TruncatedSVD(8))
])
svd_pipe.fit(train['text'])
text_vectors = svd_pipe.transform(train['text'])
```

:a-task: Plot a Seaborn pairplot of the results of projecting the article texts with an 8-dimensional SVD, with the points colored by document class.
What do you observe?

:a-task: Train a *k*-NN classifier with 5 neighbors on the SVD-transformed article texts.  You can do this with a 3-stage pipeline.
Report its accuracy on both the training and the test data.

## Summarizing Classifier Accuracy (10%)

At this point, you should have 4 different classifiers.

:a-task: Show the accuracy of your 4 different classifiers on both the training and test data with an appropriate table and plot.
Which classifier design performs the best?
Which classifier seems to overfit the most in the training process?

## Clustering (20%)

So far our machine learning has been supervised: we have the labels. We can also do unsupervised learning, where we learn patterns from the data without labels. One such technique is clustering: putting objects (such as documents) into groups, using only the features in the documents and not using external group labels.

[K-means](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html) is a simple way of clustering a group of data points into k clusters. `KMeans` in scikit-learn implements this; after training, its `predict()` method outputs cluster numbers for data points - this is how you will get the clusters.
It’s like the classifier output, except cluster numbers. The most important parameter to KMeans is the number of clusters to find - it cannot do that on its own.
It also does not match clusters to classes.

Our goal in this part is to answer the question: if we automatically cluster the news articles, do the clusters match their editor-defined categories?

We are going to explore this by showing the distribution of document categories within each clusters.  The resulting chart should be a **faceted bar chart**: one bar plot for each cluster, in which the *x* axis is the article category, and the *y* axis is the number of documents in that cluster that are in that category.

:a-task: Fit a *k*-means model with 5 clusters, using TF-IDF vectors, and plot the cluster/category alignment as described above.
Do you think the clustering did a good job of finding the categories?

:a-task: Repeat with 6 clusters.
Do you think this clustering does a better or worse job?  Explain why, using evidence from the plots (and if you think additional analyses would be useful, include them to support your argument).

:a-task: For each cluster in the clustering you think did a better job, find the words that are most important for that cluster.
The KMeans object, after it has been fit, has a `cluster_centers_` field containing a matrix. 
There is a row for each cluster, and the columns are features (in our case, words); it says where in word-space the middle of that cluster is.
What words have the largest values for each cluster?
You can get the words with the vectorizer’s `get_feature_names()` method.
You can get a row of the matrix with `matrix[row, :]`, and use that with the feature names to make a series.
Do these words make sense in light of the documents in that cluster?

## Reflection (10%)

:a-task: Write 2–3 paragraphs about what you learned from this assignment.
Please be specific — I would like you to reflect on particular things you learned about text classification or clustering, or about this data, and not just say general things about learning about text.
What surprised you in this project?

## Extra Credit (5%)

:a-task: Use `GridSearchCV` to simultaneously pick a good number of dimensions for the SVD and a good number of neighbors.
You can do this by using it to search for parameters for a pipeline.
Does optimizing your SVD improve the resulting classifier's accuracy?

:a-task: `NMF` provides another strategy for matrix factorization.
Apply it to count vectors (not TF-IDF vectors) as input to *k*-NN, and grid-search resulting classifier's settings.
How does it compare to using SVD for classifying articles?

## Time Estimate

1.  Data prep: 1 hour
2.  Classification: 2 hours
3.  Dimensionality reduction: 1 hour
4.  Summarizing Accuracy: 30 minutes
5.  Clustering: 2 hours
6.  Reflection: 30 minutes
