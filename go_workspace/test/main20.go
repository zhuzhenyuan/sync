package main

import "fmt"

type goods map[string]int

func main() {
	//var b = map[string]int{"sdfasf":234}
	var s = goods{"sdfsf": 3}
	fmt.Println(s)
	//var [][2]int
	for a, b := range [][2]int{{3,4}, {5,6}, {8,9}} {
		fmt.Println(a,b)
	}
	tt := []int{1,2,3}
	for idx, d := range tt{
		if d == 2{
			tt[idx] = 0
		}
	}
	fmt.Println(tt)

	t1 := 3
	switch t1 {
	case 1:
		fmt.Println(111)
	case 2:
		fmt.Println(222)
	default:
		fmt.Println("***")
	}

	t2 := map[int]int{1:1, 2:2, 3:3}
	for k, _ := range t2 {
		if k == 1 || k == 2{
			delete(t2, k)
		}
	}
	fmt.Println(t2)

}

