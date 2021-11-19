
package main
import (
	"fmt"
	"sync"
	"time"
)

// RWMutex 读写锁测试

const cost = time.Microsecond
type RWLock struct {
	count map[int]int
	mu    sync.RWMutex
}

func (l *RWLock) Write() {
	l.mu.Lock()
	l.count[1] ++
	//time.Sleep(cost)
	l.mu.Unlock()
}

func (l *RWLock) Read() {
	l.mu.RLock()
	e := l.count[1]
	fmt.Println(e)
	time.Sleep(cost)
	l.mu.RUnlock()
}


func main(){
	fmt.Println("ooooooooo")

	//tmp := RWLock{make(map[int]int), sync.RWMutex{}}
	//tmp := RWLock{count: make(map[int]int)}
	//tmp.count[1] = 1
	//
	//for i := 0; i< 10000;i++ {
	//	go tmp.Write()
	//	go tmp.Read()
	//}
	//time.Sleep(time.Second*2)
	//fmt.Println(tmp.count)

	ll := []int{}
	ll = append(ll, 1)
	ll =append(ll, 1)
	a := append(ll, 1)
	fmt.Println(ll)
	fmt.Println(a)

	fmt.Println(234/33)
}