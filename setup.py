#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements_dev.txt', 'r') as f:
    requirements = list(f)

setup_requirements = [ ]

test_requirements = [ ]

packages = find_packages(include=['oqspy'])
packages.extend('oqspy.' + item for item in find_packages(where='oqspy'))


setup(
    author="Igor Yusipov",
    author_email='yusipov.igor@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Open Quantum Systems Modelling Package",
    entry_points={
        'console_scripts': [
            'oqspy=oqspy.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='oqspy',
    name='oqspy',
    packages=find_packages(include=['oqspy', 'oqspy.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/GillianGrayson/oqspy',
    version='0.1.3',
    zip_safe=False,
)
