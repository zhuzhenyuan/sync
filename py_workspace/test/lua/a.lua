--#!/usr/local/bin/lua
---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by TJ38.
--- DateTime: 2021/6/9 10:06
---
-- safsfasf
--[[safasdf
asdfasf
asfasd
asdfasffasd
asdfasfasdf]]

--print(1231323)
--print("hello world")
--print(b)
--print(nil)
--b = 1230
--print(b)
--b = "sfasf"
--print(b)
--b = nil
--print(b)

--
--local b = false
--local c = true
--print(b)
--print(c)
--
--print(type(b))
--print(type(c))
--
--function a()
--    print(2111111111111)
--end
--
--a()
--
--print(131*2342)
--print(234.23424*23)

tab1 = { key1 = "val1", key2 = "val2", "val3" }
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end

tab1.key1 = nil
tab1[1] = nil
print("---------")
for k, v in pairs(tab1) do
    print(k .. " - " .. v)
end


print(type(xx) == "nil")


if nil then
    print(1111)
else
    print(2222)
end
print("234" + '32453')


local a = {}
a["key"] = "value"
key = 10
a[key] = 22
a[key] = a[key] + 11
for k, v in pairs(a) do
    print(k .. " : " .. v)
end

local tbl = {"apple", "pear", "orange", "grape"}
for key, val in pairs(tbl) do
    print("Key", key)
    print("val", val)
end

a3 = {}
for i = 1, 10 do
    a3[i] = i
end
a3["key"] = "val"
print(a3["key"])
print(a3["none"])
print(a3["1"])
print(a3[1])


local a, b = 1,2
b, a = a, b
print(a, b)

print(a3.key)
print(a3)

a = {"one", "two", "three"}
for i, v in ipairs(a) do
    print(i, v)
end


function average(...)
   result = 0
   local arg={...}    --> arg 为一个表，局部变量
   for i,v in ipairs({...}) do
      result = result + v
   end
   print("总共传入 " .. select("#", ...) .. " 个数")
   return result/#{...}
end

print("平均值为",average(10,5,3,4,5,6))


function fwrite(fmt, ...)  ---> 固定的参数fmt
    return io.write(string.format(fmt, ...))
end

fwrite("runoob\n")       --->fmt = "runoob", 没有变长参数。
fwrite("%d%d\n", 1, 2)   --->fmt = "%d%d", 变长参数为 1 和 2

function f(...)
    a = select(3,...)  -->从第三个位置开始，变量 a 对应右边变量列表的第一个参数
    print (a)
    print (select(3,...)) -->打印所有列表参数
end

f(0,1,2,3,4,5)



do
    function foo(...)
        for i = 1, select('#', ...) do  -->获取参数总数
            local arg = select(i, ...); -->读取参数，arg 对应的是右边变量列表的第一个参数
            print("arg", arg);
        end
    end

    foo(1, 2, 3, 4, "qqq");
end

a = {1,2,3,4,5}
print(select(2, a))





array = {"Google", "Runoob"}

function elementIterator (collection)
   local index = 0
   local count = #collection
   -- 闭包函数
   return function ()
      index = index + 1
       if index <= count then
           --  返回迭代器的当前元素
           return collection[index]
       else
           return 9
       end
   end
end

print(elementIterator(array))

for element in elementIterator(array) do
   print(element)
end








