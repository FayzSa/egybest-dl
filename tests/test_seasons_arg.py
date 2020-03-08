
import os
import imp
import unittest
import operator
import warnings

class TestSeasonsArgument(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ResourceWarning)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.m = imp.load_source('egybest-dl', '{dir_path}{sep}..{sep}egybest-dl{sep}egybest-dl'.format(dir_path=dir_path, sep=os.sep))

    def test_seasons(self):
        self.assertListEqual(
            list(self.m.validate_seasons(None, None, [])),
            []
        )
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['1']),
            ((1, tuple()),)
        )
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['1', '2:', '3']),
            ((1, tuple()), (2, tuple()), (3, tuple()),)
        )
    
    def test_episodes(self):
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['1:1,2,3,4,5', '2:13', '3']),
            ((1, (1,2,3,4,5)), (2, (13,)), (3, tuple()),)
        )
        self.assertRaises(Exception, self.m.validate_seasons, None, None, ['1:a'])
        self.assertRaises(Exception, self.m.validate_seasons, None, None, ['1:a,b'])
        self.assertRaises(Exception, self.m.validate_seasons, None, None, ['1:a,1'])
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['5:>4']),
            ((5, (operator.gt, 4)),)
        )
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['1:<10']),
            ((1, (operator.lt, 10)),)
        )
        self.assertTupleEqual(
            self.m.validate_seasons(None, None, ['1:<8', '2', '3:>1']),
            ((1, (operator.lt, 8)), (2, tuple()), (3, (operator.gt, 1)),)
        )

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

