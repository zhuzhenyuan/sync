package main

import (
	"fmt"
	"log"
	"os/exec"
	"time"
)

func init() {
	log.Println("plugin init function called")
}

type A struct {
	s string
	i int
}

type GoodDoctor interface {
	HealthCheck(a A) error
}

type BadNastyDoctor string

func (g BadNastyDoctor) HealthCheck(a A) error {
	bs, err := exec.Command("ls").CombinedOutput()
	if err != nil {
		return err

	}
	log.Println("now is", g)
	log.Println("shell has executed ->>>>>", string(bs))
	log.Println(a)
	//log.Println(gg)
	return nil
}

//go build -buildmode=plugin -o=plugin_doctor.so plugin_bad_docter.go

// exported as symbol named "Doctor"
var Doctor = BadNastyDoctor(time.Now().Format(time.RFC3339))

func main() {
	fmt.Println("11111111")
	//Doctor.HealthCheck()
	//doctor, ok := Doctor.(GoodDoctor)
	var doctor GoodDoctor = Doctor
	//if !ok {
	//	fmt.Println(doctor)
	//	fmt.Println("unexpected type from module symbol")
	//	os.Exit(1)
	//}
	doctor.HealthCheck(A{
		"sdafsdfas",
		999,
	})
}
