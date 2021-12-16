package main

import (
	"fmt"
	"reflect"
	"time"
)

func main() {
	x := &struct {
		DeleteAt time.Time
	}{}
	fmt.Println("type:", reflect.TypeOf(x))
	fmt.Println("name:", reflect.TypeOf(x).Name())
	fmt.Println("kind:", reflect.TypeOf(x).Kind())

	fmt.Println("value:", reflect.ValueOf(x))
	fmt.Println("kind:", reflect.ValueOf(x).Kind())
	fmt.Println("type:", reflect.ValueOf(x).Type())
	fmt.Println("kind is float64:", reflect.ValueOf(x).Kind() == reflect.Float64)
	fmt.Println(x.DeleteAt)
	t := reflect.ValueOf(x).Elem()
	d := t.FieldByName("DeleteAt")
	d.Set(reflect.ValueOf(time.Now()))
	fmt.Println(x.DeleteAt)
}