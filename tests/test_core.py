import core
import pytest


class TestCore:

    @pytest.mark.class1
    def test_core(self):
        instance1 = core.MyClass1()
        assert instance1

    @pytest.mark.class2
    def test_core(self):
        instance2 = core.MyClass2()
        assert instance2
