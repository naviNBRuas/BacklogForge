import pytest

from app.rice import calculate_rice


def test_calculate_rice_basic():
    assert calculate_rice(reach=100, impact=3, confidence=1.0, effort=5) == 60.0


def test_calculate_rice_zero_effort_raises():
    with pytest.raises(ValueError):
        calculate_rice(reach=100, impact=3, confidence=1.0, effort=0)
