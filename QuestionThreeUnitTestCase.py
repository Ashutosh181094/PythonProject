import unittest
import QuestionThree


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = QuestionThree.EvaluateMatrix

    def test(self):
        self.assertEqual(self.obj.diagonalRightSum(4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]), 10)
        self.assertEqual(self.obj.diagonalLeftMultiply(4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]),
                         1152)
        self.assertNotEqual(self.obj.diagonalRightSum(4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]), 9)
        self.assertNotEqual(self.obj.diagonalLeftMultiply(4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]),
                         123)




