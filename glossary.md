# Glossary

We're going to learn many terms and concepts this semester.
This page catalogs many of the important ones, with pointers to the resources in which they are introduced.

:::{glossary}

Ablation study
    A study in which we turn off different components of a complex model to see how much each one contributes to the overall model's performance.

    Introduced in {video}`week11:ablation`.

Aggregate
    A function that computes a single value from a series (or matrix) of values.
    Often used to compute a *statistic*.

    Introduced in {video}`week2:group-aggregate`.

Bayesianism
    A school of thought for statistical inference and the interpretation of probability that is concerned with using probability to quantify *uncertainty* or *coherent states of belief*.
    In statistical inference, this results in methods that quantify knowledge with probability distributions, and update those distributions based on the results of an experiment or data analysis.

    Not to be confused with {term}`Bayes' Theorem`, which is a fundamental building block of Bayesian inference but has many other uses as well.

Bayes' Theorem
    A theorem or identity in probability theory that allows us to reverse a conditional probability:

    $$P(B|A) = \frac{P(A|B) P(B)}{P(A)}$$

    Statisticians of all schools of thought make use of Bayes' theorem — all it does is relate $P(A|B)$ to $P(B|A)$, allowing us to (with additional information) reverse a conditional probability.

    Introduced in {video}`week4:joint-conditional`.

Bootstrap
    A technique for estimating sampling distributions by repeatedly resampling the available sample with replacement.

    Introduced in {video}`week4:bootstrap`.

Central limit theorem
    The theorem that describes the sampling distribution of the sample mean.
    If we take a random sample $X$ from (most) populations with mean $\mu$ and variance $\sigma^2$, the sample mean $\bar{x} \sim \mathrm{Normal}(\mu, \sigma/\sqrt{n})$.

Classification
    A problem where the goal is to predict a discrete class for an instance.
    This is often *binary classification*, where instances are categorized into one of two classes.

Conditional Probability
    The conditional probability $P(B|A)$ (read “the probability of $B$ given $A$”) is the probability of $B$, given that we know $A$ occurred.
    We can also discuss conditional expectation $\mathrm{E}[X|A]$, the expected value of $X$ for those occurrences where $A$ occurred.

    Introduced in {video}`week4:joint-conditional`.

Confidence Interval
    An interval used to estimate the precision of an estimate.
    A 95% confidence interval is an interval computed from a procedure (including both taking a sample and computing a statistic from that sample) that, when repeated, will return an interval containing the true parameter value 95% of the time.
    Discussed in {video}`week4:confidence`, [Having confidence in confidence intervals](https://medium.com/@EpiEllie/having-confidence-in-confidence-intervals-8f881712d837), and [Handbook section 1.3.5.2](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).

    A confidence interval is **not** a probabilistic statement about either the population mean $\mu$ or the sample mean $\bar{x}$.

Correlation
    The extent to which two variables change *with each other*.
    If one variable usually increases when the other one increases, the variables are *correlated*; if one decreases when the other increases, they are *anticorrelated*.

    Correlation is measured with the correlation coefficient:

    $$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2}\sqrt{\sum(y_i - \bar{y})^2}}$$

    This is equivalent to the **covariance** scaled by the standard deviations of the variables:

    $$\mathrm{Cor}(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

Degrees of Freedom
    The number of observations in a series that can independently vary to affect a calculation.
    This is usually the number of observations, minus the number of intermediate statistics.
    For example, the degrees of freedom for the sample standard deviation for $n$ observations is $n-1$, because one DoF is “used up” by the mean:

    $$s = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n - 1}}$$

Elementary Event
    In probability theory, an individual distinct outcome of a process we are modeling as random.

    Introduced in {video}`week4:probability` and [Notes on Probability](resources/probability.md).

Embedding
    As a noun, a vector-space representation of a data point or instance.
    This is often a lower-dimensional representation produced through some form of matrix decomposition such as SVD.

    As a verb, to convert an instance to such a representation.

Environment variable
    A string variable associated with a process by the operating system.
    Often used for configuring the behavior of software, such as the number of threads to use in parallel computation.
    Child processes inherit their parents' environment variables.

    Environment variables for the current process can be accessed and set in Python via the dictionary `os.environ`.

    In the Unix shell, set an environment variable with:

        export MY_VAR="contents"
    
    In PowerShell, set it with:

        $env:MY_VAR="contents"

    Set an environment variable *before* running commands that need to be governed by it.

Euclidean norm
    See {term}`L₂ Norm`.

Event
    In probability theory, an outcome that for which we want to estimate the probability.
    Formally, given a set $E$ of elementary outcomes, an event is a set $A \subseteq E$, and the set of possible events $\mathcal{F}$ forms a *sigma field*.

    Introduced in {video}`week4:probability` and [Notes on Probability](resources/probability.md).

Estimand
    An unknown quantity that we try to estimate.  See *Estimator*.

