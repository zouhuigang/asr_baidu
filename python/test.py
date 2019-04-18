#!/usr/bin/python
# -*- coding:utf-8 -*-
# from ctypes import cdll
import ctypes
import json

# libasr = ctypes.cdll.LoadLibrary("./libasr.so")
# # result1=libasr.max(1,2)
# # result2=libasr.test(123,bytes("中国","utf8"),bytes("aass中国人bbb1232","utf8"))
# # result3=libasr.speek(bytes("/home/wwwroot/asrcash/pcm/16k-0.pcm","utf8"))
# result3.restype = ctypes.c_char_p
# # result3.argtypes = [c_char_p]

# print("result1:%d,result2:%d,result3:%s" % (result1,result2,result3))


so = ctypes.cdll.LoadLibrary
lib = so('./libasr.so')

#解析返回的c++ string
lib.speek.restype = ctypes.c_char_p
params=[
"/home/wwwroot/asrcash/pcm/16k-0.pcm",
"/home/wwwroot/asrcash/pcm/20190410_115435.pcm",
"/home/wwwroot/asrcash/pcm/20190410_133459.pcm"]
sv=lib.speek(bytes(json.dumps(params),"utf8"))
# sv=lib.speek(bytes("/home/wwwroot/asrcash/pcm/20190410_115435.pcm","utf8"))

# resultDict=json.loads(str(resultTxt), strict=False)
# sv = b'\xe9\x82\xb9\xe6\x85\xa7\xe5\x88\x9a'

#替换里面的中文
# sv=b'{"name": "json","b": "\xe9\x82\xb9\xe6\x85\xa7\xe5\x88\x9a"}'
print(sv.decode('utf-8'))


# print(resultTxt,type(resultTxt),str(resultTxt),sv.decode('utf-8'))

#https://www.kancloud.cn/lanyulei/python/357700
#http://www.mamicode.com/info-detail-2334929.html