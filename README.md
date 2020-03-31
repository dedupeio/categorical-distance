categorical-distance
====================

Compare categorical variables

Part of the [Dedupe.io](https://dedupe.io/) cloud service and open source toolset for de-duplicating and finding fuzzy matches in your data.

```python
>>> import categorical
>>> categories = ('a', 'b')
>>> comparator = categorical.CategoricalComparator(categories)
>>> comparator('a', 'a')
[ 0.  0.]
>>> comparator('b', 'b')
[ 1.  0.]
>>> comparator('a', 'b')
[ 0.  1.]
>>> comparator('b', 'a')
[ 0.  1.]
```
