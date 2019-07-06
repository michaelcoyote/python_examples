from copy import deepcopy


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
        # This solution also works but I wanted to implement something more.
        # return arr.index(V)

    def insertion_sort_pt1(self, arr):
        '''Part one of Insertion Sort.

        1. store the value of arr[4]
        2. test lower index values successively from to until you reach value
           that is lower than arr[4]
        3. Each time test fails copy value to the lower index and print array.

         Each time your test fails, copy the value at the lower index
         to the current index and print your array. When the next lower
         indexed value is smaller than , insert the stored value at the
         current index and print the entire array.
        '''
        result = []
        # Start the test at the next to last space of the array.
        i = len(arr) - 2
        # Keep the array position and value of the array position we're
        # operating on.
        marker = len(arr) - 1
        hold = arr[marker]
        del(arr[marker])
        while i >= 0:
            p = arr[i]
            print(f'Array position {i}: {arr[i]} Hold: {hold}')
            if hold < arr[i]:
                # Insert value in new position and remove value in old position
                arr.insert(i, p)
                print('i' + str(arr))
                result.append(deepcopy(arr))
                del(arr[i + 1])
                # Decrement hold & marker if test succeeds
                marker = marker - 1
                i -= 1
            else:
                arr.insert(i + 1, hold)
                hold = -1
                print('e' + str(arr))
                result.append(deepcopy(arr))
                break
        if hold > 0:
            arr.insert(i + 1, hold)
            print('e' + str(arr))
            result.append(deepcopy(arr))
        return result

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
