from setuptools import setup, find_packages

setup(
    name='langchain',
    version='0.1',
    packages=['langchain'],
    include_package_data=True,
    package_dir={'': 'libs/langchain/langchain'},
)
