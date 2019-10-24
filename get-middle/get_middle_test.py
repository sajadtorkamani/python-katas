import unittest
from get_middle import get_middle

class GetMiddleTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEquals(get_middle("test"),"es")
        self.assertEquals(get_middle("testing"),"t")
        self.assertEquals(get_middle("middle"),"dd")
        self.assertEquals(get_middle("A"),"A")
        self.assertEquals(get_middle("of"),"of")

  
if __name__ == "__main__":
  unittest.main()
