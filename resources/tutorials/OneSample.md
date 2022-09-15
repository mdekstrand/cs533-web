---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# One Sample

This notebook demonstrates the one-sample *t*-test and checking normality with a Q-Q plot, using the [ZARR13.DAT](https://www.itl.nist.gov/div898/handbook/eda/section4/eda4281.htm) file from the *NIST e-Handbook of Statistical Methods*.


## Setup

Import our Python modules:

```python
import pandas as pd
import numpy as np
import scipy.stats as sps
import statsmodels.api as sm
import matplotlib.pyplot as plt
```

Read the [ZARR13.DAT](https://www.itl.nist.gov/div898/handbook/datasets/ZARR13.DAT) file:

```python
data = pd.read_table('ZARR13.DAT', skiprows=25, names=['X'])
data
```

## Showing the Distribution

Let's look at histogram:

```python
plt.hist(data.X, bins=20)
plt.show()
```

And the distribution statistics:

```python
data.X.describe()
```

### Q-Q Plot

The data looks normal-ish, but a histogram isn't a very reliable way to assess normality.  A Q-Q plot against the normal distribution lets us be much more precise:

```python
sm.qqplot(data.X, fit=True, line='45')
plt.show()
```

That data looks normal!  It's a straight line right through the bulk of the data. It's common for the first and last few points to deviate from normal just a little bit more than the central mass of data points.


### Drawing Q-Q Ourselves

Let's try to draw our own.  The way we draw a Q-Q plot is this:

1. Sort the data values in ascending order.  These will be plotted on the *y* axis.
2. Compute the percentile for each data point - where is it in the range of data points?  We can do this with its position or count.  We don't label any point 0 or 1; instead, for point $i \in [1,n]$, we compute $v = i / (n + 1)$.
3. Compute the quantiles in the reference distribution (in our case, normal) for each data point position.  These will be plotted on the *x* axis.

Let's sort:

```python
observed = data['X'].sort_values()
```

Now we need to compute the percentiles for each position.  The [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) function is useful for this - it can generate $i = 1 \dots n$, and we can divide to rescale the points:

```python
nobs = len(observed)
pred_ps = np.arange(1, nobs + 1) / (nobs + 1)
```

And we need to convert these percentiles into quantile values from the standard normal:

```python
norm_dist = sps.norm()
pred_vs = norm_dist.ppf(pred_ps)
```

Finally, we can plot them against each other:

```python
plt.scatter(pred_vs, observed)
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()
```

We can see the straight line, but two issues remain:

1. Our sample quantiles are on the original scale, but theoretical are standardized. Let's standardize the sample quantiles so the values, not just relative shape, are comparable.
2. We don't have the refernce line. This will be easier to draw with standardized sample quantiles.

**{term}`Standardization`**, for normally-distributed data, is transforming it to have a mean of 0 and standard deviation of 1.  We do this by subtracting the mean and dividing by the sample standard deviation:

```python
std_observed = (observed - observed.mean()) / observed.std()
# reference values; once standardized, the line will be y=x
ref_xs = np.linspace(np.min(pred_vs), np.max(pred_vs), 1000)
plt.plot(ref_xs, ref_xs, color='red')

# add the points
plt.scatter(pred_vs, std_observed)

# and labels
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()
```

## T-tests

Let's start with a 1-sample T-test for $H_0: \mu = 9$:

```python
sps.ttest_1samp(data.X, 9)
```

If $\mu$ were nine, it would be extremely unlikely to find a sample with this observed mean.

These values are very tightly distributed.  A 1-sample T-test for $H_0: \mu = 9.25$:

```python
sps.ttest_1samp(data.X, 9.25)
```

Our data would also be very unlikely, but not *as* unlikely, under this null hypothesis.

And just to see it accept the null, let's try $H_0: \mu = 9.26$:

```python
sps.ttest_1samp(data.X, 9.26)
```

Our data is consistent with $\mu=9.26$.

**Note:** What I just did here — try several different null hypotheses in a row — is **not a valid statistical procedure**.  I am only doing it to demonstrate the results of a *t*-test both when the null hypothesis holds, and when it does not.
