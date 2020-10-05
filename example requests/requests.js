// GET /fotoweb/

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


// GET /fotoweb/archives/{archive}

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


// GET /fotoweb/archives/{archive}/Arkiv/{filename}.info

var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier/Arkiv/M0112_20190403.tif.info",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.asset+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /fotoweb/archives

var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.collectionlist+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /fotoweb/archives/{archive}

var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.collection+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /fotoweb/archives/{archive}

var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.collectioninfo+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /fotoweb/archives/{archive}/?{field name}={field content}

var settings = {
  "url": "https://foto.munchmuseet.no/fotoweb/archives/5014-Malerier/?105=vampire",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/vnd.fotoware.assetlist+json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
