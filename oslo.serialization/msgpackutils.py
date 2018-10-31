# -*- coding: utf-8

from oslo_serialization import msgpackutils
import uuid
import datetime
import six

u1 = uuid.uuid1()
m1 = msgpackutils.UUIDHandler()
s1 = m1.serialize(u1)
print(s1)
u11 = m1.deserialize(s1)
print(type(u11))
print(u11)

dth = msgpackutils.DateTimeHandler(msgpackutils.default_registry)
dt = datetime.datetime(2018, 10, 31)
print(dt)
a = dth.serialize(dt)
print(a)
b = dth.deserialize(a)
print(b)

class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class ColorHandler(object):
    handles = (Color, )
    identity = (msgpackutils.HandlerRegistry.non_reserved_extension_range.min_value + 1)

    @staticmethod
    def serialize(obj):
        blob = '%s, %s, %s' % (obj.r, obj.g, obj.b)
        if six.PY3:
            blob = blob.encode('ascii')

        print("color blob: ", blob)
        return blob
    
    @staticmethod
    def deserialize(data):
        chunks = [int(c.strip()) for c in data.split(b",")]
        return Color(chunks[0], chunks[1], chunks[2])

registry = msgpackutils.default_registry.copy(unfreeze=True)
registry.register(ColorHandler())

c = Color(255, 254, 253)
c_b = msgpackutils.dumps(c, registry=registry)
print(c_b)
c = msgpackutils.loads(c_b, registry=registry)
print(c.r, c.g, c.b)

'''
msgpackutils 用于将python中的数据对象（某种类型，如这里的UUID，Color）串行化到文件或者字符串变量中。
方法及过程为：
1. 定义对象
2. 定对象的处理逻辑，主要包含四个部分：
  a. handles 变量：用于表明可以处理的数据类型。
  b. identity 变量：用于串行化到字符串中表明原有数据类型。
  c. serialize 函数：用于串行化对象
  d. deserialize 函数：反串行化数据流（怎么串行化就怎么反过程处理）
3. 获取registry 对象，相当于一个namespace，所有的处理过程的定义在一个registry下。
4. 注册串行化Handler到registry。
5. 使用：
  a. msgpackutils.loads/dumps/load/dump 这都需要一个registry即处理函数注册的空间作为参数。
'''
