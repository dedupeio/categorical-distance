# -*- coding: utf-8 -*-
import unittest
import categorical
import numpy
from numpy.testing import assert_array_equal

class CategoricalTest(unittest.TestCase):
    def test_categorical_two(self) :
        comparator = categorical.CategoricalComparator(['a', 'b'])
        assert_array_equal(comparator('a', 'a'), [0, 0])
        assert_array_equal(comparator('b', 'a'), [0, 1])
        assert_array_equal(comparator('a', 'b'), [0, 1])
        assert_array_equal(comparator('b', 'b'), [1, 0])
    def test_categorical_three(self) : 
        comparator = categorical.CategoricalComparator(['a', 'b', 'c'])
        assert_array_equal(comparator('a', 'a'), [ 0, 0, 0, 0, 0,])
        assert_array_equal(comparator('b', 'a'), [ 0, 0, 1, 0, 0,])
        assert_array_equal(comparator('a', 'b'), [ 0, 0, 1, 0, 0,])
        assert_array_equal(comparator('b', 'b'), [ 1, 0, 0, 0, 0,])
        assert_array_equal(comparator('c', 'c'), [ 0, 1, 0, 0, 0,])
        assert_array_equal(comparator('a', 'c'), [ 0, 0, 0, 1, 0,])
        assert_array_equal(comparator('c', 'a'), [ 0, 0, 0, 1, 0,])
        assert_array_equal(comparator('b', 'c'), [ 0, 0, 0, 0, 1,])
        assert_array_equal(comparator('c', 'b'), [ 0, 0, 0, 0, 1,])

    def test_errors(self) :
        comparator = categorical.CategoricalComparator(['a', 'b'])
        self.assertRaises(ValueError, lambda : comparator(1,2))


if __name__ ==  "__main__":
    unittest.main()

