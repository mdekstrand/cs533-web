# Assignment 6

:::{updated} F21
:::

This assignment is designed to develop your ability to process data sets, use scikit-learn models, and analyze their output.
You will do this by classifying, clustering, and analyzing news articles from the BBC.

This will demonstrate the following skills:

- Multi-class (more than 2 classes) classification using naïve Bayes and *k*-nearest neighbors classifiers
- Clustering with the *k*-means algorithm
- SciKit pipelines
- Dimensionality reduction with SVD and NMF

This assignment is due **midnight, {date}`wk13 sun long`**.
Upload your solution notebook and PDF export to {{LMS}}.

:::{attention}
Please pay careful attention to writing up your notebook, explaining what you are doing and *why*, and observing what we learn from the analysis.
Review the [notebook guidance](../../resources/notebook-checklist.md) for details.
:::

## SciKit-Learn Classes

There are two different text vectorizers you will need to use:

- {py:class}`sklearn.feature_extraction.text.CountVectorizer`
- {py:class}`sklearn.feature_extraction.text.TfidfVectorizer`

You can also use {py:class}`~sklearn.feature_extraction.text.CountVectorizer` with {py:class}`~sklearn.feature_extraction.text.TfidfTransformer` to get the same result as {py:class}`~sklearn.feature_extraction.text.TfidfVectorizer`.

I recommend using the vectorizer in a pipeline with your other learning class(es).

You will need to use the following classifiers and models:

- {py:class}`sklearn.naive_bayes.MultinomialNB`, the naïve Bayes classifier.
- {py:class}`sklearn.neighbors.KNeighborsClassifier`, the *k*-nearest neighbors classifier.
- {py:class}`sklearn.cluster.KMeans`, the *k*-means clustering algorithm.
- {py:class}`sklearn.decomposition.TruncatedSVD`, the dimensionality reduction algorithm.

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

{{mtodo}} Set aside 20% of the data for testing your classifiers.

{{mtodo}} Show the distribution of categories — how many articles are there in each category? Do this with a suitable plot.

## Classification (25%)

{{mtodo}} Train a naïve Bayes classifier ({py:class}`sklearn.naive_bayes.MultinomialNB`) to predict an article's category using its **term counts**.
Report its accuracy on both the training and the test data.

:::{ltip} Pipeline
You can do this in one shot with a pipeline consisting of a {py:class}`~sklearn.feature_extraction.text.CountVectorizer` followed by a {py:class}`~sklearn.naive_bayes.MultinomialNB`:

```python
bayes_pipe = Pipeline([
    ('word_count', CountVectorizer()),
    ('classify', MultinomialNB())
])
bayes_pipe.fit(train['text'], train['category'])
```
:::

{{mtodo}} Train a *k*-NN classifier ({py:class}`sklearn.neighbors.KNeighborsClassifier`) with 5 neighbors on TF-IDF term vectors.
Report its accuracy on both the training and the test data.
You can do this with a pipeline.

Remember {py:class}`~sklearn.linear_model.LogisticRegressionCV` that used cross-validation on the training data to select regularization parameters?
{py:class}`sklearn.model_selection.GridSearchCV` lets us do that for any parameters of any model.
For example:

```python
GridSearchCV(KNeighborsClassifier(), {
    'n_neighbors': [1, 2, 3, 5, 7, 10]
}, scoring=make_scorer(accuracy_score))
```

This will select the `n_neighbors` with the highest cross-validation accuracy on the training data.
The {py:func}`sklearn.metrics.make_scorer` function adapts a metric for use as a grid-search objective, and in this case we're using {py:func}`~sklearn.metrics.accuracy_score` as our metric.

{{mtodo}} Train a *k*-NN classifier with {py:class}`~sklearn.model_selection.GridSearchCV` to pick the neighborhood size.
Report its accuracy on both the training and test data.
Does tuning the neighborhood size result in better test accuracy?  What neighborhood size does the tuning select?  (You will need to explore the SciKit-Learn documentation and structure of the Python classes to determine how to extract the selected neighborhood size.)

:::{lnote} Stop words
Should you remove stop words? Are stop words useful for this classification task?
:::

## Dimensionality Reduction (15%)

