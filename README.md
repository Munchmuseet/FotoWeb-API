# FotoWeb-API

## Introduction

The API contains paintings, graphics, drawings, sculptures, photographies and documentary photographies by Edvard Munch, as well as the Stenersen collections. The API can be used for the following purposes:
- Building custom user interfaces
- Building custom mobile apps
- Automating workflow
- Analytics

These are only examples. Any application that needs to read data from a FotoWeb server and maybe manipulate some of this data can make use of the FotoWeb API. See [FotoWare](https://learn.fotoware.com/02_FotoWeb_8.0/Integrating_FotoWeb_with_third-party_systems/001_The_FotoWeb_API) For full documentation.

The API is also documented on [Postman](https://documenter.getpostman.com/view/2789837/S1TPbLh5?version=latest).

## Overview
Dataformats:
- JSON

Supported methods:
- GET

Available archives in the Munch Museum's API are:
- 5014-Malerier (paintings)
- 5018-Grafikk (graphics)
- 5016-Tegninger (drawings)
- 5051-Skulpturer (sculptures)
- 5020-Fotografi (photographies)
- 5022-Dokumentarfoto (documentary photographies)
- 5042-Stenersensamlingene (the Stenersen collections)
## Authentication
No authentication is needed for the public entry point.
## Error codes
The most important status codes are:
- 400 Bad Request (The request was malformed)
- 401 Unauthorized (The client did not provide valid credentials or no credentials at all, and the type of request requires authentication)
- 404 Not Found (The request URL does not refer to any existing resource)
- 500 Internal Server Error (The request is valid, but there was a problem on the server-side)
---
### GET /fotoweb/
`https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier`

API descriptor: This is a JSON document, returned in the response body, which contains information about the API. See [link](https://learn.fotoware.com/02_FotoWeb_8.0/Integrating_FotoWeb_with_third-party_systems/001_The_FotoWeb_API/04_API_Entry_Points) for full documentation.

#### HEADERS
| Key | Value |
| --- | ----- |
| Accept | application/vnd.fotoware.api-descriptor+json |

#### Example requests

C#
```C#
var client = new RestClient("https://foto.munchmuseet.no/fotoweb/");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.api-descriptor+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```
cURL
```cURL
curl --location --request GET 'https://foto.munchmuseet.no/fotoweb/' \
--header 'Accept: application/vnd.fotoware.api-descriptor+json'
```
JavaScript jQuery
```JavaScript
var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.api-descriptor+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
---
### GET /fotoweb/archives/5014-Malerier
`https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier`

Asset list: The JSON representation of a list of assets in the FotoWeb RESTful API. Every collection has an asset list. See [link](https://learn.fotoware.com/02_FotoWeb_8.0/Integrating_FotoWeb_with_third-party_systems/001_The_FotoWeb_API/Asset_list_representation) for full documentation.

#### HEADERS
| Key | Value |
| --- | ----- |
| Accept | application/vnd.fotoware.assetlist+json |

#### Example requests

C#
```C#
var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.assetlist+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

cURL
```cURL
curl --location --request GET 'https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier' \
--header 'Accept: application/vnd.fotoware.assetlist+json'
```

JavaScript jQuery
```JavaScript
var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.assetlist+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```
