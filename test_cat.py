import pytest
from main_cat import get_cat_pick


def test_get_cat(mocker):
    mock_get = mocker.patch('main_cat.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'id': '3aa',
        'url': 'https://cdn2.thecatapi.com/images/3aa.jpg',
        'width': 425,
        'height': 640
    }]
    cat_data = get_cat_pick()
    assert cat_data == [{
        'id': '3aa',
        'url': 'https://cdn2.thecatapi.com/images/3aa.jpg',
        'width': 425,
        'height': 640
    }]


def test_get_cat_err(mocker):
    mock_get = mocker.patch('main_cat.requests.get')
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = [{
        'id': '3aa',
        'url': 'https://cdn2.thecatapi.com/images/3aa.jpg',
        'width': 425,
        'height': 640
    }]
    cat_data = get_cat_pick()
    assert cat_data == None

