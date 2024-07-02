# test_my_script.py

import pytest
from src.my_script import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

if __name__ == "__main__":
    pytest.main()
