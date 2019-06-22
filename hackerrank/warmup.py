

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
        '''Return the number of instances of max in array.'''
        ar.sort()
        ar.reverse()
        count = 0
        for t in ar:
            if t == ar[0]:
                count += 1
            else:
                break
        return count

    def time_converter(self, s):
        '''Given time in AM/PM format, convert to 24-hr time.

        Input:
        A single string `s` containing a time in 24-hr clock format

        Output:
        Time in 24-hr format

        Notes: Midnight is 12:00:00AM on a 12-hour clock, and
        00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a
        12-hour clock, and 12:00:00 on a 24-hour clock.
        '''
        ss = s.split(':')
        if s[8:10] == 'PM':
            if int(ss[0]) == 12:
                result = f"12:{ss[1]}:{ss[2][0:2]}"
            elif int(ss[1]) >= 1:
                result = f"{int(ss[0]) + 12}:{ss[1]}:{ss[2][0:2]}"
        else:
            if int(ss[0]) == 12:
                result = f"00:{ss[1]}:{ss[2][0:2]}"
            else:
                result = f"{ss[0]}:{ss[1]}:{ss[2][0:2]}"
        return result
