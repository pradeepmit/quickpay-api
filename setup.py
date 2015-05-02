#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name='quickpay',
    packages=('quickpay', ),
    version='1.1',
    description=('''App that used to access the quickpay api with different functions to access this library just import the file as 
"from  quickpay import quickpayApi" and then create an object as "api = quickpayApi.Api()" now you can access all the methods as res1.method_name()'''
),
    author='Pradeep Singh | openerp4you',
    author_email='pradeep@openerp4you.in',
    url='http://www.openerp4you.in',
    install_requires=(
        'xmltodict',
        'hashlib',
        
        ),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        ]
 )
