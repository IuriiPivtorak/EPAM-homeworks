# License MIT

import os
from setuptools import setup, find_packages

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def extract_requirements(file):
    """
    Extract requirements from requirements file
    :param file: path to requirements file
    :type file: str
    :return: list[str] -- list of requirements
    """
    with open(file, 'r') as file:
        return file.read().splitlines()


setup(
    name='stats',
    version='0.1',
    description='Package for statistical operations',
    author='Iurii Pivtorak',
    author_email='Pivtorakuv@yandex.ru',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=extract_requirements(os.path.join(ROOT_PATH, 'requirements', 'base.txt')),
    test_requires=extract_requirements(os.path.join(ROOT_PATH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    zip_safe=False
)
