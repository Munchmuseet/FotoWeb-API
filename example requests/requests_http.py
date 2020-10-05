# GET /fotoweb/

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.api-descriptor+json'
}
conn.request("GET", "/fotoweb/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives/{archive}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.assetlist+json'
}
conn.request("GET", "/fotoweb/archives/5014-Malerier", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives/{archive}/Arkiv/{filename}.info

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.asset+json'
}
conn.request("GET", "/fotoweb/archives/5014-Malerier/Arkiv/M0112_20190403.tif.info", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.collectionlist+json'
}
conn.request("GET", "/fotoweb/archives", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives/{archive}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.collection+json'
}
conn.request("GET", "/fotoweb/archives/5014-Malerier", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives/{archive}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.collectioninfo+json'
}
conn.request("GET", "/fotoweb/archives/5014-Malerier", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /fotoweb/archives/{archive}/?{field name}={field content}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("foto.munchmuseet.no")
payload = ''
headers = {
  'Accept': 'application/vnd.fotoware.assetlist+json'
}
conn.request("GET", "/fotoweb/archives/5014-Malerier/?105=vampire", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
