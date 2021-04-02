import unittest

import hello

class TestDemo(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test_add(self):
        """Test method add(a, b)"""
        print("hello")
        self.assertEqual(3, hello.add(1, 2))
       



# if __name__ == '__main__':
#     # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
#     unittest.main(verbosity=1)