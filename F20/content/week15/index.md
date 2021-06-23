# Week 15 — What Next?
{% import 'video.md' as media %}

This is the last week of class. We're going to recap, and talk about what's next, both for learning and for putting what you've learned to practical use.

[TOC]

This week's videos are also available as a [Panopto playlist](https://boisestate.hosted.panopto.com/Panopto/Pages/Viewer.aspx?pid=4d0ba130-571b-4ed0-b38d-ac8900665be1).

## :a-video: Recap {: data-length="6m23s"}

This video reviews the concepts we have discussed this term and puts them into the broader context of data science.

=== "Video"

    {{ media.video('56f9e697-dcc1-488f-b704-ac890065a439') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173432', 'AHfNFdGccgu4HVE') }}

{{ media.vidtext('15-1 - Recap') }}

## :a-video: Data and Concept Drift {: data-length="7m13s"}

This video introduces a fundamental assumption of predictive modeling and the way *drift* can affect it.
 
=== "Video"

    {{ media.video('6cfcf3f6-241f-4f28-9dd6-ac89006a23a3') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173435', 'AE55Qg7-c1ba2sg') }}

{{ media.vidtext('15-2 - Drift') }}

### Resources

- [A unifying view on dataset shift in classification](https://doi.org/10.1016/j.patcog.2011.06.019) (available through Boise State library)

## :a-video: Time Series Operations {: data-length="11m16s"}

Time is an important kind of data that we haven't spent much time with — this video discusses the fundamental Pandas operations for working with time-series data.

=== "Video"

    {{ media.video('d160dff7-e6f7-47fc-96c7-ac890065a401') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173433', 'AOYczBP6aJFAe9Q') }}

{{ media.vidtext('15-3 - Time Series Operations') }}

### Resources

- [Pandas time series analysis](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

## :a-notebook: Time Series Example

The [MovieLens Time Series notebook](../../resources/tutorials/MLTimeSeries.ipynb) demonstrates basic time series operations in Pandas.

## :a-quiz: Weekly Quiz 15

Take the Week 15 Quiz in Blackboard.

## :a-video: Correlated Errors {: data-length="13m50s"}

Regression models require that the data be *independent*. This video introduces two kinds of non-independence and methods for addressing them: grouped observations addressed with a mixed-effects model and temporal auto-correlation addressed with ARIMA models.

=== "Video"

    {{ media.video('f3021c78-deef-4e69-8f87-ac89006865fb') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173434', 'AM4VHU5-GJ5MWCQ') }}

{{ media.vidtext('15-4 - Correlated Errors') }}

### Resources

- [Linear Mixed Effects in statsmodels](https://www.statsmodels.org/stable/mixed_linear.html)
- [Time Series Analysis in statsmodels](https://www.statsmodels.org/stable/tsa.html)
- [Time Series Analysis slides](http://people.cs.pitt.edu/~milos/courses/cs3750/lectures/class16.pdf) — much more in-depth treatment

## :a-video: Publishing Projects {: data-length="9m55s"}

This video talks about going from an analysis and its notebooks to a publishable paper.

=== "Video"

    {{ media.video('22727cd5-2fbc-4125-9b65-ac89006dc967') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173436', 'AADUJlRHFQaO_HA') }}

{{ media.vidtext('15-5 - Publishing Projects') }}

### Resources

- [PlotNine](https://plotnine.readthedocs.io/en/stable/api.html) is a good plotting library for preparing consistent, publication-ready graphics.
- The [book gender example](../week14/index.md#more-examples) also demonstrates the current evolution of my own practices for preparing for publication.

## :a-video: Production Applications {: data-length="7m28s"}

How do you put the results of your data science project into product?

=== "Video"

    {{ media.video('16e9af81-ea7b-4d46-b4bf-ac89006ebceb') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173437', 'ADSmmu5pFo5O0Ks') }}

{{ media.vidtext('15-6 - Production Applications') }}

## :a-video: Topics to Learn {: data-length="6m25s"}

This video goes over some useful topics to learn to fill out more of your data science education.

=== "Video"

    {{ media.video('8ba3b404-9499-4134-8be7-ac890071e33c') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173438', 'AJKQaSqNcdTrWcc') }}

{{ media.vidtext('15-7 - Topics to Learn') }}

## :a-video: General Tips {: data-length="10m25s"}

Some final closing tips and suggestions for you to think about as you take the next steps in your data science career.

=== "Video"

    {{ media.video('211d4a20-4b95-45d0-b7b5-ac890073df03') }}

=== "Slides"

    {{ media.slides('495979F9A431DDB0%2173439', 'AMQPBtshRrNaHoc') }}

{{ media.vidtext('15-8 - General Tips') }}

## :a-video: Farewell {: data-length="1m58s"}

It's been grand!
I would love to hear more feedback on how to improve this material, because I hope to keep using it for a while.

=== "Video"

    {{ media.video('d0ddb9e9-abc5-4401-840e-ac890065a3b3') }}

## :a-quiz: Makeup Exam

The makeup midterm is due **Saturday, Dec. 12** at **5:00 PM**.

!!! warning "Grade Replacement"

    If you turn in the makeup exam to be graded, its grade will replace the lower of your Midterm A and B grades, **even if that lowers your final grade**.
    Only turn it in if you think you did better than your worst normal midterm!

## :a-assignment: Assignment 7

[Assignment 7](../../assignments/A7/index.md) is due **December 13, 2020**.

## :a-quiz: Final Exam

The final exam will be released at 5PM on **Monday, Dec. 14**, and due at **5PM Thursday, Dec. 17**.
