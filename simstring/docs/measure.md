# Measure

The measure defines the formula by which the distance between strings is measured.

Use as:

```python
from simstring.measure import CosineMeasure, JaccardMeasure, OverlapMeasure, DiceMeasure

```

But be carefull, they are not identical to the normal definitions of these measures. 


Cosine Measure is different to `scipy.spatial.distance.cosine` as it works on strings and not vectors.


Jaccard distance does not discard duplicates in its sets, unlike in the normally used definition. This means that 'fooo' is seen as more different from 'fo' than 'foo', which is a more useful way of lookng at the string difference, but is not the usual definition of the distance as implimanted by `scipy.spatial.distance.jaccard` or [wikipedia](https://en.wikipedia.org/wiki/Jaccard_index) or any public [calculator](https://planetcalc.com/1664/).


## Cosine Measure

::: simstring.measure.CosineMeasure
    :docstring:
    :members:

## Jaccard Measure

::: simstring.measure.JaccardMeasure
    :docstring:
    :members:

## OverlapMeasures

::: simstring.measure.OverlapMeasure
    :docstring:
    :members:

::: simstring.measure.LeftOverlapMeasure
    :docstring:
    :members:


## DiceMeasure

::: simstring.measure.DiceMeasure
    :docstring:
    :members:
