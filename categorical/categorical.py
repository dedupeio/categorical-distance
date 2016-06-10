import itertools
import warnings
import numpy

class CategoricalComparator(object):
    def __init__(self, category_names) :
        if None in category_names :
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

        self.levels = set(category_names)

    def __call__(self, field_1, field_2):
        categories = (field_1, field_2)
        if categories in self.categories :
            return self.categories[categories]
        else :
            unmatched = set(categories) - self.levels

            raise ValueError("value(s) %s not among declared "\
                             "set of categories: %s" %
                             (unmatched, self.levels))

def vectorLength(n) :
    vector_length = (n + 1) * n / 2 # (n + r - 1) choose r
    vector_length -= 1 
    return int(vector_length)
    

def responseVector(value, vector_length) :
    response = numpy.zeros(vector_length)
    if value :
        response[value - 1] = 1
    return response
