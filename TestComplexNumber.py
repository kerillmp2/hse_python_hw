import unittest
from ComplexNumber import ComplexNumber

class TestComplexNumber(unittest.TestCase):
  
    def setUp(self):
        pass
  
    
    def test_add(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    for h in range(-10, 10):
                        first = ComplexNumber(i, k)
                        second = ComplexNumber(j, h)
                        expected = ComplexNumber(i + j, k + h)
                        self.assertEqual(first + second, expected)

                        
    def test_sub(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    for h in range(-10, 10):
                        first = ComplexNumber(i, k)
                        second = ComplexNumber(j, h)
                        expected = ComplexNumber(i - j, k - h)
                        self.assertEqual(first - second, expected)
                        
                        
        
    def test_mult(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    for h in range(-10, 10):
                        first = ComplexNumber(i, k)
                        second = ComplexNumber(j, h)
                        expected = ComplexNumber(i * j - k * h, k * j + h * i)
                        self.assertEqual(first * second, expected)
                        
                        
    def test_abs(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                first = ComplexNumber(i, j)
                expected = (i ** 2 + j ** 2) ** (1/2)
                self.assertEqual(abs(first), expected)
                
                
    def test_eq(self):
        for i in range(-10, 10):
            for j in range(-10, 10):
                for k in range(-10, 10):
                    for h in range(-10, 10):
                        first = ComplexNumber(i, k)
                        second = ComplexNumber(j, h)
                        expected = (i == j and k == h)
                        self.assertEqual(first == second, expected)
                        
                        
if __name__ == "__main__":
    unittest.main()
