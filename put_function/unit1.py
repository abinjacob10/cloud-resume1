import unittest

class Testing1(unittest.TestCase):
  
  def tests(self):
    self.message1="unit1"
    return print(self.message1)



if __name__ == "__main__":
  unittest.main()