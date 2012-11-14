__author__ = 'mturilin'

from setuptools import setup, find_packages

setup(name='django-cms-markdown',
    version='0.1',
    description='Django CMS Markdown Plugin',
    author='Mikhail Turilin/Ilya Brodotsky',
    author_email='mturilin@gmail.com',
    url='github.com/mturilin/django-cms-markdown',
    packages=find_packages(),
    install_requires=[
        'markdown==2.1.1',
        'django',
        'django-cms'
    ],
)