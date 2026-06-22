import pytest

@pytest.mark.alpha  # Mark with label alpha
def test_one():
    assert 1

@pytest.mark.alpha  # Mark with label alpha
@pytest.mark.gamma
def test_two():
    assert 1

@pytest.mark.beta  # Mark with label beta
@pytest.mark.delta
def test_three():
    assert 1

if __name__ == "__main__":
    pytest.main([__file__, '-v', '-s',  '-m', 'alpha'])
    # pytest -v test_mark.py