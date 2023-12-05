from setuptools import setup, find_packages

setup(
    name='langchain',
    version='0.1',
    packages=['prompts', 'chains', 'chat_models', 'evaluation', 'tools', 'llms', 'document_loaders'],
    include_package_data=True,
    package_dir={'langchain': 'libs/langchain'},
)
