# Glossary

We're going to learn many terms and concepts this semester.
This page catalogs many of the important ones, with pointers to the resources in which they are introduced.

:::{glossary}

ablation study
    A study in which we turn off different components of a complex model to see how much each one contributes to the overall model's performance.

    Introduced in {video}`week11:ablation`.

aggregate
    A function that computes a single value from a series (or matrix) of values.
    Often used to compute a {term}`statistic`.

    Introduced in {video}`week2:group-aggregate`.

aleatoric uncertainty
    Uncertainty that arises due to inherent randomness, such that further information will not make us more certain.
    Contrast {term}`epistemic uncertainty`.

arithmetic mean
    The most common type of {term}`mean`, computed from a sequence of observations as $\bar{x} = \frac{1}{n} \sum_i x_i$.
    When using the term “mean” without an additional qualifier, this is the type of mean we mean.

Bayesianism
    A school of thought for statistical inference and the interpretation of probability that is concerned with using probability to quantify *uncertainty* or *coherent states of belief*.
    In statistical inference, this results in methods that quantify knowledge with probability distributions, and update those distributions based on the results of an experiment or data analysis.

    Not to be confused with {term}`Bayes' Theorem`, which is a fundamental building block of Bayesian inference but has many other uses as well.

Bayes' theorem
    A theorem or identity in probability theory that allows us to reverse a {term}`conditional probability`:

    $$\P[B|A] = \frac{\P[A|B] \P[B]}{\P[A]}$$

    Statisticians of all schools of thought make use of Bayes' theorem — all it does is relate $\P[A|B]$ to $\P[B|A]$, allowing us to (with additional information) reverse a conditional probability.

    Introduced in {video}`week4:joint-conditional`.

bootstrap
    A technique for estimating sampling distributions by repeatedly resampling the available sample with replacement.

    Introduced in {video}`week4:bootstrap`.

central limit theorem
    The theorem that describes the sampling distribution of the sample mean.
    If we take a random sample $X$ from (most) populations with mean $\mu$ and variance $\sigma^2$, the sample mean $\bar{x} \sim \mathrm{Normal}(\mu, \sigma/\sqrt{n})$.

classification
    A {term}`supervised learning` problem where the goal is to predict a discrete class for an instance.
    This is often *binary classification*, where instances are categorized into one of two classes.

    This is the major topic of {module}`week10`.

conditional probability
    The conditional probability $\P[B|A]$ (read “the probability of $B$ given $A$”) is the probability of $B$, given that we know $A$ occurred.
    We can also discuss conditional expectation $\E[X|A]$, the expected value of $X$ for those occurrences where $A$ occurred.

    Introduced in {video}`week4:joint-conditional` and discussed in [Notes on Probability](prob-conditional).

confidence interval
    An interval used to estimate the precision of an estimate.
    A 95% confidence interval is an interval computed from a procedure (including both taking a sample and computing a statistic from that sample) that, when repeated, will return an interval containing the true parameter value 95% of the time.
    Discussed in {video}`week4:confidence`, {reading}`week4:confidence-in-confidence`, and [Handbook section 1.3.5.2](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).

    A confidence interval is **not** a probabilistic statement about either the population mean $\mu$ or the sample mean $\bar{x}$.

correlation
    The extent to which two variables change *with each other*.
    If one variable usually increases when the other one increases, the variables are *correlated*; if one decreases when the other increases, they are *anticorrelated*.

    Correlation is measured with the correlation coefficient:

    $$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2}\sqrt{\sum(y_i - \bar{y})^2}}$$

    This is equivalent to the **{term}`covariance`** scaled by the {term}`standard deviations <standard deviation>` of the variables:

    $$\Cor(X, Y) = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$$
    
    Defined in {video}`week6:correlation` and [Notes on Probability](prob-variance). Used extensively in [Assignment 4](a4-covariance).

