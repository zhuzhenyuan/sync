package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"plugin"
)
type Driver interface {
	Name() string
}


func HelloHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	params := url.Values{}
	params.Set("ipAddress", query.Get("ipAddress"))
	params.Set("os", query.Get("os"))
	params.Set("gameCode", "FKDJXEN")

	Url, _ := url.Parse("http://appsmobile.damoregame.com/odc/chekIsp.do")
	Url.RawQuery = params.Encode()
	urlPath := Url.String()

	resp, err := http.Get(urlPath)
	if err != nil {
		panic(err.Error())
	}
	s, err := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	//ret := make(map[string]interface{})
	ret := struct {
		Code string
		Tag int
	}{}
	if json.Unmarshal(s, &ret) == nil {
		fmt.Println(ret)
		fmt.Println(ret.Tag == 1)
		//fmt.Println(int(ret["tag"].(float64)) == 1)
		//fmt.Println(ret["tag"].(string))
	}
	fmt.Println(ret)
	w.Write(s)
}

func ReloadHandler(w http.ResponseWriter, r *http.Request) {
	p, err := plugin.Open("driver.so")
	if err != nil {
		panic(err)
	}

	newDriverSymbol, err := p.Lookup("NewDriver")
	if err != nil {
		panic(err)
	}

	newDriverFunc := newDriverSymbol.(func() Driver)
	newDriver := newDriverFunc()
	fmt.Println(newDriver.Name())
}
func main () {
	http.HandleFunc("/aa", HelloHandler)
	http.HandleFunc("/reload", ReloadHandler)
	http.ListenAndServe("0.0.0.0:8000", nil)
}
