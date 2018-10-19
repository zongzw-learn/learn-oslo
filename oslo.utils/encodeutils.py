from oslo_utils import encodeutils
import sys

'''
Python3 becomes able to handle unicode, 
'''

str = "andrew zong"

print("system default encoding: " + sys.getdefaultencoding())

print(encodeutils.safe_decode(str))

print(encodeutils.safe_decode(str, incoming='ascii'))

print(encodeutils.safe_decode(str, incoming='utf-8'))

print(encodeutils.safe_decode(str, incoming='ISO-8859-1'))

print(encodeutils.safe_encode(str, incoming='ascii', encoding='ISO-8859-1'))

print(encodeutils.to_utf8(str))