# test_cryptomove.py
"""
Tests for CryptoMove module.
"""

import unittest
from cryptomove import CryptoMove

class TestCryptoMove(unittest.TestCase):
    """Test cases for CryptoMove class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoMove()
        self.assertIsInstance(instance, CryptoMove)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoMove()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
