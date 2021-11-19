
package main
import (
	"fmt"
)
var (
	PlayRankings = map[string]bool{
		"11111": true,
		"222222": true,
		"33333": true,
	}
)

func init()  {
	checkService := "6666"
	if checkService == "555555" {
		fmt.Println(checkService)
	} else if _, ok := PlayRankings[checkService]; ok {
		fmt.Println(checkService)
	} else if checkService == "6666" {
		fmt.Println("6666")
	}

}

func main(){
	fmt.Println("ooooooooo")
}