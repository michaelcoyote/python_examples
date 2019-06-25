

class Sorting(object):

    def intro_tutorial(self, V, arr):
        '''Find location of number in array.

        Given a sorted array (arr) and a number(V), print index 
        location of V.

        Input:
        arr: a sorted array of integers
        V: an integer to search for

        Output: Index of V
        '''
        count = 0
        for i in arr:
            if i == V:
                return count
            count += 1
        # return arr.index(V)

    def median(self, arr):
        '''Return the median of an array w/ odd elements.'''
        arr.sort()
        return arr[int((len(arr) - 1) / 2)]

    def insertion_sort_analyse(self, arr):
        '''Analyse the amount of work required to sort array.

        Calculate number of shifts insertion sort performs sorting an
        array.
        This basically implements an insertion sort but places a counter
        on the inner loop to track the changes.
        https://en.wikipedia.org/wiki/Insertion_sort
        '''
        counter = 0
        for i in range(1, len(arr)):
            curval = arr[i]
            curpos = i
            while curpos > 0 and arr[curpos - 1] > curval:
                arr[curpos] = arr[curpos - 1]
                print(f'Moving value: {curval} from {curpos -1} to {curpos}')
                counter += 1
                curpos = curpos - 1
            arr[curpos] = curval
        print(arr)
        return counter

    def insertion_sort_analyse_two(self, arr):
        count = 0
        lvar = len(arr)
        for i in range(lvar):
            for j in range(i + 1, lvar):
                if arr[i] > arr[j]:
                    count += 1
        return(count)
