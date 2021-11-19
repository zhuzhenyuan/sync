/// 可以引⼊的库和版本相关请参考 “环境说明”
// 必须定义⼀个 包名为 `main` 的包

package main

import (
	"fmt"
	"math"
)

func solution(ranks map[int]int) int {
	tmp := make(map[int]int)
	m := 0
	ret := 0
	for key, val := range ranks {
		c := int(math.Abs(float64(key - val)))
		tmp[key] = c
		if m < c {
			m = c
			ret = key
		}
	}
	//fmt.Println(m)
	//fmt.Println(tmp)

	for key, val := range tmp {
		//fmt.Println(key, val)
		if val == m {
			if ret < val {
				ret = key
			}
		} else {
			if val <= m {
				m = val
				ret = key
			}
		}
	}
	// fmt.Println("******")
	return ret

}
func main() {
	fmt.Println(solution(map[int]int{1: 10000, 10: 1000, 100: 100, 1000: 10, 10000: 1}))
	fmt.Println(solution(map[int]int{1: 10000, 10: 9, 100: 99, 1000: 1001}))
}
