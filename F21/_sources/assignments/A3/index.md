# Assignment 3

The purpose of Assignment 3 is to give you experience integrating data from multiple sources to explore a two-variable question.

It is due **October 10, 2020** at the end of the day (11:59 PM). Submit your `.ipynb` and PDF files to {{LMS}}.

:::{note}
This assignment is not structured step-by-step like the first two.  I describe the data, and the questions you need to answer,
and you need to build a well-structured notebook that answers them.
:::

:::{admonition} Read
:class: tip

Read the entire assignment before you begin!
:::

## Revision Log

Sep. 30, 2021
:   Fixed lingering reference to 3 mortality rates.

## Concept

**Central Question:** Are health outcomes correlated with poverty levels in a community?

That is the key objective of this assignment.  To answer this, we are going to obtain poverty data from the U.S. Census Bureau and health data from the Global Health Data Exchange and the US Centers for Disease Control, and look at the relationship between a state's poverty rate and various health outcomes.

We are going to operationalize these as follows:

-   Poverty rate: fraction of family households underneath the poverty line in 2014
-   Health outcomes:
    -   Mortality rates from infectious diseases in 2014
    -   Infant mortality rate in 2014
-   Unit of analysis: state (we will discuss implications of this!)

For more background, read [Healthy People 2020's description of social determinants of health](https://www.healthypeople.gov/2020/topics-objectives/topic/social-determinants-of-health).

## Data

We're going to get data from 3 sources.

### Income — US Census

We are going to get *income* data from the US Census Bureau.
See [Using the Census](../../resources/tutorials/UsingTheCensus.ipynb) for an introduction to working with this data.

The in-class exercise on September 30 will give you practice with census data.

#### Setting Up

Before using census data, you need to get an API key. [Request one here](https://api.census.gov/data/key_signup.html).

You will also need to install the Python package for the Census API, and a package of US state code data.  These are not available in the main Conda repository, so use Pip:

    pip install census us

#### Data Layout

The census data comes in a variety of *files*. These files include:

- `sf1` — Summary File 1, containing complete count information on the *decennial* census.
- `acs5` — American Community Survey, a supplementary annual survey of a sample of the population carried out by the census bureau, 5-year estimates.

We are going to be using ACS5.  It has thousands of variables.  The [variable list](https://api.census.gov/data/2014/acs/acs5/variables.html) describes them, and the ones of interest are all reported as **estimated population counts**.  That means variable `B06009_003E` is an estimate, based on the sample, of the number of people in a geographic region whose highest educational attainment is a high school degree.

The `B05010_*` variables describe population with respect to the poverty line.  `B05010_001E` is the estimated total number of family households, and `B05010_002E` is the estimated number under the poverty line.  These variables are described in more detail in the [Social Data Explorer](https://www.socialexplorer.com/data/ACS2014_5yr/metadata/?ds=ACS14_5yr&table=B05010).

You can use these two variables to caculate the *poverty level* as defined above: the fraction of households under the poverty line.

:::{admonition} Fetching Census Data
:class: tip

If you have a `Census` object defined in variable `c`, as we did in the Sep. 30 example, you can fetch these variables for all states with:

```python
state_pop = pd.DataFrame.from_records(c.acs5.state(('NAME', 'B05010_001E', 'B05010_002E'), '*', year=2014))
```
:::

The `state` column in the resulting table is the state's FIPS code, as a string.

:::{admonition} Social Explorer
:class: tip

The Social Explorer has a very good [database of census fields](https://www.socialexplorer.com/data/ACS2014_5yr/metadata/?ds=ACS14_5yr).
This database describes all the census sub-tables, and lets you browse them by group (e.g. B05010).

Within the page for a group, such as [B05010](https://www.socialexplorer.com/data/ACS2014_5yr/metadata/?ds=ACS14_5yr&table=B05010), there
is a list of all the sub-variables, organized hierarchically so you can see how they relate to each other.
The variable names do need a bit of modification; when Social Explorer says `B05010001`, you need to request that from the census as `B05010_001E` (the Estimated value).
The census API puts an underscore (`_`) between th evariable group code (`B05010`) and the specific sub-variable identifier (`001E`); Social Explorer does not include the underscore.

The explorer also includes excerpts from the full census technical documentation providing more detail about the different variables and their codings.
:::

### Infectious Deseases — GHDx

We will obtain infectious disease mortality rates from the [Global Health Data Exchange](http://ghdx.healthdata.org/record/ihme-data/united-states-infectious-disease-mortality-rates-county-1980-2014).
These files contain county- and state-level mortality data from the U.S. from 1980 to 2014.
The files themselves are on the “Files” tab; download “National: All States and Counties (5-year Intervals)”.

Pandas provides a [`read_excel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) function to read data tables from Excel files.
This file has 6 sheets, one for each of 6 different disease families.

:::{admonition} Reading GHDx Data
:class: tip

You can read these data files with {py:func}`pandas.read_excel`:

```python
sheets = pd.read_excel('IHME_USA_COUNTY_INFECT_DIS_MORT_1980_2014_NATIONAL_Y2018M03D27.XLSX',
                        sheet_name=None, header=1, skipfooter=2)
```

The resulting `sheets` variable is a *dictionary* (remember those?) mapping sheet names (disease families) to data frames.
The `sheet_name=None` option tells it to load all sheets, and `header=1` says to skip the first row and read the column headers from the second.
`skipfooter=2` tells it to skip the last two rows as well.  Look at the files to see why!

For this function to work, you will need the `openpyxl` module:

    conda install openpyxl

You won't need to use openpyxl directly, but Pandas uses it to read Excel files.

Alternatively, you can open the data file in Excel or LibreOffice and export the parts you need to a CSV file.
:::

This data frame has annoying column names, and also annoying fields: the field values include confidence intervals. 

:::{admonition} Extracting Column Data
:class: tip

The {py:meth}`pandas.Series.str.replace` method, combined with a type conversion, lets us extract the actual estimate from the cell that includes the confidence intervals.
We can do this by replacing the parenthsized intervals with nothing.  Like this:

```python
df['Mortality'] = df['Mortality Rate, 2014*'].str.replace(r'\s*\(.+\)', '').astype('f8')
```
:::

This mortality data is recorded as “deaths per 100,000 people”.  The rates are *age-standardized*: look up age-standardized mortality rates to read about what this means.

### Infant Mortality — CDC

The Centers for Disease Control and Prevention provide a table of [infant mortality data by state](https://www.cdc.gov/nchs/pressroom/sosmap/infant_mortality_rates/infant_mortality.htm).
Click “Download Data (CSV)” at the bottom of the page to download the file.

This file has multiple years; you will need to select the rows with the year you want.

### FIPS Codes

A [FIPS code](https://en.wikipedia.org/wiki/FIPS_county_code) is a numeric code that identifies a U.S. state or county.
State codes are two digits; you can therefore extract the state-level data from an Infectious Disease table by selecting all rows where the FIPS column is less than 100 (the national-level `NaN` will also be excluded by such a filter).

Both the census and the infectious disease table use FIPS codes, so you can join or merge (subsets of) the two tables by their FIPS code.
The census will return FIPS data as a string, so you will need to convert it to a number (`.astype('i4')`) before joining.
It is fine to join an integer column with a floating-point column.

The infant mortality data does *not* use FIPS codes — it uses state abbreviations.
To link FIPS codes to state abbreviations, you can use the `us` Python package (and create a data table with the appropriate linking identifiers), or download the “National FIPS and GNIS Codes File” from the [US Census Bureau](https://www.census.gov/library/reference/code-lists/ansi/ansi-codes-for-states.html).
It is separated by vertical bars (`|`), so you can read it with:

    pd.read_table('state.txt', sep='|')

You may need to convert the data type of the FIPS code column.  Once you have this file, you can merge infant mortality with census data by:

1.  Merge infant mortality with the state codes file by state abbreviation to get FIPS codes.
2.  Merge the resulting table with census data by FIPS code.

## Requirements

Submit a notebook using the data above to do the following (all for year 2014 data):

1.  (20%) Describe, both numerically and graphically, the distribution of state poverty rates.
2.  (30%) Show the relationship of poverty rates to mortality rates of two different disease families — Meningitis and Diarrheal deseases — using appropriate plots.
3.  (20%) Quantify the relationship between poverty and each of the 2 mortality rates in (2) by computing correlation coefficients with bootstrapped confidence intervals for each disease.
4.  (20%) Repeat (2) and (3) for infant mortality.
5.  (10%) Write 2–3 paragraphs about what you learn from these data.  Discuss also limitations that you see in the data and analysis!

:::{admonition} Correlation and Causation
:class: note

All this analysis can look at is whether the states with higher poverty rates also tend to have better or worse health outcomes.
We can draw no conclusions about *causality* between these variables.
:::

:::{tip}
The [Correlation Notebook](../../resources/tutorials/Correlation.ipynb) shows how to bootstrap a confidence interval for a correlation.
:::

:::{admonition} Structure
:class: Note

There are a couple of different ways you can think about organizing your data and questions:

- Load and merge all data sets in a “Data” section, and then proceed with the analysis.
- Load and merge data in analysis-specific subsections.
:::

## Time Estimates

I'm going to try something new this time, and please let me know if it's helpful or not.
I'm going to provide a little info on how long I expect each piece might take, given what we've done in the class so far.
These numbers are aimed to target about the 80th %ile of how long it would take the students in this class, but I admit it's just my best guess.
My hope is that it helps you calibrate your work and expectations.
I would love feedback on this!  Should I keep doing it?

- Fetching census data & describing poverty rates: 1.5 hours (we've done a lot of data descriptions by now)
- Reading GHDx data and linking it to census data: 1 hour
- Showing infectious disease and mortality: 1 hour
- Computing correlations and bootstrapped CIs for infectious diseases: 2 hours
- Reading and linking infant mortality data: 1.5 hours
- Presenting infant mortality correlations: 1 hour (you should be able to reuse ideas & code from the infectious diseases)
- Cleaning up, presenting, and writing your conclusions: 2 hours
