# Measure

The measure defines the formula by which the distance between strings is measured.

Use as:

```python
from simstring.measure.cosine import CosineMeasure
from simstring.measure.jaccard import JaccardMeasure
from simstring.measure.overlap import OverlapMeasure
from from simstring.measure.dice import DiceMeasure

```

But be carefull, they are not identical to the normal definitions of these measures. 


Cosine Measure is different to `scipy.spatial.distance.cosine` as it works on strings and not vectors.


Jaccard distance does not discard duplicates in its sets, unlike in the normally used definition. This means that 'fooo' is seen as more different from 'fo' than 'foo', which is a more useful way of lookng at the string difference, but is not the usual definition of the distance as implimanted by `scipy.spatial.distance.jaccard` or [wikipedia](https://en.wikipedia.org/wiki/Jaccard_index) or any public [calculator](https://planetcalc.com/1664/).


## Cosine Measure

::: simstring.measure.cosine.CosineMeasure
    handler: python
    options:
      show_root_heading: false

## Jaccard Measure

::: simstring.measure.jaccard.JaccardMeasure
    :docstring:
    :members:

## OverlapMeasures

::: simstring.measure.overlap.OverlapMeasure
    :docstring:
    :members:

::: simstring.measure.overlap.LeftOverlapMeasure
    :docstring:
    :members:


## DiceMeasure

::: simstring.measure.dice.DiceMeasure
    :docstring:
    :members:
