#!/usr/bin/env/ python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name = 'GitMon',
    version = '0.3',
    packages = find_packages(),
    scripts = ['gitmon/gitmon.py', 'gitmon/notifiers.py'],
    data_files = ['gitmon/git.png', 'gitmon/gitmon'],

    install_requires = ['gitpython >= 0.3', 'py_Growl >= 0.0.7'],

    #Metadata for PyPI
    author = 'Tomas Varaneckas',
    author_email = 'tomas.varaneckas@gmail.com',
    description = 'GitMon - The Git Repository Monitor',
    license = 'GPLv3',
    keywords = ['git', 'monitor', 'scm', 'repository'],
    url = 'http://spajus.github.com/gitmon/'
)