import unittest

from .. import main

def test_entry_point():
    assert main() == "Here's the entry point"
