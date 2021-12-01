package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	//x := &struct {
	//	s string
	//}{"sdfs"}
	fmt.Println("type:", reflect.TypeOf(x))
	fmt.Println("name:", reflect.TypeOf(x).Name())
	fmt.Println("kind:", reflect.TypeOf(x).Kind())

	fmt.Println("value:", reflect.ValueOf(x))
	fmt.Println("kind:", reflect.ValueOf(x).Kind())
	fmt.Println("type:", reflect.ValueOf(x).Type())
	fmt.Println("kind is float64:", reflect.ValueOf(x).Kind() == reflect.Float64)
	fmt.Println("value:", reflect.ValueOf(x).Float())

	var xx uint8 = 'x'
	v := reflect.ValueOf(xx)
	fmt.Println("type:", v.Type())                            // uint8.
	fmt.Println("kind is uint8: ", v.Kind() == reflect.Uint8) // true.
	xx = uint8(v.Uint())                                       // v.Uint returns a uint64.

	type MyInt int
	var y MyInt = 7
	v2 := reflect.ValueOf(y)
	fmt.Println(v2.Type())
	fmt.Println(v2.Type().Name())
	fmt.Println(v2.Kind())
	fmt.Println(v2)
}