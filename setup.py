from setuptools import setup, find_packages

setup(
    name='langchain',
    version='0.1',
    packages=['prompts', 'chains', 'chat_models', 'evaluation_qa', 'requests', 'tools', 'llms', 'document_loaders'],
    include_package_data=True,
    package_dir={'': 'libs/langchain/langchain'},
)
