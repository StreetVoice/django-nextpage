from setuptools import setup, find_packages

version = '1.0.7'

LONG_DESCRIPTION = """
Usage just like django-pagination but only next and previous page is provided.
"""

setup(
    name='django-nextpage',
    version=version,
    description="django-nextpage",
    long_description=LONG_DESCRIPTION,
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
