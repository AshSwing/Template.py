import unittest

def foo() -> int:
    return 1

class Test{{project_name}}(unittest.TestCase):
    
    def test_foo(self):
        self.assertEqual(foo(), 1)

if __name__ == '__main__':
    unittest.main()