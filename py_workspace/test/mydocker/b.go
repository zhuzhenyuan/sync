package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"path"
	"strconv"
	"syscall"
)

// add cgroup

const cgroupMemoryHierarchyMount = "/sys/fs/cgroup/memory"  // 默认关闭，因为耗资源

func main() {
	fmt.Println("0000")
	fmt.Println(os.Args)
	if os.Args[0] == "/proc/self/exe" {
		// 容器进程
		fmt.Printf("ccurrent pid %d", syscall.Getpid())
		fmt.Println()
		fmt.Println("11111111111111")
		cmd := exec.Command("sh", "-c", `stress --vm-bytes 1000m --vm-keep -m 1`)  // 阿里云超出100M就会被杀掉了 内核4.4，应该是没有设置交换分区的关系
		fmt.Println("55555555")
		cmd.SysProcAttr = &syscall.SysProcAttr{}
		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		if err := cmd.Run(); err != nil {
			fmt.Println("222222")
			fmt.Println(err)
			os.Exit(1)
		}
	}
	cmd := exec.Command("/proc/self/exe")  // 当前命令行窗口， todo 这样指令什么意思
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Start(); err != nil {
		fmt.Println("ERROR", err)
		os.Exit(1)
	} else {
		// 得到fork出来进程映射在外部命名空间的pid
		fmt.Printf("%v", cmd.Process.Pid)
		fmt.Println("3333")

		// 在系统默认创建挂在了memory subsystem的Hierarchy上创建cgroup
		os.Mkdir(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit"), 0755)
		// 将容器进程加入到这个cgroup中
		ioutil.WriteFile(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit", "tasks"), []byte(strconv.Itoa(cmd.Process.Pid)), 0644)
		// 限制cgroup进程使用
		ioutil.WriteFile(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit", "memory.limit_in_bytes"), []byte("100m"), 0644)  // 内核4.9确实如此，限制在指定数值

	}
	fmt.Println("4444")
	cmd.Process.Wait()
	//
	//
	//
	//cmd := exec.Command("sh")
	//cmd.SysProcAttr = &syscall.SysProcAttr{
	//	//CAP_SYS_ADMIN:
	//	Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWUSER | syscall.CLONE_NEWNET,
	//	// 内核3.3可能不需要这里的代码(未测试）。    测试3.6是需要的， 内核3.19以上用这里。
	//	UidMappings: []syscall.SysProcIDMap{
	//		// 规则
	//		// 列表中只有一个就可以默认使用
	//		// 多个的话默认取HostID 为0的，没有0的则自动生成，除非指定(下Credential)
	//		{
	//			ContainerID: 1258,
	//			HostID:      0,
	//			Size:        1,
	//		},
	//		{
	//			ContainerID: 1259,
	//			HostID:      2,
	//			Size:        1,
	//		},
	//	},
	//	GidMappings: []syscall.SysProcIDMap{
	//		{
	//			ContainerID: 1254,
	//			HostID:      0,
	//			Size:        1,
	//		},
	//	},
	//}
	//// 内核3.3可能只需要这一行就可以
	//// 如果指定，则使用指定id，必须在上面的UidMappings/GidMappings中,配合使用
	//cmd.SysProcAttr.Credential = &syscall.Credential{Uid: 1259, Gid: 1254}  // 不要这行的话，会自动分配uid gid groups
	//
	//cmd.Stdin = os.Stdin
	//cmd.Stdout = os.Stdout
	//cmd.Stderr = os.Stderr
	//if err := cmd.Run(); err != nil {
	//	log.Println(err)
	//	log.Fatal(err)
	//}
	//os.Exit(-1)
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
