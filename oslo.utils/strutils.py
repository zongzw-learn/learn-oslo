from oslo_utils import strutils

'''
some of the utils is useless... personally speaking.
'''

rlt = []
for n in ['t', 'true', 'on', 'y', 'yes', '1', 'x']:
    rlt.append(strutils.bool_from_string(n, strict=False, default=False))
print(rlt)

#print(strutils.check_string_length('zongzhaowei', name="myname", min_length=50))
# in check_string_length
#     raise ValueError(msg)
# ValueError: myname has 11 characters, less than 50.

print(strutils.mask_dict_password({'password': 'abcd d81juxmEW_',
                    'user': 'admin',
                    'home-dir': '/home/admin'},
                    '???'))
print(strutils.mask_dict_password({'password': '--password d81juxmEW_',
                    'user': 'admin',
                    'home-dir': '/home/admin'},
                    '???'))

print(strutils.mask_password("""{'password': '--password d81juxmEW_',
                    'user': 'admin',
                    'home-dir': '/home/admin'}""",
                    '???'))

