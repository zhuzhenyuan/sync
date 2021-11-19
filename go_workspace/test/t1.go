package main

import (
	"fmt"
	"net"
)

func main() {
	//name := "BraveChallenge"
	//s := strings.ToLower(name)
	//s := strings.ToLowerSpecial(name)
	//fmt.Printf(s+"\n")

	//_, subnet, _ := net.ParseCIDR("192.168.0.1/24")
	_, subnet, _ := net.ParseCIDR("127.0.0.0/8")
	fmt.Println(subnet.String())
	_, subnet, _ = net.ParseCIDR(subnet.String())
	fmt.Println(subnet.String())
	one, size := subnet.Mask.Size()
	fmt.Println(one, size)

	tt := make(map[int][]int)
	tt[1] = []int{1,2,3,4}

	tt[2] = append(tt[2], 4)
	tt[2] = append(tt[2], 5)
	fmt.Println(tt)
	fmt.Println(tt[3])

	//tt2 := make(map[int]map[int]int)
	//tt2[1] = map[int]int{1:1,2:2,3:3,4:4}
	//
	//tt[2][2] = 2
	//fmt.Println(tt)
}
