import requests


def count_words_at_url(url):
    responce = requests.get(url)
    return len(responce.text.split())