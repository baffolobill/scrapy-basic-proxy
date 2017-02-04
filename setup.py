"""
Setup script for PyPi
"""
import codecs
import re
from setuptools import setup


# Open the package file so we can read the meta data.
with codecs.open('scrapy_basic_proxy.py', encoding='utf-8') as f:
    package_file = f.read()


def get_package_meta(meta_name):
    """Return value of variable set in the package where said variable is
    named in the Python meta format `__<meta_name>__`.
    """
    regex = "__{0}__ = ['\"]([^'\"]+)['\"]".format(meta_name)
    return re.search(regex, package_file).group(1)


version = get_package_meta('version')
author = get_package_meta('author')
license = get_package_meta('license')


setup(
    name='scrapy-basic-proxy',
    version=version,

    description='Scrapy Middleware to set a proxy for every Request.',

    author=author,
    url='https://github.com/baffolobill/scrapy-basic-proxy',

    license=license,

    py_modules=['scrapy_basic_proxy'],
    platforms=['Any'],

    keywords="scrapy proxy",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Scrapy',
    ]
)