Estimate
    *n.* A value computed to approximate the value of some estimand.  See *Estimator*.
 
    *v.* The process of computing an estimate for an estimand.

Estimator
    A computation (or computed value) that we use to try to estimate an unknown value.
    Formally, an *estimator* is a computation to produce an *estimate* of an *estimand*.
    The sample mean $\bar{x}$, as an abstract concept, is an estimator of the population mean, also as an abstract concept.
    Any *particular* sample mean we compute, such as $\bar{x} = 3.2$, is an *estimate* of the population mean *for that sample*.

    Introduced in {video}`week4:introduction`.

Expected value
    The mean of a random variable $X$: $\E[X] = \sum x P(x)$ or $\E[X] = \int x p(x) dx$.

    Discussed in {video}`week4:continuous` and [Notes on Probability](resources/probability.md).

Frequentism
    A school of thought for statistical inference and the interpretation of probability that is concerned with probabilities as descriptions of the long-run behavior of a random process: how frequent would various outcomes be if the process were repeated infinitely many times?
    In statistical inference, this results in methods that are characterized by their behavior if a sampling procedure or experiment were repeated, such as confidence intervals (defined in terms of the behavior of calculating them over multiple samples) and *p*-values (the probability that a random sample would produce a statistic at least as large as the observed statistic if the sampling procedure were repeated).

Hyperparameter
    A value that controls a model's training or prediction behavior that is **not** learned from the data.
    Examples include learning rates, iteration counts, and regularization terms.

