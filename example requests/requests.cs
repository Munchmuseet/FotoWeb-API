// GET /fotoweb/

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.api-descriptor+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);

// GET /fotoweb/archives/{archive}

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.assetlist+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);

// GET /fotoweb/archives/{archive}/Arkiv/{filename}.info

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier/Arkiv/M0112_20190403.tif.info");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.asset+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);

GET /fotoweb/archives

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.collectionlist+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


GET /fotoweb/archives/{archive}

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.collection+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


GET /fotoweb/archives/{archive}

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.collectioninfo+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


GET /fotoweb/archives/{archive}/?{field name}={field content}

var client = new RestClient("https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier/?105=vampire");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("Accept", "application/vnd.fotoware.assetlist+json");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
