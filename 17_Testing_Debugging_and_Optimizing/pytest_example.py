# pytest discovery scans for files named test_*.py or *_test.py,
# or scans files explicitly passed to pytest.
#
# Within those files, tests are discovered if they:
# - are a function at module scope and start with "test_", or
# - are in a class named "Test*" and are a method with name starting with "test_"
#
# Run this file using "pytest pytest_example.py"
#
import pytest

def test_passing_at_module_level():
    assert 1 == 1

def test_failing_at_module_level():
    assert 1 == 0

def test_error_at_module_level():
    assert 1 == 1
    1/0


class TestA:
    def test_passing(self):
        assert 1 == 1

    def test_failing(self):
        assert 1 == 0

    def test_error(self):
        assert 1 == 1
        1 / 0


# use raises to test when an expected exception is raised
with pytest.raises(ZeroDivisionError, match="zero"):
    1/0