Joint Probability
    The joint probability $P(A, B)$ is the probability of both $A$ and $B$ occurring (in terms of underlying events, it's the probability that the elementary event $\zeta$ is in both $A$ and $B$).
    Equivalent to $P(A \cap B)$.
    Related to the conditional and marginal probabilities by $P(A, B) = P(A|B) P(B)$.
    Symmetric ($P(A, B) = P(B, A)$).

    Introduced in {video}`week4:joint-conditional` and [Notes on Probability](resources/probability.md).

L₁ Norm
    A measure of the magnitude of a vector, sometimes called the *Manhattan distance*.  It is the sum of the absolute values of the elements in the vector:

    $$\| \mathbf{x} \|_1 = \sum_i |x_i|$$

L₂ Norm
    A measure of the magnitude of a vector, also called the *Euclidean norm* or *Euclidean length*.  It is square root of the sum of squares of the elements in the vector:

    $$\| \mathbf{x} \|_2 = \sqrt{\sum_i x_i^2}$$

Leakage
    When your predictive model benefits from information that would not be available when the model is in actual use.
    Setting aside test data until the model is ready for final evaluation helps reduce leakage.

Linear model
    A model of the form $\hat{y} = \beta_0 + \sum_i \beta_i x_i$: it is the sum of scalar products.

    Linear models are introduced in {module}`week8`.

Logistic function
    A *sigmoid* function that maps unbounded real values to the range $(0,1)$:

    $$\mathrm{logistic}(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1}$$

    The logistic function is the invert of the logit function.

    Logistic regressions are introduced in {module}`week10`.

Logit function
    The inverse of the logistic function:

    $$\mathrm{logit(x)} = \mathrm{logistic}^{-1}(x) = \operatorname{log} \frac{x}{1-x} = \operatorname{log} x - \operatorname{log} (1-x)$$

    Applying *logit* to a probability yields the *log odds*.

Majority-class classifier
    A classifier that classifies every data point with the most common class from the training data.
    If 72% of the training data is in class A, the majority-class classifier will classify every test point as A, no matter what its input feature values are.

Marginal Probability
    The probability of a single event, or distribution of a single dimension, $P(A)$.
    Primarily used when we are talking about the probability of events (or expectation of variables) along one dimension of a *product space*, such as the suit or number of a card from a deck of playing cards.

    Described in {video}`week4:joint-conditional` and [Notes on Probability](resources/probability.md).

Matrix
    A two-dimensional array of numbers.
    Alternatively, a linear map between vector spaces.

Matrix decomposition
    A decomposition of a matrix into other matrices, such that multiplying the decomposition back together yields the original matrix or an approximation thereof.
    An example is the *singular value decomposition* (SVD):

    $$M = P \Sigma Q^T$$

    where $P \in \Reals^{m \times k}$ and $Q \in \Reals^{n \times k}$ are orthogonal, and $\Sigma \in \Reals^{k \times k}$ is diagonal.

Objective Function
    A function describing a model's performance that is used as the goal for learning its parameters.
    This can be a **loss function** (where the goal is to minimize it) or a **utility function** (which should be maximized).

    Defined in {video}:`week11:building-models`, and introduced in {video}`week9:optimizing-loss`.

Operationalization
    The mapping of a goal or question to a specific, measurable quantity (or measurement procedure).
    When we operationalize a question, we translate it into the precise computations and measurements we will use to attempt to answer it.

    Introduced in {video}`week1:asking-questions`.

Odds
    An alternative way of framing probability, as the ratio of the likelihood for or against an event:

    $$\Odds(A) = \frac{P(A)}{P(A^c)}$$

    The *log odds* is a particularly convenient way of working with odds, and is $\log P(A) - \log (1 - P(A))$.
    See the [probability notes](resources/probability.md#odds).

Odds ratio
    The ratio of the odds of two different outcomes.

    $$\operatorname{OR}(A, B) = \frac{\Odds(A)}{\Odds{B}}$$

    See the [probability notes](resources/probability.md#odds).

Overfitting
    When a model learns too much from its training data, so it cannot do an effective job of predicting future unseen data.

    Introduced in {video}`week9:overfitting`.

Parameter
    In *inferential statistics*: a “true” value in the population, such as the mean flipper length of Chinstrap penguins.
    The goal of inferential statistics is often to estimate parameters, because we typically do not have direct access to them.

    Introduced in {video}`week4:sampling`.

    In *model fitting*: a variable in a statistical or machine learning model whose value is learned from the data.
    Contrast *hyper-parameter*, a variable that controls the model or the model-fitting process but is not learned from the data.

Population
    The complete set of entities we want to study.  This is not only all entities that *do* exist, but under some philosophies, all entities that *could* exist.
    For example, the set of all possible adult Chinstrap penguins would be the population.

    Discussed in more detail in {video}`week4:sampling`.

P-value
    In hypothesis testing, the probability that the null hypothesis ($H_0$) would produce a value as large as the observed value.
    Typically the null hypothesis is an appropriate formalization of “nothing interesting”, so the *p*-value is the probability of seeing an effect as large as the one observed if there is no true effect to observe.

    Discussed in {video}`week4:hypotest`.

Regression
    A modeling or prediction problem where we try to estimate or predict a continuous variable $Y$.

    This is the focus of {module}`week8`.

Regularization
    A penalty term added to a loss function, typically penalizing large values.  Used to encourage sparsity or to require coefficients to be supported by larger quantiies of data.

    Introduced in {video}`week11:regularization`.

Residual
    The error in estimating a variable with a model.  For a model fitting an estimator $\hat{Y}$ for a variable $Y$, the residuals are $\epsilon_i = y - \hat{y}$.
    This is reflected in the full linear model: $y_i = \beta_0 + \sum_j \beta_j x_{ij} + \epsilon_i$.

    Introduced in {video}`week8:single-regression`.

Sample : n.
    A subset of the population, for which we have observations.

    Discussed in more detail in {video}`week4:sampling`.

Sample Size
    The number of items in the sample.  Often denoted $n$.

Sampling distribution
    The distribution of a statistic when it is computed over many repeated samples of the same size from the same population.
    The sampling distribution of the sample mean from a population with mean $\mu$ and variance $\sigma^2$ is $\mathrm{Normal}(\mu, \sigma/\sqrt{n})$.

Statistic
    A value computed from a set of observations.
    For example, the sample mean $\bar{x} = n^{-1} \sum_i x_i$ is a statistic of a sample $X = \langle x_i, \dots, x_n \rangle$.
    
    Discussed in {video}`week4:introduction`.

Standard deviation
    A measure of the spread of a random variable.  It is the square root of the mean squared deviation from the mean:

    $$\sigma_X = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n}}$$

    When computing the standard deviation from a sample, we instead compute the **sample standard deviation**:

    $$s = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n - 1}}$$

Standard error
    The standard deviation of the *sampling distribution* of a statistic.  The standard error of the mean (Pandas function `.sem`) is $s/\sqrt{n}$.

    Discussed in {video}`week4:confidence`.

*t*-test
    A statistical test for means of normally-distributed data.  T-tests come in three varieties:

    1. One-sample *t*-test that tests whether a single mean is different from zero (or another fixed value $\mu_0$).  $H_0: \mu=0$
    2. Two-sample independent *t*-test that tests whether the means of two independent samples are the same.  $H_0: \mu_1 = \mu_2$
    3. Paired *t*-test that tests, for a sample of paired observations, whether the mean difference between observations for each sample is zero (the measurements are, on average, the same).  $H_0: \mu_{x_{i1} - x_{i2}} = 0$

    Discussed in {video}`week4:hypotest`, {video}`week5:t-test`, and associated readings.

Variance
    A measure of the spread of a random variable (which may be observable quantities in the population).

    $$\Var(X) = \E[(X - \E[X])^2]$$

    Variance is the square of the standard deviation, and is sometimes written $\sigma^2$.

Vector
    A sequence or array of numbers; $\mathbf{x} = [x_1, x_2, \dots, x_n]$ is an $n$-dimensional vector.

Vectorization
    Writing a computation so that mathematical operations are done across entire arrays at a time, rather than looping over individual data points in Python code.

Unbiased estimator
    An estimator whose expected value is the population parameter.

:::
