// 从控制台读取输入:
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	firstName, lastName, s string
)

func main() {
	fmt.Println("Please enter your full name: ")
	//读一个
	fmt.Scanln(&firstName, &lastName)
	fmt.Println(firstName, lastName)
	fmt.Println(firstName+lastName)

	// 读一行
	var a, b int
	input := bufio.NewScanner(os.Stdin)
	// input.Scan() 读一行 input.Text()取一行
	for input.Scan() {
		if input.Text() == "" {
			return
		}
		fmt.Println(input.Text())
		a, _ = strconv.Atoi(strings.Split(input.Text(), " ")[0])
		b, _ = strconv.Atoi(strings.Split(input.Text(), " ")[1])
		fmt.Println(a+b)
	}

	// 转换
	//string --> int：将字符串13转换为int类型的数值13
	str := "13"
	distInt,err := strconv.Atoi(str)

	//string --> int64
	// 参数1：带转换字符串，
	// 参数2：基于几进制，值可以是0,8,16,32,64
	// 参数3：要转成哪个int类型：可以是0、8、16、32、64，分别对应 int,int8,int16,int32,int64
	distInt64, err := strconv.ParseInt(str, 10, 64)

	//string --> float64、float32
	// ParseFloat 将字符串转换为浮点数
	// str：要转换的字符串
	// bitSize：指定浮点类型（32:float32、64:float64）
	// 如果 str 是合法的格式，而且接近一个浮点值，
	// 则返回浮点数的四舍五入值（依据 IEEE754 的四舍五入标准）
	// 如果 str 不是合法的格式，则返回“语法错误”
	// 如果转换结果超出 bitSize 范围，则返回“超出范围”
	//到float64
	distFloat,err := strconv.ParseFloat(str,64)
	//到float32
	distFloat,err := strconv.ParseFloat(str,32)

	//int、int64转其它
	i := 11
	str1 := strconv.Itoa(i)
	//或
	str2 := strconv.FormatInt(int64(i),10)

	//int64 --> string
	distStr := strconv.FormatInt(num,10)

	//float --> string
	// FormatFloat 将浮点数 f 转换为字符串值
	// f：要转换的浮点数
	// fmt：格式标记（b、e、E、f、g、G）
	// prec：精度（数字部分的长度，不包括指数部分）
	// bitSize：指定浮点类型（32:float32、64:float64）
	// 格式标记：
	// 'b' (-ddddp±ddd，二进制指数)
	// 'e' (-d.dddde±dd，十进制指数)
	// 'E' (-d.ddddE±dd，十进制指数)
	// 'f' (-ddd.dddd，没有指数)
	// 'g' ('e':大指数，'f':其它情况)
	// 'G' ('E':大指数，'f':其它情况)
	// 如果格式标记为 'e'，'E'和'f'，则 prec 表示小数点后的数字位数
	// 如果格式标记为 'g'，'G'，则 prec 表示总的数字位数（整数部分+小数部分）
	str1 = strconv.FormatFloat(11.34,'E',-1,32)
	str2 = strconv.FormatFloat(10.55,'E',-1,64)
	fmt.Println(str1,str2)	//1.134E+01  1.055E+01
	//解析转换后的string变量str为float
	h,_ :=strconv.ParseFloat(str1,32)
	fmt.Println(h)	//11.34000015258789
	h,_ =strconv.ParseFloat(str2,64)
	fmt.Println(h)	//10.55


	//float64 --> int64(会有精度损失
	var x float64 = 6.9
	y := int64(x)
}
