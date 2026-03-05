import unittest
import over

class TestTotal(unittest.TestCase):

    def setUp(self):
        self.obj = over.test()

    def test_total(self):
        self.assertEqual(self.obj.total([10,2]), 12)
    def test_high(self):
        self.assertEqual(self.obj.highest({
            "azmina": [22, 33],
            "azwa": [22, 23]}),"azmina")
    def test_average(self):
        self.assertEqual(self.obj.average([2,2]), 2)


if __name__ == "__main__":
    unittest.main()