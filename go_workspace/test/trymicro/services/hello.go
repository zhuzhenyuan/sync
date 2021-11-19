package main

import (
	"context"
	"fmt"

	proto "winmicro/proto"

	micro "github.com/micro/go-micro"
)

type Hello struct{}

func (h *Hello) Ping(ctx context.Context, req *proto.Request, res *proto.Response) error {
	res.Msg = "Hello " + req.Name
	return nil
}
func main() {
	service := micro.NewService(
		micro.Name("hellooo"), // 服务名称
	)
	service.Init()
	proto.RegisterHelloHandler(service.Server(), new(Hello))
	if err := service.Run(); err != nil {
		fmt.Println(err)
	}
}
