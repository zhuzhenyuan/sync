package main

import (
	"log"
	"os"
	"os/exec"
	"syscall"
)

func main() {
	cmd := exec.Command("sh")
	cmd.SysProcAttr = &syscall.SysProcAttr{
		//CAP_SYS_ADMIN:
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWUSER | syscall.CLONE_NEWNET,
		//Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWNET,
		// 内核3.19以上用这里
		UidMappings: []syscall.SysProcIDMap{
			{
				ContainerID: 1234,
				HostID:      0,
				Size:        1,
			},
		},
		GidMappings: []syscall.SysProcIDMap{
			{
				ContainerID: 1234,
				HostID:      0,
				Size:        1,
			},
		},
	}
	// 内核3.3，，在内核3.16不好使，原因未知
	// cmd.SysProcAttr.Credential = &syscall.Credential{Uid: 0, Gid: 0}  // 不要这行的话，会自动分配uid gid groups

	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		log.Println(err)
		log.Fatal(err)
	}
	os.Exit(-1)
}

//CLONE_NEWUSER 问题：fork/exec /bin/sh: operation not permitted
//内核4.4（or3.19以上）
//https://github.com/xianlubird/mydocker/issues/3
// 内核3.16 未解决
