# import pytest
import warmup


class TestBigSum(object):
    def test_bigsum_one(self):
        foo1 = warmup.Warmup()
        ar = ['1000000001', '1000000002', '1000000003',
              '1000000004', '1000000005']
        result = foo1.big_sum(ar)
        assert(result == 5000000015)


class TestDiagDiff(object):

    def test_dd_one(self):
        foo1 = warmup.Warmup()
        arr = [[11, 2, 4],
               [4, 5, 6],
               [10, 8, -12]]
        result = foo1.diagonal_difference(arr)
        assert(result == 15)


class TestPlusMinus(object):

    def test_pm_one(self):
        foo1 = warmup.Warmup()
        arr = '-4 3 -9 0 4 1'.split(' ')
        result = foo1.plus_minus(arr)
        assert(result == [0.500000, 0.333333, 0.166667])

    def test_pm_two(self):
        foo1 = warmup.Warmup()
        arr = ['0', '-67', '-74', '-38', '-72', '-53',
               '0', '-13', '-95', '-91', '-100', '-59',
               '0', '-10', '-68', '-71', '-62', '-21',
               '0', '-42', '-57', '-16', '-66', '-23',
               '0', '-80', '-63', '-68', '-65', '-71',
               '0', '-71', '-15', '-32', '-26', '-8',
               '0', '-6', '-51', '-87', '-19', '-71',
               '0', '-93', '-26', '-35', '-56', '-89',
               '0', '-21', '-74', '-39', '-57', '-8',
               '0', '-69', '-29', '-24', '-99', '-53',
               '0', '-65', '-42', '-72', '-18', '-4',
               '0', '-73', '-46', '-63', '-78', '-87']
        result = foo1.plus_minus(arr)
        assert(result == [0.000000, 0.833333, 0.166667])


class TestMinMaxSum(object):

    def test_minmax_one(self):
        foo1 = warmup.Warmup()
        # list(map(int, '1 2 3 4 5'.split(' ')))
        arr = [1, 2, 3, 4, 5]
        result = foo1.min_max_sum(arr)
        assert(result == [10, 14])


class TestBirthdayCandle(object):

    def test_birthday_candle_one(self):
        foo1 = warmup.Warmup()
        ar = [3, 2, 1, 3]
        result = foo1.birthday_candle(ar)
        assert(result == 2)

    def test_birthday_candle_two(self):
        foo1 = warmup.Warmup()
        ar = [4, 3, 2, 1, 3]
        result = foo1.birthday_candle(ar)
        assert(result == 1)


class TestTimeConverter(object):

    def test_time_converter_one(self):
        foo1 = warmup.Warmup()
        s = '07:05:45PM'
        result = foo1.time_converter(s)
        assert(result == '19:05:45')

    def test_time_converter_two(self):
        foo1 = warmup.Warmup()
        s = '12:00:00AM'
        result = foo1.time_converter(s)
        assert(result == '00:00:00')

    def test_time_converter_three(self):
        foo1 = warmup.Warmup()
        s = '12:40:22AM'
        result = foo1.time_converter(s)
        assert(result == '00:40:22')
