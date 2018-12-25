
'''

whole bundle of classifiers:
https://pypi.python.org/pypi?%3Aaction=list_classifiers

trove and python
https://stackoverflow.com/questions/9094220/trove-classifiers-definition

'''

'''
python setup.py sdist
python setup.py install 
'''

import setuptools

setuptools.setup(setup_requires=['pbr'], pbr=True)
