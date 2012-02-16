from setuptools import setup, find_packages
from nextpage import __version__

long_description = open('README.rst').read()

setup(
    name='django-nextpage',
    version=__version__,
    description="django-nextpage",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='pagination,django',
    author='tzangms',
    author_email='tzangms@gmail.com',
    url='http://github.com/tzangms/django-nextpage',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
