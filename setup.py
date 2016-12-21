from __future__ import unicode_literals

import imp
import os

from setuptools import (
    find_packages,
    setup,
)

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))
init = os.path.join(ROOT, 'src', 'admin_page_lock', '__init__.py')
app = imp.load_source('page_lock', init)


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def fread(fname):
    return open(fname).read()


setup(
    name=app.NAME,
    version=app.VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='Apache License, Version 2.0',
    description='Page Lock application prevents users being able to edit '
                'same page defined by its unique URL at the same time. '
                'The application is tailored to django admin implementation.',
    long_description=fread('README.rst'),
    url='https://github.com/ShowMax/django-admin-page-lock',
    author='Vojtech Stefka',
    author_email='vojtech.stefka@gmail.com',
    keywords=['django', 'admin', 'locking', 'concurrency'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Framework :: Django locking concurrency page view',
        'Framework :: Django :: 1.8',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
)