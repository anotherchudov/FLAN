from setuptools import setup, find_packages

setup(
    name='flan',
    version='0.1.0',
    packages=find_packages(include=['flan', 'flan.*']),
    package_data={'': ['v2/cot_data/*.tsv']},
    include_package_data=True
)