We can also search for neighbors in a vector space with reduced dimension, using either {py:class}`~sklearn.decomposition.TruncatedSVD` (to compute a singular value decomposition) or {py:class}`~sklearn.decomposition.NMF` (to compute a non-negative matrix factorization).

You can use {py:class}`~sklearn.decomposition.TruncatedSVD` in a pipeline, either as the last step (so you need to call {py:meth}`~sklearn.pipeline.Pipeline.transform` on the pipeline instead of {py:meth}`~sklearn.pipeline.Pipeline.predict`), or in between your vectorizer and your classifier.
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

{{mtodo}} Plot a Seaborn {py:func}`~seaborn.pairplot` of the results of projecting the article texts with an 8-dimensional SVD, with the points colored by document class.
What do you observe?

{{mtodo}} Train a *k*-NN classifier with 5 neighbors on the SVD-transformed article texts.  You can do this with a 3-stage pipeline.
Report its accuracy on both the training and the test data.

## Summarizing Classifier Accuracy (10%)

At this point, you should have 4 different classifiers.

{{mtodo}} Show the accuracy of your 4 different classifiers on both the training and test data with an appropriate table and plot.
Which classifier design performs the best?
Which classifier seems like it may be overfitting the most in the training process?

{{mtodo}} Use {py:class}`~sklearn.model_selection.GridSearchCV` to simultaneously pick a good number of dimensions for the SVD and a good number of neighbors.
You can do this by using it to search for parameters for a pipeline.
Does optimizing your SVD improve the resulting classifier's accuracy?

## Clustering (20%)

So far our machine learning has been supervised: we have the labels. We can also do unsupervised learning, where we learn patterns from the data without labels. One such technique is clustering: putting objects (such as documents) into groups, using only the features in the documents and not using external group labels.

[K-means](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html) is a simple way of clustering a group of data points into k clusters. {py:class}`sklearn.cluster.KMeans` implements this; after training, its {py:meth}`~sklearn.cluster.KMeans.predict` method outputs cluster numbers for data points — this is how you will get the clusters.
It’s like the classifier output, except cluster numbers. The most important parameter to KMeans is the number of clusters to find — it cannot do that on its own.
It also does not match clusters to classes.

Our goal in this part is to answer the question: if we automatically cluster the news articles, do the clusters match their editor-defined categories?

We are going to explore this by showing the distribution of document categories within each clusters.  The resulting chart should be a **faceted bar chart**: one bar plot for each cluster, in which the *x* axis is the article category, and the *y* axis is the number of documents in that cluster that are in that category.

{{mtodo}} Fit a *k*-means model with 5 clusters, using TF-IDF vectors, and plot the cluster/category alignment as described above.
Do you think the clustering did a good job of finding the categories?

{{mtodo}} Repeat with 6 clusters.
Do you think this clustering does a better or worse job?  Explain why, using evidence from the plots (and if you think additional analyses would be useful, include them to support your argument).

{{mtodo}} For each cluster in the clustering you think did a better job, find the words that are most important for that cluster.
The KMeans object, after it has been fit, has a `cluster_centers_` field containing a matrix. 
There is a row for each cluster, and the columns are features (in our case, words); it says where in word-space the middle of that cluster is.
What words have the largest values for each cluster?
You can get the words with the vectorizer’s {py:meth}`~sklearn.feature_extraction.text.CountVectorizer.get_feature_names` method.
You can get a row of the matrix with `matrix[row, :]`, and use that with the feature names to make a series.
Do these words make sense in light of the documents in that cluster?

## Reflection (10%)

{{mtodo}} Write 2–3 paragraphs about what you learned from this assignment.
Please be specific — I would like you to reflect on particular things you learned about text classification or clustering, or about this data, and not just say general things about learning about text.
What surprised you in this project?

## Time Estimate

If, through A5 and the exercises, you have become proficient at building and running SciKit-Learn pipelines, I expect this assignment will not be as fiddly as some previous ones, and will hopefully take somewhat less time.

1.  Data prep: 1 hour
2.  Classification: 2 hours
3.  Dimensionality reduction: 1 hour
4.  Summarizing Accuracy: 30 minutes
5.  Clustering: 2 hours
6.  Reflection: 30 minutes