covariance
    A non-normalized measure of the extent to which two variables change with each other:

    $$\Cov(X, Y) = \E[(X - \E[X]) (Y - \E[Y])]$$

    Defined in {video}`week6:correlation` and [Notes on Probability](prob-variance). Used extensively in [Assignment 4](a4-covariance).

cumulative distribution function
    A function describing a distribution by defining the fraction of elements that are less than a particular value ($F_X(x) = \P[X < x]$).
    Also called a **CDF**.

    Discussed in [Notes on Probability](random-variables).  See {term}`empirical CDF`.

degrees of freedom
    The number of observations in a series that can independently vary to affect a calculation.
    This is usually the number of observations, minus the number of intermediate statistics.
    For example, the degrees of freedom for the sample standard deviation for $n$ observations is $n-1$, because one DoF is “used up” by the mean:

    $$s = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n - 1}}$$

    Introduced in {video}`week5:t-test`.

disaggregation
    When we take something that is usually aggregated over the total population (e.g. the completion rate for students at a school) and
    instead aggregate it over subsets of the population (e.g. computing a completion rate for each racial group).  Practiced in
    [Assignment 6](assignments/A6/index.md).

elementary event
    In probability theory, an individual distinct outcome of a process we are modeling as random.

    Introduced in {video}`week4:probability` and [Notes on Probability](resources/probability.md).

embedding
    As a noun, a vector-space representation of a data point or instance.
    This is often a lower-dimensional representation produced through some form of matrix decomposition such as SVD.
    Introduced in {module}`week13`.

    As a verb, to convert an instance to such a representation.

empirical CDF
    A {term}`cumulative distribution function` computed from data.

    Introduced in {video}`week2:distributions`.

encoding
    How we record a piece of data (especially an observation of a {term}`variable`) in the computer system.

    Introduced in {video}`week2:encodings`.

entropy
    A measure of the “uninformitiveness” or uncertainty represented by a probability distribution.  For a discrete distribution,
    it is computed as:

    $$H(X) = - \sum_x \P[x] \log_2 \P[x]$$

    The entropy is the expected number of bits required to record a draw from the distribution (or a message resolving the uncertainty)
    using an efficient {term}`encoding`, assuming the recipient knows the distribution and the encoding. 

    Introduced in {video}`week13:entropy`.

environment variable
    A string variable associated with a process by the operating system.
    Often used for configuring the behavior of software, such as the number of threads to use in parallel computation.
    Child processes inherit their parents' environment variables.

    Environment variables for the current process can be accessed and set in Python via the dictionary `os.environ`.

    In the Unix shell, set an environment variable with:

        export MY_VAR="contents"
    
    In PowerShell, set it with:

        $env:MY_VAR="contents"

    Set an environment variable *before* running commands that need to be governed by it.

epistemic uncertainty
    Uncertainty that arises due to incomplete knowledge about a process or future outcomes.
    Contrast {term}`aleatoric uncertainty`.

Euclidean norm
    See {term}`L₂ Norm`.

event
    In probability theory, an outcome that for which we want to estimate the probability.
    Formally, given a set $E$ of elementary outcomes, an event is a set $A \subseteq E$, and the set of possible events $\mathcal{F}$ forms a *sigma field*.

    Introduced in {video}`week4:probability` and [Notes on Probability](resources/probability.md).

estimand
    An unknown quantity that we try to estimate.  See *Estimator*.

estimate
    *n.* A value computed to approximate the value of some estimand.  See *Estimator*.
 
    *v.* The process of computing an estimate for an estimand.

estimator
    A computation (or computed value) that we use to try to estimate an unknown value.
    Formally, an *estimator* is a computation to produce an *estimate* of an *estimand*.
    The sample mean $\bar{x}$, as an abstract concept, is an estimator of the population mean, also as an abstract concept.
    Any *particular* sample mean we compute, such as $\bar{x} = 3.2$, is an *estimate* of the population mean (estimand) *for that sample*.

    Introduced in {video}`week4:introduction`.

