import os

from setuptools import find_packages, setup

from django_etuovi import __version__

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django_etuovi",
    version=__version__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    license="MIT License",
    description="Django wrapper around Etuovi API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/City-of-Helsinki/django-etuovi",
    author="City of Helsinki",
    author_email="dev@hel.fi",
    install_requires=[
        "Django~=3.2.6",
        "lxml~=4.6.3",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-django"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
