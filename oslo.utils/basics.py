'''
pip install oslo.utils
'''

from oslo_utils import strutils

'''
utils: 


    dictutils
    encodeutils
    eventletutils
    excutils
    fileutils
    fixture
    importutils
    netutils
    reflection
    secretutils
    specs_matcher
    strutils
    timeutils
    units
    uuidutils
    versionutils


'''

slug = strutils.to_slug("input value")
print("strutils.to_slug", slug)
