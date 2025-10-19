# test_walletbuilder.py
"""
Tests for WalletBuilder module.
"""

import unittest
from walletbuilder import WalletBuilder

class TestWalletBuilder(unittest.TestCase):
    """Test cases for WalletBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletBuilder()
        self.assertIsInstance(instance, WalletBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
