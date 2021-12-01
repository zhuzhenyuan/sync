package main

import (
	"fmt"
	"reflect"
)

func main() {

	type MyInt int
	var y MyInt = 7
	v2 := reflect.ValueOf(&y)
	fmt.Println(v2.Type())
	fmt.Println(v2.Type().Name())
	fmt.Println(v2.Kind())
	fmt.Println(v2)
	//v2.SetInt(11)
	//fmt.Println(y)

	v3 := v2.Elem()
	v3.SetInt(234)
	//v2
	fmt.Println(v3.Int())
	fmt.Println(y)
	y2 := v3.Interface().(MyInt) // y will have type float64.
	fmt.Println(y2)

}
