# -*- coding: utf-8 -*-
# @Author: xiweibo
# @Date:   2018-09-04 16:13:33
# @Last Modified by:   xiweibo
# @Last Modified time: 2018-09-04 17:27:51
import xmlrpclib

__HOST = 'localhost'
__PORT = '8000'

s = xmlrpclib.ServerProxy('http://' + __HOST + ':' + __PORT)
print s.pow(2, 3)
print s.add(2, 3)
print s.div(5, 2)

print s.system.listMethods()