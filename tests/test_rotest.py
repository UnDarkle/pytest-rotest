# -*- coding: utf-8 -*-
from rotest.core import TestCase, TestFlow, TestBlock, BlockInput, BlockOutput


class RotestCase(TestCase):
    """A passing test case."""
    def test_method(self):
        pass


class RotestBlockOutput(TestBlock):
    """A test block that creates an output."""
    value = BlockOutput()

    def test_method(self):
        self.value = 5


class RotestBlockInput(TestBlock):
    """A test block that creates an output."""
    value = BlockInput()

    def test_method(self):
        self.assertEqual(self.value, 5)


class RotestFlow(TestFlow):
    """An example for a test flow."""
    blocks = (RotestBlockOutput,
              RotestBlockInput)
