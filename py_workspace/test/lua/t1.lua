---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by zhuzhenyuan.
--- DateTime: 2021/11/24 0:04
---

print("heoll world")
print(b)

a = {}
a[10000] = 1
print(#a)

b = {x=10, y=45; "one", "two", "three"}
print(b)
for k, v in ipairs(b) do
    print(k, v)
end
for i in 1,#b do
    print(i)
end
