import unittest

from queens.test.solver import testSolver
from queens.test.checker import testChecker
from queens.test.candidate import testNextCandidate

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [ testChecker, testNextCandidate, testSolver ]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
