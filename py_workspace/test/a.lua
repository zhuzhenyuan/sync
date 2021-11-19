-- 元类
Rectangle = {area = 0, length = 0, breadth = 0}

-- 派生类的方法 new
function Rectangle:new(o,length,breadth)
  o = o or {}
  setmetatable(o, self)
  self.__index = self
  o.length = length or 0
  o.breadth = breadth or 0
  o.area = length*breadth;
  return o
end

-- 派生类的方法 printArea
function Rectangle:printArea ()
  print("矩形面积为 ",self.length*self.breadth)
end

r = Rectangle:new(nil,10,20)
r.length = 2
print(r.length)
print(r)
r:printArea()

r2 = Rectangle:new(nil,130,20)

print(r.length)
print(r2.length)
print(r2)
r2:printArea()
r:printArea()
