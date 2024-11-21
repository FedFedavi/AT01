import pytest
from main_git import get_github_user


def test_get_github_user(mocker):
    mock_get = mocker.patch('main_git.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nike'
    }

    user_data = get_github_user('nizavr')
    assert user_data == {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nike'
    }


def test_get_github_user_error(mocker):
    mock_get = mocker.patch('main_git.requests.get')
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': 345178,
        'name': 'Nik'
    }

    user_data = get_github_user('nizavr')
    assert user_data == None

