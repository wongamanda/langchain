from setuptools import setup, find_packages

setup(
    name='langchain',
    version='0.1',
    packages=find_packages(where='/libs/langchain/langchain'),
    package_dir={'': 'libs/langchain/langchain'},
)
