from unittest import TestCase
from GroupTortureProject.Components.Clock import clock

class Test(TestCase):
    def test_clock(self):
        d = clock("ael",1)
        print(d.Operate())
