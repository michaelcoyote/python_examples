

class Warmup(object):

    def big_sum(self, ar):
        '''Sum up all numbers in an array.'''

        res = 0
        for i in ar:
            res += int(i)
        return res

    def diagonal_difference(self, arr):
        '''Calculate difference bettween sum of matrix diagonals.

        Calculate the absolute difference between the sums of the
        diagonals within a matrix.
        '''
        pri = 0
        sec = 0
        # Calculate both diagonals at once
        for i, r in zip(list(range(0, len(arr))),
                        list(reversed(range(0, len(arr))))):
            pri += arr[i][i]
            sec += arr[i][r]
        return abs(pri - sec)

    def plus_minus(self, arr):
        '''Calculate fractions and return decimal.

        Given an array of integers, calculate the fractions of
        its elements that are positive, negative, and are zeros.
        Print the decimal value of each fraction on a new line.

        Output Format:
        print the following lines:

        A decimal representing of the fraction of positive numbers
        in the array compared to its size.
        A decimal representing of the fraction of negative numbers
        in the array compared to its size.
        A decimal representing of the fraction of zeros in the
        array compared to its size.
        '''
        res = []
        cnt = [0, 0, 0]
        for n in arr:
            if int(n) > 0:
                cnt[0] += 1
            elif int(n) < 0:
                cnt[1] += 1
            else:
                cnt[2] += 1
        for c in cnt:
            res.append(round((c / len(arr)), 6))
        # On hacker rank I did this with string format statments
        # but the round() function does seem to work even with caveats
        # in the Python documentation that it may not
        return res

    def staircase(n):
        for i in range(0, n):
            hashes = '#' * (i + 1)
            print('{h:>{n}}'.format(h=hashes, n=n))

    def min_max_sum(self, arr):
        '''Find min/max sum that can be generated w/ 4 of 5 integers.

        Given five positive integers, find the minimum and maximum
        values that can be calculated by summing exactly four of the
        five integers. Then print the respective minimum and maximum
        values as a single line of two space-separated long integers.

        Output Format
        Print two space-separated long integers denoting the respective
        minimum and maximum values that can be calculated by summing
        exactly four of the five integers. (The output can be greater
        than a 32 bit integer.)

        Note: Python 3 has only one integer type, which is called
        int but is equivalent to a Python 2 long which is unlimited.
        '''

        totals = []
        for i in range(0, len(arr)):
            totals.append(sum(arr[:i] + arr[(i + 1):]))
        totals.sort()
        return [totals[0], totals[-1]]

    def birthday_candle(self, ar):
        ar.sort() 
        ar.reverse()
        count = 0
        for t in ar:
            if t == ar[0]:
                count += 1
            else:
                break
        return count
