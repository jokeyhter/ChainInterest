# test_chaininterest.py
"""
Tests for ChainInterest module.
"""

import unittest
from chaininterest import ChainInterest

class TestChainInterest(unittest.TestCase):
    """Test cases for ChainInterest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainInterest()
        self.assertIsInstance(instance, ChainInterest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainInterest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
