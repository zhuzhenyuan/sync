package main

import (
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
	"time"
)

func Logger() gin.HandlerFunc {
	return func(c *gin.Context) {
		t := time.Now()
		// 给Context实例设置一个值
		c.Set("geektutu", "1111")
		// 请求前
		log.Println("1111111")
		c.Next()
		// 请求后
		log.Println("2222222222")
		latency := time.Since(t)
		log.Print(latency)
	}
}

func main() {
	r := gin.Default()
	r.Use(Logger())
	r.GET("/", func(c *gin.Context) {
		c.String(200, "Hello, Geektutu")
	})
	// 匹配 /user/geektutu
	r.GET("/user/:name/*role", func(c *gin.Context) {
		name := c.Param("name")
		c.String(http.StatusOK, "Hello %s", name)
	})
	// 匹配users?name=xxx&role=xxx，role可选
	r.GET("/users", func(c *gin.Context) {
		name := c.Query("name")
		role := c.DefaultQuery("role", "teacher")
		c.String(http.StatusOK, "%s is a %s", name, role)
	})
	// POST
	r.POST("/form", func(c *gin.Context) {
		username := c.PostForm("username")
		password := c.DefaultPostForm("password", "000000") // 可设置默认值

		c.JSON(http.StatusOK, gin.H{
			"username": username,
			"password": password,
		})
	})
	// GET 和 POST 混合
	r.POST("/posts", func(c *gin.Context) {
		id := c.Query("id")
		page := c.DefaultQuery("page", "0")
		username := c.PostForm("username")
		password := c.DefaultPostForm("username", "000000") // 可设置默认值

		c.JSON(http.StatusOK, gin.H{
			"id":       id,
			"page":     page,
			"username": username,
			"password": password,
		})
	})
	//Map参数(字典参数)
	r.POST("/post", func(c *gin.Context) {
		ids := c.QueryMap("ids")
		names := c.PostFormMap("names")

		c.JSON(http.StatusOK, gin.H{
			"ids":   ids,
			"names": names,
		})
	})
	r.GET("/redirect", func(c *gin.Context) {
		c.Redirect(http.StatusMovedPermanently, "/")
	})

	r.GET("/goindex", func(c *gin.Context) {
		c.Request.URL.Path = "/"
		r.HandleContext(c)
	})
	// group routes 分组路由
	defaultHandler := func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"path": c.FullPath(),
		})
	}
	// group: v1
	v1 := r.Group("/v1")
	{
		v1.GET("/posts", defaultHandler)
		v1.GET("/series", defaultHandler)
	}
	// group: v2
	v2 := r.Group("/v2")
	{
		v2.GET("/posts", defaultHandler)
		v2.GET("/series", defaultHandler)
	}
	//单个文件
	r.POST("/upload1", func(c *gin.Context) {
		file, _ := c.FormFile("file")
		// c.SaveUploadedFile(file, dst)
		c.String(http.StatusOK, "%s uploaded!", file.Filename)
	})
	//多个文件
	r.POST("/upload2", func(c *gin.Context) {
		// Multipart form
		form, _ := c.MultipartForm()
		files := form.File["upload[]"]

		for _, file := range files {
			log.Println(file.Filename)
			// c.SaveUploadedFile(file, dst)
		}
		c.String(http.StatusOK, "%d files uploaded!", len(files))
	})
	type student struct {
		Name string
		Age  int8
	}

	r.LoadHTMLGlob("templates/*")

	stu1 := &student{Name: "Geektutu", Age: 20}
	stu2 := &student{Name: "Jack", Age: 22}
	r.GET("/arr", func(c *gin.Context) {
		log.Println("333333333")
		c.HTML(http.StatusOK, "arr.tmpl", gin.H{
			"title":  "Gin",
			"stuArr": [2]*student{stu1, stu2},
		})
	})

	// 作用于全局
	r.Use(gin.Logger())
	r.Use(gin.Recovery())

	// 作用于单个路由
	//r.GET("/benchmark", MyBenchLogger(), benchEndpoint)
	//
	// 作用于某个组
	//authorized := r.Group("/")
	//authorized.Use(AuthRequired())
	//{
	//	authorized.POST("/login", loginEndpoint)
	//	authorized.POST("/submit", submitEndpoint)
	//}

	r.Run() // listen and serve on 0.0.0.0:8080
}
