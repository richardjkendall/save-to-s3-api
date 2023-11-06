from random import randint
import requests

c = 0
mx = 100

towns = [
  "Melbourne",
  "Sydney",
  "Brisbane",
  "Monington",
  "Perth",
  "Geelong",
  "Toowoomba",
  "Scarborough",
  "York",
  "Leeds",
  "London"
]

colours = [
  "green",
  "red",
  "blue",
  "yellow",
  "amber",
  "purple",
  "brown",
  "white",
  "black",
  "orange",
  "olive",
  "violet"
]

while c < mx:
  age = randint(18,70)
  town = towns[randint(0, len(towns)-1)]
  colour = colours[randint(0, len(colours)-1)]
  print(f"age: {age}, hometown: {town}, colour: {colour}")
  tosend = {
    "age": age,
    "fav_colour": colour,
    "hometown": town
  }
  resp = requests.post(
    url = "",
    json = tosend,
    headers = {
      "x-api-key": ""
    }
  )
  print(f"response code: {resp.status_code}")
  c = c + 1