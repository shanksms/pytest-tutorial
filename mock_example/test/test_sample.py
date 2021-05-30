from unittest import mock
from mock_example.app.sample import guess_number
from mock_example.app.sample import get_ip
import pytest


@pytest.mark.parametrize("_input, expected", [(3, "you won"), (4, "you lost")])
@mock.patch("mock_example.app.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("mock_example.app.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_response = mock.Mock(**{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})
    mock_requests_get.return_value = mock_response
    assert get_ip() == "0.0.0.0"
