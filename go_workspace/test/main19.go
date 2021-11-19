package main

import (
	"fmt"
)

type IHello interface {
	Hello(name string)
}

type IHello2 interface {
	Hello2(name string)
}

type A struct {
}

func (a *A) Hello(name string) {
	fmt.Println("hello " + name + ", i am a")
}

type D struct {
}

func (*D) Hello(name string) {
	fmt.Println("hello " + name + ", i am d")
}
func (*D) Hello2(name string) {
	fmt.Println("hello2 " + name + ", i am d")
}

type B struct {
	IHello
}

func (*B) Hello(name string) {
	fmt.Println("hello " + name + ", i am b")
}

type C struct {
	IHello
	IHello2
}

func ttt(a IHello)  {
	a.Hello("ccccccc")
}
func ttt2(a IHello2)  {
	a.Hello2("ccccccc")
}

func main() {
	name := "Lee"
	a := A{}
	a.Hello(name) //hello Lee, i am a

	b := B{&A{}}
	b.Hello(name) //hello Lee, i am b
	b.IHello = &A{}
	b.IHello.Hello("aaa")

	b.IHello.Hello(name) //hello Lee, i am a

	c := C{IHello:&A{}}
	c.Hello(name) //hello Lee, i am a

	c.IHello2 = &D{}
	c.Hello(name) //hello Lee, i am d

	ttt(&A{})
	//ttt(&B{})
	//ttt(B{})
	ttt(&b)
	//ttt(b)
	//ttt(C{})
	ttt(c)
	ttt2(c)
	ttt(&D{})
}

