# Common Problems

This page describes common problems you may encounter with Pandas, and how to fix them.

(prob-missing-plots)=
## Missing Plots

**Symptoms:** plots do not show up in the Jupyter notebook.

Some versions of Jupyter and IPython will display plots directly in the notebook without any need for specific intervention.
Some versions, however, need you to explicitly draw the plots or enable auto-display.

To enable auto-display, include a code cell near the top (I usually do this right before or after imports) that uses the `%matplotlib` “magic” to turn on inline auto-display:

```
%matplotlib inline
```

To explicitly draw plots, use the {py:func}`matplotlib.pyplot.plot` function.  With the idiomatic import in your setup section:

```
import matplotlib.pyplot as plt
```

You can draw plots by putting the following at the end of any cell containing a plot:

```
plt.plot()
```

(prob-mangled-pdf)=
## Mangled PDFs

**Symptoms:** you follow the instructions to export a PDF using Print Preview, but the resulting PDF has display problems such as missing or truncated plots.

I have seen this problem arise most frequently when using Firefox.  There are three ways I know of to fix it:

1. Use Chrome, Chromium, or Microsoft Edge instead of Firefox.  Its PDF renderer seems to usually work better.

2. Use Jupyter's PDF-through-LaTeX export (in the Jupyter “File” menu).  This requires you to have Pandoc (which Conda will install), and a working LaTeX installation.  On Linux, you can get LaTeX by installing TeXlive from your distribution's package manager.

3.  Use Jupyter's PDF-through-HTML export.  This requires an additional package, and a download of a compatible version of Chromium (which the package will do for you).  In your Conda shell, run the following to install Pyppeteer and Chromium:

    ```shell
    conda install -c conda-forge pyppeteer
    pyppeteer-install
    ```

(prob-memory-explosion)=
## Memory Explosion

**Symptoms:** notebook or kernel crashes, system grinds to a halt.

There are some seemingly-innocuous things that can cause Pandas to eat an absurd amount of memory.  The common ones involve either hierarchical indexes or non-unique indexes.  I've seen it happen with:

- `groupby` on a frame with a hierarchical index
- `groupby` on a frame with a non-unique index
- `join` with a non-unique index

If you are experiencing this problem, make sure that your frames have single-level, unique indexes.  If in doubt, just reset the index to get a range index.

For more on indexes, see [Indexing](tutorials/Indexing.ipynb).

(warn-chained-assignment)=
## Chained Assignment

**Symptoms:** Pandas issues a warning about chained assignment or assigning to a copy of a slice.

When you slice or subset a data frame, Pandas returns a *view* backed by the original data.  If you then try to *modify* that slice, Pandas is not sure if you want to modify the original data or the view (which is supposed to act like a copy, but save memory).

For example, if you write:

```python
frame[mask]['column'] = 400
```

Pandas will issue the warning.  There are two solutions, depending on what you want to do:

-   If you want to modify the underlying frame, use `.loc` (or `.iloc`) to index and modify the appropriate subset:

    ```python
    frame.loc[mask, 'column'] = 400
    ```

-   If you want to modify a copy, use `.copy()` to make a copy of the frame:

    ```python
    f2 = frame[mask].copy()
    f2['column'] = 400
    ```

    In this version, the contents of `frame` are unchanged.
