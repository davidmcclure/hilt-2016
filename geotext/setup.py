

from setuptools import setup, find_packages


setup(

    name='geotext',
    version='0.1.0',
    description='Extract toponyms from plain text.',
    url='https://github.com/davidmcclure/hilt-2016',
    license='MIT',
    author='David McClure',
    author_email='dclure@stanford.edu',
    packages=find_packages(),
    scripts=['bin/geotext'],

)
