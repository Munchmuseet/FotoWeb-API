# GET /fotoweb/

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.api-descriptor+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives/{archive}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives/5026-Malerier"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.assetlist+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives/{archive}/Arkiv/{filename}.info

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives/5026-Malerier/Arkiv/M0112_20190403.tif.info"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.asset+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.collectionlist+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives/{archive}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives/5026-Malerier"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.collection+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives/{archive}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives/5026-Malerier"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.collectioninfo+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /fotoweb/archives/{archive}/?{field name}={field content}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://foto.munchmuseet.no/fotoweb/archives/5026-Malerier/?105=vampire"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Accept", "application/vnd.fotoware.assetlist+json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}
