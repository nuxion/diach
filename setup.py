from setuptools import setup, find_packages

setup(
    name="Diach",
    version="0.0.1",
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['diach=diach.cli:cli']
    },
    author="Xavier Petit",
    author_email="nuxion@gmail.com",
    license="MPL-2.0",
    url="https://github.com/nuxion",
    description="Work with dates from console"
)
