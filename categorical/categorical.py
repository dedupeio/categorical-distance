import itertools
import warnings
import numpy

class CategoricalComparator(object):
    def __init__(self, category_names) :
        if '' in category_names :
            raise ValueError("'' is an invalid category name. "
                             "'' is reserved for missing values.")
        if '' in category_names :
            raise ValueError("None is an invalid category name. "
                             "None is reserved for missing values.")


        vector_length = vectorLength(len(category_names))
        
        categories = [(name, name) for name in category_names]
        categories += itertools.combinations(category_names, 2)
        self.dummy_names = categories[1:]
        
        self.categories = {}
        for i, (a, b) in enumerate(categories) :
            response = responseVector(i, vector_length)
            self.categories[(a,b)] = response
            self.categories[(b,a)] = response

        self.missing_response = numpy.array([numpy.nan] * int(vector_length))

        self.levels = set(category_names)

    def __call__(self, field_1, field_2):
        categories = (field_1, field_2)
        if categories in self.categories :
            return self.categories[categories]
        elif field_1 == '' or field_2 == '' :
            warnings.warn('In the dedupe 1.2 release, missing data will have to have a value of None. See http://dedupe.readthedocs.org/en/latest/Variable-definition.html#missing-data')
            return self.missing_response
        else :
            unmatched = set(categories) - self.levels

            raise ValueError("value(s) %s not among declared "\
                             "set of categories: %s" %
                             (unmatched, self.levels))

def vectorLength(n) :
    vector_length = (n + 1) * n / 2 # (n + r - 1) choose r
    vector_length -= 1 
    return vector_length
    

def responseVector(value, vector_length) :
    response = numpy.zeros(vector_length)
    if value :
        response[value - 1] = 1
    return response

