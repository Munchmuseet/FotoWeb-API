# GET /fotoweb/

import requests

url = "https://foto.munchmuseet.no/fotoweb/"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.api-descriptor+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives/{archive}

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives/5000-Malerier"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.assetlist+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives/{archive}/Assets/Arkiv/{filename}.info

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives/5000-Malerier/Assets/Arkiv/M0112_20190403.tif.info"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.asset+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.collectionlist+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives/{archive}

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives/5000-Malerier"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.collection+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives/{archive}

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives/5000-Malerier"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.collectioninfo+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /fotoweb/archives/{archive}/?{field name}={field content}

import requests

url = "https://foto.munchmuseet.no/fotoweb/archives/5000-Malerier/?105=vampire"

payload = {}
headers = {
  'Accept': 'application/vnd.fotoware.assetlist+json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
