from unittest import TestCase
from GroupTortureProject.Components.Switch import switch
test = switch ("Switch")


class Testswitch(TestCase):
    def test_output(self):
        test.Output([1,0,1])
        print(test.result)
        assert test.result == 0

