# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='{{cookiecutter.project_name}}',
    description='{{cookiecutter.project_description}}',
    version=':versiontools:{{cookiecutter.project_slug}}:',

    packages=find_packages(),
    include_package_data=True,
    setup_requires=('versiontools'),

    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_mail}}',
    url='{{cookiecutter.project_url}}',
)
