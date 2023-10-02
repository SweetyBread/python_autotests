import requests
import pytest

url = "https://api.pokemonbattle.me:9104/" 

def test_status_code():
    response = requests.get(url+"trainers", params={'trainer_id': 1239})
    assert response.status_code == 200

def test_name_of_trainer():
    response = requests.get(url+"trainers", params={'trainer_id': 1239})
    assert response.json()['trainer_name'] == 'SweetyBread'