import unittest
from ..sheets import trainings, roles, volunteers

from .. import *


def test_entry_point():
    assert main() == "Here's the entry point"

