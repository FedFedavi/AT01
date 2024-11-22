import requests


def get_cat_pick():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
        # return response.json()[0]['url']

    else:
        return None

# print(f"Ответ API_cat {get_cat_pick()}")
