#!/usr/bin/env python3

import unittest
import loggz

from logfix.logfix import StacktraceFinder
from sample import LOG_STRING

loggz.setup()

LOG = loggz.factory('logfix')


class LogFixTestCases(unittest.TestCase):
    def test_find_exception(self):
        stacktrace_finder = StacktraceFinder(LOG_STRING.split('\n'))
        stacktrace_finder.run()
        self.assertEqual((1, 30), stacktrace_finder.positions[0])
        self.assertEqual((36, 42), stacktrace_finder.positions[1])
        self.assertEqual((45, 58), stacktrace_finder.positions[2])


if __name__ == '__main__':
    unittest.main()
