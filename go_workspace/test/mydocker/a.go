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
		// 内核3.3可能不需要这里的代码(未测试）。    测试3.6是需要的， 内核3.19以上用这里。
		UidMappings: []syscall.SysProcIDMap{
			// 规则
			// 列表中只有一个就可以默认使用
			// 多个的话默认取HostID 为0的，没有0的则自动生成，除非指定(下Credential)
			{
				ContainerID: 1258,
				HostID:      0,
				Size:        1,
			},
			{
				ContainerID: 1259,
				HostID:      2,
				Size:        1,
			},
		},
		GidMappings: []syscall.SysProcIDMap{
			{
				ContainerID: 1254,
				HostID:      0,
				Size:        1,
			},
		},
	}
	// 内核3.3可能只需要这一行就可以
	// 如果指定，则使用指定id，必须在上面的UidMappings/GidMappings中,配合使用
	cmd.SysProcAttr.Credential = &syscall.Credential{Uid: 1259, Gid: 1254}  // 不要这行的话，会自动分配uid gid groups

	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		log.Println(err)
		log.Fatal(err)
	}
	os.Exit(-1)
}


// 问题记录
//CLONE_NEWUSER 问题：fork/exec /bin/sh: operation not permitted
//内核4.4（or3.19以上）
//https://github.com/xianlubird/mydocker/issues/3

// 内核3.16 未解决
//或许是go版本的原因
// https://aijishu.com/a/1060000000023988
// 可能是默认没有开启user namespace
// https://githubmemory.com/repo/xianlubird/mydocker/issues/3?page=2
// https://zhuanlan.zhihu.com/p/31871814

// 最终解决 96上
// mount -t proc proc /proc
// 不知道为啥需要挂载一下
// done
