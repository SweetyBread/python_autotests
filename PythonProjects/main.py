import requests
import random
from faker import Faker

token = "СЮДА НУЖНО ВСТАВИТЬ ТОКЕН СВОЕГО ТРЕНЕРА!!!"
url = "https://api.pokemonbattle.me:9104/"

fake = Faker()
name = fake.name()
print(name)

random_number = random.randint(1, 1008)
random_number_formatted = f"{random_number:03d}"
photo_url = f"https://dolnikov.ru/pokemons/albums/{random_number_formatted}.png"
print(photo_url)

response_create = requests.post(url+"pokemons",
    json = {
    "name": name,
    "photo": photo_url
    }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})

print(response_create.text)
json_response = response_create.json()
id = json_response['id']

fake = Faker()
name = fake.name()
print(name)

random_number = random.randint(1, 1008)
random_number_formatted = f"{random_number:03d}"
photo_url = f"https://dolnikov.ru/pokemons/albums/{random_number_formatted}.png"
print(photo_url)

response_change = requests.put(url+"pokemons",
     json = {
    "pokemon_id" : id,
    "name": name,
    "photo": photo_url
    }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})

print(response_change.text)
json_response = response_change.json()
id = json_response['id']

response_catch = requests.post(url+"trainers/add_pokeball",
    json = {
    "pokemon_id" : id,
    }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})

print(response_catch.text)