expected value
    The mean of a {term}`random variable` $X$: $\E[X] = \sum x \P[x]$ or $\E[X] = \int x p(x) dx$.

    Discussed in {video}`week4:continuous` and [Notes on Probability](resources/probability.md).

frequentism
    A school of thought for statistical inference and the interpretation of probability that is concerned with probabilities as descriptions of the long-run behavior of a random process: how frequent would various outcomes be if the process were repeated infinitely many times?
    In statistical inference, this results in methods that are characterized by their behavior if a sampling procedure or experiment were repeated, such as confidence intervals (defined in terms of the behavior of calculating them over multiple samples) and *p*-values (the probability that a random sample would produce a statistic at least as large as the observed statistic if the sampling procedure were repeated).

geometric mean
    A measure of central tendency where sums are replaced by products. It is less sensitive to large outliers than the {term}`arithmetic mean` (the usual kind of mean).  It is computed by:

    $$\sqrt[n]{\prod_i x_i}$$

    Or alternatively (so long as $\forall i. x_i \ne 0$):

    $$e^{\frac{1}{n}\sum_i \operatorname{log}(x_i)}$$

HARKing
    “Hypothesizing After Results are Known”, a statistical error where we formulate our hypotheses to test *after* looking
    at the data.  A {term}`null hypothesis significance test` computes the probability
    $P(t' \ge t | H_0 \text{ is true})$; if we have already looked at the data, what we are computing is
    $P(t' \ge t | H_0 \text{ is true}, H_0 \text{ looks false})$.
    See {video}`week5:hypotest`.

heteroskedasticity
    Having unequal {term}`variance`.  The opposite of {term}`homoskedasticity`.

homoskedasticity
    Having the same {term}`variance`.  The opposite of {term}`heteroskedasticity`.

hyperparameter
    A value that controls a model's training or prediction behavior that is **not** learned from the data.
    Examples include learning rates, iteration counts, and regularization terms.
    These hyperparameters usually control one of three things:

    - A configurable aspect of the model's *structure*, such as the number of dimensions in a {term}`dimensionality reduction`.
    - A configurable aspect of the model's *objective function*, such as the regularization strength.
    - A configurable aspect of the model's *optimization process*, such as the number of iterations to run for an {term}`iterative method`.

    In programming, we would usually call these “parameters”, but that term is taken by the statistical or machine learning notion of a
    {term}`parameter`, so we call these “hyperparameters”.

inference
    As we primarily use it in this class, inference is the act of learning from the data; in particular, when we are trying to learn something about the world or the data generating process from the data we observe.  It contrasts with {term}`prediction`, discussed in {video}`week8:pred-inf` and at length in {module}`week4`.

    In machine learning deployment, inference is often used to refer to using the model to score or classify new instances at runtime, as opposed to the training stage of the model.

    Inference can also be used to refer to learning the model parameters itself, but we won't be using it this way to avoid confusion.

instance
    One entity of the data for a modeling or prediction problem.  Typically one row of the training or testing data; each row is an observation of an
    instance.  In general, however, it is one entity about which we are trying to learn or predict, such as one transaction.

iterative method
    An computational method that works by computing an initial solution (or guess) and iteratively refining it, usually until some stopping condition is met (often
    the number of iterations, or a convergence criteria such as the change from one iteration to the next dropping below a threshold).

    {py:func}`scipy.optimize.minimize` as demonstrated in {video}`week9:optimizing-loss` is an example of an iterative method.

joint probability
    The joint probability $\P[A, B]$ is the probability of both $A$ and $B$ occurring (in terms of underlying events, it's the probability that the elementary event $\zeta$ is in both $A$ and $B$).
    Equivalent to $\P[A \cap B]$.
    Related to the conditional and marginal probabilities by $\P[A, B] = \P[A|B] \P[B]$.
    Symmetric ($\P[A, B] = \P[B, A]$).

    Introduced in {video}`week4:joint-conditional` and [Notes on Probability](resources/probability.md).

L₁ Norm
    A measure of the magnitude of a vector, sometimes called the *Manhattan distance*.  It is the sum of the absolute values of the elements in the vector:

    $$\| \mathbf{x} \|_1 = \sum_i |x_i|$$

L₂ Norm
    A measure of the magnitude of a vector, also called the *Euclidean norm* or *Euclidean length*.  It is square root of the sum of squares of the elements in the vector:

    $$\| \mathbf{x} \|_2 = \sqrt{\sum_i x_i^2}$$

label
    An observed outcome for an {term}`instance`, used for supervized learning.  Sometimes called a {term}`supervision signal`.

leakage
    When your predictive model benefits from information that would not be available when the model is in actual use.
    Setting aside test data until the model is ready for final evaluation helps reduce leakage.

linear model
    A model of the form $\hat{y} = \beta_0 + \sum_i \beta_i x_i$: it is the sum of scalar products.

    Linear models are introduced in {module}`week8`.

logistic function
    A *sigmoid* function that maps unbounded real values to the range $(0,1)$:

    $$\mathrm{logistic}(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1}$$

    The logistic function is the invert of the {term}`logit function`.

    Logistic regressions are introduced in {module}`week10`.

logit function
    The inverse of the {term}`logistic function`:

    $$\mathrm{logit(x)} = \mathrm{logistic}^{-1}(x) = \operatorname{log} \frac{x}{1-x} = \operatorname{log} x - \operatorname{log} (1-x)$$

    Applying *logit* to a probability yields the {term}`log odds`.

log odds
    The logarithm of the {term}`odds`.  Introduced in {video}`week10:logistic`.

majority-class classifier
    A classifier that classifies every data point with the most common class from the training data.
    If 72% of the training data is in class A, the majority-class classifier will classify every test point as A, no matter what its input feature values are.

marginal probability
    The probability of a single event, or distribution of a single dimension, $P(A)$.
    Primarily used when we are talking about the probability of events (or expectation of variables) along one dimension of a *product space*, such as the suit or number of a card from a deck of playing cards.

    Described in {video}`week4:joint-conditional` and [Notes on Probability](resources/probability.md).

matrix
    A two-dimensional array of numbers.
    Alternatively, a linear map between vector spaces.

matrix decomposition
    A decomposition of a matrix into other matrices, such that multiplying the decomposition back together yields the original matrix or an approximation thereof.
    An example is the *singular value decomposition* (SVD):

    $$M = P \Sigma Q^T$$

    where $P \in \Reals^{m \times k}$ and $Q \in \Reals^{n \times k}$ are orthogonal, and $\Sigma \in \Reals^{k \times k}$ is diagonal.

    Introduced in {video}`week13:decomp`.

mean
    A measure of central tendency; the expected value of a random variable.  Without any further specifier, such as geometric or harmonic, the mean is taken to refer to the *arithmetic mean*.  The sample mean $\bar{x}$ is computed as:

    $$\bar{x} = \frac{1}{n} \sum_i x_i$$

    The mean of a vector or data series can be computed with {py:func}`numpy.mean` or {py:meth}`pandas.Series.mean`.

    Introduced in {video}`week2:descriptive-statistics`.

naïve Bayes
    A classification technique that uses Bayes' theorem to classify instances given (counts of) discrete features.  Given a sequence of tokens $T$,
    it computes:

    $$\P[Y=y|T] \propto \P[T|Y=y] P[Y=y]$$

    The "naïve" term comes from the simplifying assumption that tokens are conditionally independent of each other given the class, so that $\P[T|Y=y]$ can be
    computed from $\P[t|Y=y]$:

    $$\P[T|Y=y] = \prod_{t \in T} \P[t | Y=y]$$

    Naïve Bayes is a good baseline model for many text classification tasks.
    It is implemented (for arbitrarily many classes) by {py:class}`sklearn.naive_bayes.MultinomialNB`, and introduced in {video}`week12:classifying-text`.

null hypothesis
    A formalization of the idea of “no effect”, used for {term}`null hypothesis significance testing <null hypothesis significance test>` and typically
    denoted $H_0$. See {term}`p-value`.

null hypothesis significance test
    A significance test that assesses whether the data provide evidence to reject the {term}`null hypothesis` $H_0$ in favor of an alternate hypothesis
    $H_a$.  This is typically done by computing a {term}`p-value`, the probability of seeing an effect at least as large as the one observed if the
    null hypothesis is true, and rejecting the null hypothesis if this probability is sufficiently small.

objective function
    A function describing a model's performance that is used as the goal for learning its parameters.
    This can be a **loss function** (where the goal is to minimize it) or a **utility function** (which should be maximized).

    Defined in {video}`week11:eval-intro`, and introduced in {video}`week9:optimizing-loss`.

operationalization
    The mapping of a goal or question to a specific, measurable quantity (or measurement procedure).
    When we operationalize a question, we translate it into the precise computations and measurements we will use to attempt to answer it.

    Introduced in {video}`week1:asking-questions`.

odds
    An alternative way of framing probability, as the ratio of the likelihood for or against an event:

    $$\Odds(A) = \frac{\P[A]}{\P[A^c]}$$

    The {term}`log odds` is a particularly convenient way of working with odds, and is $\log \P[A] - \log (1 - \P[A])$.
    See the [{{mnote}} probability notes](prob-odds).

odds ratio
    The ratio of the odds of two different outcomes.

    $$\operatorname{OR}(A, B) = \frac{\Odds(A)}{\Odds{B}}$$

    See the [{{mnote}} probability notes](resources/probability.md#odds).

overfitting
    When a model learns too much from its training data, so it cannot do an effective job of predicting future unseen data.

    Introduced in {video}`week9:overfitting`.

parameter
    In *inferential statistics*: a “true” value in the population, such as the mean flipper length of Chinstrap penguins.
    The goal of inferential statistics is often to estimate parameters, because we typically do not have direct access to them.

    Introduced in {video}`week4:sampling`.

    In *model fitting*: a variable in a statistical or machine learning model whose value is learned from the data.
    Contrast {term}`hyperparameter`, a variable that controls the model or the model-fitting process but is not learned from the data.

$p$-hacking
    Computing hypothesis tests of multiple things in hopes that one of them will be statistically significant.
    See [XKCD #882: Significant](https://xkcd.com/882/) and [Week 4](p-hacking-cartoon).

population
    The complete set of entities we want to study.  This is not only all entities that *do* exist, but under some philosophies, all entities that *could* exist.
    For example, the set of all possible adult Chinstrap penguins would be the population.

    Discussed in more detail in {video}`week4:sampling`.

prediction
    Using a model to estimate or predict a score or label from explanatory variables for instances that were not seen during training.
    Contrasts with {term}`inference` as one of the major goals of modeling, discussed in {video}`week8:pred-inf`.

probability mass
    The amount of probability on a particular event.  Discussed in [:mdoc: Notes on Probability](probability-mass).

$p$-value
    In hypothesis testing, the probability that the null hypothesis ($H_0$) would produce a value as large as the observed value; if the observed statistic is $x$ and $X$ is a random variable representing the sampling and analysis process, this is $\P[X > x | H_0 \text{ is true}]$.

    Typically the null hypothesis is an appropriate formalization of “nothing interesting”, so the *p*-value is the probability of seeing an effect as large as the one observed if there is no true effect to observe.

    Discussed in {video}`week5:hypotest`.

random variable
    A variable that takes on random values, usually as the result of a random process or because we are using randomness and probability to model uncertainty about the variable's actual value in any particular case.  For our purposes, random variables may be discrete (integer-valued) or continuous (real-valued), but are always numeric.  We denote random variables with capital letters ($X$).  A single sample is an observation of a random variable.

    The probability distribution of a continous random variable is defined by a distribution function $F_X(x) = \P[X < x]$.
    Two common operations on a random variable are to take its {term}`expected value` or compute its {term}`variance`.

    Formally, a random variable is a function $f_X: E \to \Reals$, where $E$ is the set of {term}`elementary events <elementary event>` from a probability space $(E, \Field, \P)$, and $F_X(x) = \P[F_X(e) < x]$.  For the purposes of this class, we will not need this distinction.

    Discussed in [Notes on Probability](resources/probability.md) and {video}`week4:continuous`.

regression
    A modeling or prediction problem where we try to estimate or predict a continuous variable $Y$.

    This is the focus of {module}`week8`.

regularization
    A penalty term added to a loss function, typically penalizing large values.  Used to encourage sparsity or to require coefficients to be supported by larger quantities of data.

    Introduced in {video}`week11:regularization`.

residual
    The error in estimating a variable with a model.  For a model fitting an estimator $\hat{Y}$ for a variable $Y$, the residuals are $\epsilon_i = y - \hat{y}$.
    This is reflected in the full linear model: $y_i = \beta_0 + \sum_j \beta_j x_{ij} + \epsilon_i$.

    Introduced in {video}`week8:single-regression`.

sample : n.
    A subset of the population, for which we have observations.

    Discussed in more detail in {video}`week4:sampling`.

sample size
    The number of items in the sample.  Often denoted $n$.

sampling distribution
    The distribution of a statistic when it is computed over many repeated samples of the same size from the same population.
    The sampling distribution of the sample mean from a population with mean $\mu$ and variance $\sigma^2$ is $\mathrm{Normal}(\mu, \sigma/\sqrt{n})$.

    Discussed in {video}`week4:sampling`.

statistic
    A value computed from a set of observations.
    For example, the sample mean $\bar{x} = n^{-1} \sum_i x_i$ is a statistic of a sample $X = \langle x_i, \dots, x_n \rangle$.
    
    Discussed in {video}`week4:introduction`.

standard deviation
    A measure of the spread of a {term}`random variable`.  It is the square root of the mean squared deviation from the mean:

    $$\sigma_X = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n}}$$

    Sometimes we compute the **sample standard deviation**:

    $$s = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n - 1}}$$

    The sample standard deviation is an {term}`unbiased estimator` of the population standard deviation;
    computing the standard deviation (divided by $n$ instead of $n-1$) technically has a small bias when
    used to estimate the population standard deviation, but in reasonably large data sets this difference
    is miniscule, and often is [not very important](https://dansblog.netlify.app/posts/2021-10-11-n-sane-in-the-membrane/)
    (there are usually more impactful discrepancies between the sample estimate and population s.d. than this bias).

    The standard deviation is the square root of the {term}`variance`.

    Standard deviations can be computed with:

    - {py:meth}`pandas.Series.std` (computes sample $s$, pass `ddof=0` to compute population $\sigma$)
    - {py:func}`numpy.std` (computes population $\sigma$, pass `ddof=1` to compute sample $s$)

    Introduced in {video}`week2:descriptive-statistics`.

standard error
    The standard deviation of the *sampling distribution* of a statistic.  The standard error of the mean (Pandas method {py:meth}`pandas.Series.sem`) is $s/\sqrt{n}$.

    Discussed in {video}`week4:confidence`.

standardization
    Normalizing a variable to be in units of ``standard deviations from the mean'', instead of the original units.  This is done by
    subtracting the mean and dividing by the standard deviation (in this formula, $\tilde{x}_i$ is the standardized value of observation $x_i$):

    $$\tilde{x}_i = \frac{x_i - \bar{x}}{s}$$

    Demonstrated in [One Sample notebook](resources/tutorials/OneSample.ipynb).

supervision signal
    The label or outcome observations used for supervised machine learning.  See {term}`label`.

    This term is introduced in {video}`week13:unsupervised-intro`.

supervized learning
    Training a model to predict an observed outcome or {term}`label`.  We use this when we have known outcomes for training and evaluation data,
    and want to build a model that will predict those outcomes for future data before they are observed (or when they cannot be observed).

    Contrast {term}`unsupervised learning`.

test set
    A portion of your data set that is held back to evaluate the effectiveness of the **final** model.
    Contrast with {term}`training set`.
    Sometimes erroneously called the {term}`validation set`.

    Data is typically split into three pieces:

    1. The test set
    2. The tuning or validation set
    3. The training set

    Once model tuning is done, the model may be retrained on the union of the training and tuning sets, or it may be used as-is.
    We can think of these either as three separate sets, or as a sequence of splits:

    - Split the initial data into train and test data
    - Re-split the training data into tuning data a “train'” set
    
    Introduced in {video}`week8:prediction-accuracy` and discussed in more detail in {video}`week11:workflow`.
    See also [Training, validation, and test sets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets) on Wikipedia, and
    [this answer on Cross Validated](https://stats.stackexchange.com/a/96869/389).

training set
    The portion of your data set on which you train your model.
    Contrast with {term}`test set` and {term}`tuning set`.
    See {term}`test set` for more details.

*t*-test
    A statistical test for means of normally-distributed data.  T-tests come in three varieties:

    1. One-sample *t*-test that tests whether a single mean is different from zero (or another fixed value $\mu_0$).  $H_0: \mu=0$
    2. Two-sample independent *t*-test that tests whether the means of two independent samples are the same.  $H_0: \mu_1 = \mu_2$
    3. Paired *t*-test that tests, for a sample of paired observations, whether the mean difference between observations for each sample is zero (the measurements are, on average, the same).  $H_0: \mu_{x_{i1} - x_{i2}} = 0$

    Discussed in {video}`week5:hypotest`, {video}`week5:t-test`, and associated readings.

tuning set
    A portion of your data set that you use to compare the performance of different candidate models, for hyperparameter tuning, feature selection, and similar tasks.
    Distinct from the {term}`test set`, which is only used **once** to test the performance of your final model.
    Often called a *validation set*, but I avoid this term because it is ambiguous.

    See {term}`test set` for more details.

unbiased estimator
    An {term}`estimator` whose expected value is the population parameter.

unsupervised learning
    Learning when we do not have a specific observed outcome to predict; this typically tries to learn patterns or structure in the training data,
    but no external ground truth is available to know if the patterns it learns are “correct”.  Contrast {term}`supervised learning`.  Introduced in
    {video}`week13:unsupervised-intro`.

validation set
    A widely-used name for the {term}`tuning set`.  Sometimes validation and test are switched, so an author will talk about trying out different models with their test set and doing the final evaluation with a validation set.  I avoid the term due to this confusion.

    See {term}`test set` for more details.

variable
    In **statistics**, a particular data value that can be observed.  For example, the a penguin's mass is a variable for penguin entities.
    A {term}`random variable` is a variable that takes on random values (or unknown values, where we model the unknowns with randomness).

    In **programming**, a name used to refer to a piece of data.  The following Python code assigns the value 3 to the variable `x`:

    ```python
    x = 3
    ```

variance
    A measure of the spread of a random variable (which may be observable quantities in the population).

    $$\Var(X) = \E[(X - \E[X])^2]$$

    Variance is the square of the {term}`standard deviation`, and is sometimes written $\sigma^2$.  It is also related to the {term}`covariance`: $\Var(X) = \Cov(X, X)$.

    Variance can be computed with:

    - {py:meth}`pandas.Series.var` (computes sample variance, pass `ddof=0` to compute population variance)
    - {py:func}`numpy.var` (computes population variance, pass `ddof=1` to compute sample variance)

vector
    A sequence or array of numbers; $\mathbf{x} = [x_1, x_2, \dots, x_n]$ is an $n$-dimensional vector.

vectorization
    Writing a computation so that mathematical operations are done across entire arrays at a time, rather than looping over individual data points in Python code.

:::
