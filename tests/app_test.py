import unittest


class AppTestCase(unittest.TestCase):
    def test_method_1(self):
        self.assertTrue(True)
        
    def test_method_2(self):
        self.assertTrue(True)
        
    def test_method_3(self):
        self.assertTrue(False)
        
    def test_method_4(self):
        self.assertTrue(True)
        
        
if __name__ == "__main__":
    unittest.main()
