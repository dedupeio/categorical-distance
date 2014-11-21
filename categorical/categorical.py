import itertools
import numpy

class CategoricalComparator(object):
    def __init__(self, category_names) :
        vector_length = vectorLength(len(category_names))
        
        categories = [(name, name) for name in category_names]
        categories += itertools.combinations(category_names, 2)
        self.dummy_names = categories[1:]
        
        self.categories = {}
        for i, cat in enumerate(categories) :
            response = responseVector(i, vector_length)
            self.categories[cat] = response
            alternate_order = tuple(reversed(cat))
            self.categories[alternate_order] = response

        self.categories_and_null = set(category_names + [''])
        self.missing_response = numpy.array([numpy.nan] * vector_length)

    def __call__(self, field_1, field_2):
        categories = (field_1, field_2)
        if categories in self.categories :
            return self.categories[categories]
        elif set(categories) <= self.categories_and_null :
            return self.missing_response
        else :
            raise ValueError("value %s not among declared "\
                             "set of categories: %s" %
                             (categories, self.categories.keys()))

def vectorLength(n) :
    vector_length = (n + 1) * n / 2 # (n + r - 1) choose r
    vector_length -= 1 
    return vector_length
    

def responseVector(value, vector_length) :
    response = numpy.zeros(vector_length)
    if value :
        response[value - 1] = 1
    return response

