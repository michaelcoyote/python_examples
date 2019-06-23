

class Sorting(object):

    def median(self, arr):
        '''Return the median of an array w/ odd elements.'''
        arr.sort()
        return arr[int((len(arr) - 1) / 2)]
