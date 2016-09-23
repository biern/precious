import setuptools


setuptools.setup(
    name="precious",
    version="0.1.0",
    url="https://github.com/biern/precious",

    author="Marcin Biernat",
    author_email="mb@marcinbiernat.pl",

    description="Value objects for Python",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[

    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
