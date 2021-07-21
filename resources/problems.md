# Common Problems

This page describes common problems you may encounter with Pandas, and how to fix them.

## Memory Explosion

**Symptoms:** notebook or kernel crashes, system grinds to a halt.

There are some seemingly-innocuous things that can cause Pandas to eat an absurd amount of memory.  The common ones involve either hierarchical indexes or non-unique indexes.  I've seen it happen with:

- `groupby` on a frame with a hierarchical index
- `groupby` on a frame with a non-unique index
- `join` with a non-unique index

If you are experiencing this problem, make sure that your frames have single-level, unique indexes.  If in doubt, just reset the index to get a range index.

For more on indexes, see [Indexing](tutorials/Indexing.ipynb).

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
