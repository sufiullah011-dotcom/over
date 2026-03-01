import over
import unittest
class TestTotal(unittest.TestCase):
    def test_total(self):
     self.assertEqual(over.total([10,2]), 12)

    def test_highest(self):
        self.assertEqual(
            over.highest([[100,1],[1,11]]),[100,1])

    def test_average(self):
        self.assertEqual(over.average([2,2]), 2)
if __name__=="__main__":
    unittest.main()