import pytest
from main_mock import get_weather


def test_get_weather(mocker):
    mock_get = mocker.patch('main_mock.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 10}
    }


    api_key = '94b58f3cb159aaa05717dbdced298c8a'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 10}
    }