from exception_assertion.myapp.sample import validate_age
import pytest


def test_validate_age_valid_age():
    validate_age(0)


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age can not be less than 0"):
        validate_age(-1)

