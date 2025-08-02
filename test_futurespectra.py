# test_futurespectra.py
"""
Tests for FutureSpectra module.
"""

import unittest
from futurespectra import FutureSpectra

class TestFutureSpectra(unittest.TestCase):
    """Test cases for FutureSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureSpectra()
        self.assertIsInstance(instance, FutureSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
