from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='abbreviations_py',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    description='A simple package to replace abbreviations/contractions by full forms. Also works with slangs like b4 (before)',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
